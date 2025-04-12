// ��c++�����д
#include<iostream>
#include <stdlib.h>
#include <string.h>
using namespace std;

typedef unsigned int size_t;

class small_block {
public:
    char* cur_usable_buffer;
    char* buffer_end;
    small_block* next_block;
    int no_enough_times;
};

class big_block {
public:
    char* big_buffer;
    big_block* next_block;
};

class memory_pool {
public:
    size_t small_buffer_capacity;
    small_block* cur_usable_small_block;
    big_block* big_block_start;
    small_block small_block_start[0];
    static memory_pool* createPool(size_t capacity);
    static void destroyPool(memory_pool* pool);
    static char* createNewSmallBlock(memory_pool* pool, size_t size);
    static char* mallocBigBlock(memory_pool* pool, size_t size);
    static void* poolMalloc(memory_pool* pool, size_t size);
    static void freeBigBlock(memory_pool* pool, char* buffer_ptr);
};

//-�����ڴ�ز���ʼ��
memory_pool* memory_pool::createPool(size_t capacity) {
    //-capacity��buffer���������ڳ�ʼ����ʱ��ȷ������������С���buffer���������С
    //-�����ȷ���һ��������ڴ�,���ڴ�������������ڴ���pool+small_block+small_block_buffers�����������.
    //-ΪʲôҪ����������(�������Ϊ��������)�������ڴ�����,��Ϊ���������ؿ������Ƚ�����.�����ֵ�ַ������Ůɢ���������ڴ�ĸ�������.
    size_t total_size = sizeof(memory_pool) + sizeof(small_block) + capacity;

    //����ռ䲢��ʼ��
    void* temp = malloc(total_size);
    memset(temp, 0, total_size);

    // ��������
    memory_pool* pool = (memory_pool*)temp;
    cout << "pool address:" << pool << endl;
    // small_buffer�㶨������
    // ��ʼ������һ��small_block��������big_block
    // С�ڴ�ļ���Ӧ���ӵ�һ��С�ڴ濪ʼ����
    pool->small_buffer_capacity = capacity;
    pool->big_block_start = nullptr;
    pool->cur_usable_small_block = (small_block*)(pool->small_block_start);

    // pool+1��1������memory_pool�Ĳ�������Ū���ˡ���ʱsbp��small_block��ָ��
    // temp��������ڴ滹���������֣��ڴ˷���
    small_block* sbp = (small_block*)(pool + 1);
    cout << "first small block address:" << sbp << endl;

    // ��ʼ��small_block����
    // sbp + 1 ��1����Ϊtemp��������ڴ滹��һ�����֣��ڴ˷���
    sbp->cur_usable_buffer = (char*)(sbp + 1);
    cout << "first small block buffer address:" << &sbp->cur_usable_buffer << endl;
    //-��һ�����õ�buffer���ǿ�ͷ������end=��ͷ+capacity
    sbp->buffer_end = sbp->cur_usable_buffer + capacity;
    sbp->next_block = nullptr;
    sbp->no_enough_times = 0;

    return pool;
};

//-�����ڴ��
void memory_pool::destroyPool(memory_pool* pool) {
    //-���ٴ��ڴ�
    // ��Ϊbig_block�ǵ����������������ͷ�big_buffer
    big_block* bbp = pool->big_block_start;
    while (bbp) {
        if (bbp->big_buffer) {
            free(bbp->big_buffer);
            bbp->big_buffer = nullptr;
        }
        bbp = bbp->next_block;
    }
    // big_block��С�ڴ���У��Ȼ�ͺ�С�ڴ��һ��������

    //-����С�ڴ�
    // �ӵڶ����ڵ㿪ʼ�����ͷţ���һ���ڵ�����ͷ�
    small_block* temp = pool->small_block_start->next_block;
    while (temp) {
        small_block* next = temp->next_block;
        free(temp);
        temp = next;
    }
    free(pool);
}

//-������small block��û���㹻�ռ���䣬�򴴽��µ�small block������size�ռ䣬���ط���ռ����ָ��
char* memory_pool::createNewSmallBlock(memory_pool* pool, size_t size) {
    //-�ȴ����µ�small block��ע�⻹��buffer
    size_t malloc_size = sizeof(small_block) + pool->small_buffer_capacity;
    void* temp = malloc(malloc_size);
    memset(temp, 0, malloc_size);

    //-��ʼ���µ�small block
    small_block* sbp = (small_block*)temp;
    cout << "new small block address:" << sbp << endl;

    //-��Խһ��small_block�Ĳ���,ԭ��ͬ��
    sbp->cur_usable_buffer = (char*)(sbp + 1);
    cout << "new small block buffer address:" << sbp->cur_usable_buffer << endl;
    sbp->buffer_end = (char*)temp + malloc_size;
    sbp->next_block = nullptr;
    sbp->no_enough_times = 0;

    //-���������Ϊ����ֵ
    char* res = sbp->cur_usable_buffer;
    // ������ָ����ƣ�Ԥ����size��С�Ŀռ�
    // ��һ����֪���ã�Ӧ����Ϊ�����ݰ�ȫ
    sbp->cur_usable_buffer = res + size;

    //-��ΪĿǰ������small_block��û���㹻�Ŀռ��ˡ�
    //-��ζ�ſ�����Ҫ�����̳߳ص�cur_usable_small_block��Ҳ����Ѱ�ҵ����
    small_block* p = pool->cur_usable_small_block;
    while (p->next_block) {
        if (p->no_enough_times > 4) {
            pool->cur_usable_small_block = p->next_block;
        }
        ++(p->no_enough_times); // ��Ϊ��ǰ����С�ڴ涼�޷����䣬���Ա�ʶ��ȫ����һ
        p = p->next_block;
    }

    // ����һ��������С�ڴ洮����
    //-��ʱp����ָ��ǰpool�����һ��small_block,���½ڵ����ȥ��
    p->next_block = sbp;

    //-��Ϊ���һ��block�п���no_enough_times>4����cur_usable_small_block���³�nullptr
    //-���Ի�Ҫ�ж�һ��
    if (pool->cur_usable_small_block == nullptr) {
        pool->cur_usable_small_block = sbp;
    }
    return res;//-�����·����ڴ���׵�ַ
}


//-��������ڴ�
char* memory_pool::mallocBigBlock(memory_pool* pool, size_t size) {
    //-�ȷ���size��С�Ŀռ䣬
    void* temp = malloc(size);
    memset(temp, 0, size);

    //-��big_block_start��ʼѰ��,ע��big block��һ��ջʽ����
    // ������Ԫ���ǲ��뵽ͷ����λ�á�
    big_block* bbp = pool->big_block_start;
    int i = 0;
    while (bbp) {
        // ��ǰ���ڿ����big_block_start����
        if (bbp->big_buffer == nullptr) {
            bbp->big_buffer = (char*)temp;
            // �Ѿ�����Ҫ���˳�����
            return bbp->big_buffer;
        }
        if (i > 3) {
            break;//-Ϊ�˱�֤Ч�ʣ���������ֻ�û�ҵ��п�buffer��big_block����ֱ�ӽ����µ�big_block
        }
        bbp = bbp->next_block;
        ++i;
    }

    // ���Կ������Ǵ�Ϊ��
    //-�����µ�big_block������Ƚ��Ѷ��ĵ㣬����Nginx����big_block��buffer��Ȼ��һ�������ַ�Ĵ��ڴ�
    //-����big_block������һ��С�ڴ棬�ǾͲ�Ӧ�û����������ַ��Ӧ�ñ������ڴ���ڲ��Ŀռ䡣
    //-���������и����޵��ڴ��malloc����
    big_block* new_bbp = (big_block*)memory_pool::poolMalloc(pool, sizeof(big_block));
    //-��ʼ��
    //����ǰbig_block��Ϊ��ͷ���뵽�ڴ����
    new_bbp->big_buffer = (char*)temp;
    new_bbp->next_block = pool->big_block_start;
    pool->big_block_start = new_bbp;

    //-���ط����ڴ���׵�ַ
    return new_bbp->big_buffer;
}

//-�����ڴ�
void* memory_pool::poolMalloc(memory_pool* pool, size_t size) {
    //-���ж�Ҫmalloc���Ǵ��ڴ滹��С�ڴ�
    if (size < pool->small_buffer_capacity) {//-�����С�ڴ�
        //-��cur small block��ʼѰ��
        small_block* temp = pool->cur_usable_small_block;
        do {
            //-�жϵ�ǰsmall block��buffer����������
            //-���������,ֱ�ӷ���
            if (temp->buffer_end - temp->cur_usable_buffer > size) {
                char* res = temp->cur_usable_buffer;
                temp->cur_usable_buffer = temp->cur_usable_buffer + size;
                return res;
            }
            temp = temp->next_block;
        } while (temp);
        //-������һ��small block���������䣬�򴴽��µ�small block;
        //-��small block�ڴ�����,ֱ��Ԥ�ȷ���size��С�Ŀռ�,���Է��ؼ���.
        return createNewSmallBlock(pool, size);
    }
    //-������ڴ�
    return mallocBigBlock(pool, size);
}

//-�ͷŴ��ڴ��buffer������
void memory_pool::freeBigBlock(memory_pool* pool, char* buffer_ptr) {
    big_block* bbp = pool->big_block_start;
    while (bbp) {
        if (bbp->big_buffer == buffer_ptr) {
            free(bbp->big_buffer);
            bbp->big_buffer = nullptr;
            return;
        }
        bbp = bbp->next_block;
    }
}

int main() {
    memory_pool* pool = memory_pool::createPool(1024);
    //-����С�ڴ�
    char* p1 = (char*)memory_pool::poolMalloc(pool, 2);
    cout << "little malloc1:" << &p1 << endl;
    char* p2 = (char*)memory_pool::poolMalloc(pool, 4);
    cout << "little malloc1:" << &p2 << endl;
    char* p3 = (char*)memory_pool::poolMalloc(pool, 8);
    cout << "little malloc1:" << &p3 << endl;
    char* p4 = (char*)memory_pool::poolMalloc(pool, 256);
    cout << "little malloc1:" << &p4 << endl;
    char* p5 = (char*)memory_pool::poolMalloc(pool, 512);
    cout << "little malloc1:" << &p5 << endl;

    //-���Է��䲻�㿪���µ�small block
    char* p6 = (char*)memory_pool::poolMalloc(pool, 512);
    cout << "little malloc1:" << &p6 << endl;

    //-���Է�����ڴ�
    char* p7 = (char*)memory_pool::poolMalloc(pool, 2048);
    cout << "big malloc1:" << &p7 << endl;

    char* p8 = (char*)memory_pool::poolMalloc(pool, 4096);
    cout << "big malloc1:" << &p8 << endl;

    //-����free���ڴ�
    memory_pool::freeBigBlock(pool, p8);

    //-�����ٴη�����ڴ�
    char* p9 = (char*)memory_pool::poolMalloc(pool, 2048);
    cout << "big malloc1:" << &p9 << endl;

    //-�����ڴ��
    memory_pool::destroyPool(pool);

    return 0;
}