// 用c++风格重写
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

//-创建内存池并初始化
memory_pool* memory_pool::createPool(size_t capacity) {
    //-capacity是buffer的容量，在初始化的时候确定，后续所有小块的buffer都是这个大小
    //-我们先分配一大段连续内存,该内存可以想象成这段内存由pool+small_block+small_block_buffers三个部分组成.
    //-为什么要把三个部分(可以理解为三个对象)用连续内存来存,因为这样整个池看起来比较优雅.各部分地址不会天女散花地落在内存的各个角落.
    size_t total_size = sizeof(memory_pool) + sizeof(small_block) + capacity;

    //分配空间并初始化
    void* temp = malloc(total_size);
    memset(temp, 0, total_size);

    // 分配属性
    memory_pool* pool = (memory_pool*)temp;
    cout << "pool address:" << pool << endl;
    // small_buffer恒定，储存
    // 初始化创建一个small_block，不创建big_block
    // 小内存的检索应当从第一个小内存开始检索
    pool->small_buffer_capacity = capacity;
    pool->big_block_start = nullptr;
    pool->cur_usable_small_block = (small_block*)(pool->small_block_start);

    // pool+1的1是整个memory_pool的步长，别弄错了。此时sbp是small_block的指针
    // temp处申请的内存还有两个部分，在此分配
    small_block* sbp = (small_block*)(pool + 1);
    cout << "first small block address:" << sbp << endl;

    // 初始化small_block对象
    // sbp + 1 加1是因为temp处申请的内存还有一个部分，在此分配
    sbp->cur_usable_buffer = (char*)(sbp + 1);
    cout << "first small block buffer address:" << &sbp->cur_usable_buffer << endl;
    //-第一个可用的buffer就是开头，所以end=开头+capacity
    sbp->buffer_end = sbp->cur_usable_buffer + capacity;
    sbp->next_block = nullptr;
    sbp->no_enough_times = 0;

    return pool;
};

//-销毁内存池
void memory_pool::destroyPool(memory_pool* pool) {
    //-销毁大内存
    // 因为big_block是单独的链表，所以先释放big_buffer
    big_block* bbp = pool->big_block_start;
    while (bbp) {
        if (bbp->big_buffer) {
            free(bbp->big_buffer);
            bbp->big_buffer = nullptr;
        }
        bbp = bbp->next_block;
    }
    // big_block在小内存池中，等会就和小内存池一起销毁了

    //-销毁小内存
    // 从第二个节点开始依次释放，第一个节点最后释放
    small_block* temp = pool->small_block_start->next_block;
    while (temp) {
        small_block* next = temp->next_block;
        free(temp);
        temp = next;
    }
    free(pool);
}

//-当所有small block都没有足够空间分配，则创建新的small block并分配size空间，返回分配空间的首指针
char* memory_pool::createNewSmallBlock(memory_pool* pool, size_t size) {
    //-先创建新的small block，注意还有buffer
    size_t malloc_size = sizeof(small_block) + pool->small_buffer_capacity;
    void* temp = malloc(malloc_size);
    memset(temp, 0, malloc_size);

    //-初始化新的small block
    small_block* sbp = (small_block*)temp;
    cout << "new small block address:" << sbp << endl;

    //-跨越一个small_block的步长,原因同上
    sbp->cur_usable_buffer = (char*)(sbp + 1);
    cout << "new small block buffer address:" << sbp->cur_usable_buffer << endl;
    sbp->buffer_end = (char*)temp + malloc_size;
    sbp->next_block = nullptr;
    sbp->no_enough_times = 0;

    //-存个副本作为返回值
    char* res = sbp->cur_usable_buffer;
    // 将可用指针后移，预留出size大小的空间
    // 这一步不知何用，应该是为了数据安全
    sbp->cur_usable_buffer = res + size;

    //-因为目前的所有small_block都没有足够的空间了。
    //-意味着可能需要更新线程池的cur_usable_small_block，也就是寻找的起点
    small_block* p = pool->cur_usable_small_block;
    while (p->next_block) {
        if (p->no_enough_times > 4) {
            pool->cur_usable_small_block = p->next_block;
        }
        ++(p->no_enough_times); // 因为当前所有小内存都无法分配，所以标识符全部加一
        p = p->next_block;
    }

    // 在这一步将整个小内存串起来
    //-此时p正好指向当前pool中最后一个small_block,将新节点接上去。
    p->next_block = sbp;

    //-因为最后一个block有可能no_enough_times>4导致cur_usable_small_block更新成nullptr
    //-所以还要判断一下
    if (pool->cur_usable_small_block == nullptr) {
        pool->cur_usable_small_block = sbp;
    }
    return res;//-返回新分配内存的首地址
}


//-分配大块的内存
char* memory_pool::mallocBigBlock(memory_pool* pool, size_t size) {
    //-先分配size大小的空间，
    void* temp = malloc(size);
    memset(temp, 0, size);

    //-从big_block_start开始寻找,注意big block是一个栈式链，
    // 插入新元素是插入到头结点的位置。
    big_block* bbp = pool->big_block_start;
    int i = 0;
    while (bbp) {
        // 当前存在空余的big_block_start索引
        if (bbp->big_buffer == nullptr) {
            bbp->big_buffer = (char*)temp;
            // 已经满足要求，退出函数
            return bbp->big_buffer;
        }
        if (i > 3) {
            break;//-为了保证效率，如果找三轮还没找到有空buffer的big_block，就直接建立新的big_block
        }
        bbp = bbp->next_block;
        ++i;
    }

    // 可以看懂但是大为震撼
    //-创建新的big_block，这里比较难懂的点，就是Nginx觉得big_block的buffer虽然是一个随机地址的大内存
    //-但是big_block本身算一个小内存，那就不应该还是用随机地址，应该保存在内存池内部的空间。
    //-所以这里有个套娃的内存池malloc操作
    big_block* new_bbp = (big_block*)memory_pool::poolMalloc(pool, sizeof(big_block));
    //-初始化
    //将当前big_block作为表头加入到内存池中
    new_bbp->big_buffer = (char*)temp;
    new_bbp->next_block = pool->big_block_start;
    pool->big_block_start = new_bbp;

    //-返回分配内存的首地址
    return new_bbp->big_buffer;
}

//-分配内存
void* memory_pool::poolMalloc(memory_pool* pool, size_t size) {
    //-先判断要malloc的是大内存还是小内存
    if (size < pool->small_buffer_capacity) {//-如果是小内存
        //-从cur small block开始寻找
        small_block* temp = pool->cur_usable_small_block;
        do {
            //-判断当前small block的buffer够不够分配
            //-如果够分配,直接返回
            if (temp->buffer_end - temp->cur_usable_buffer > size) {
                char* res = temp->cur_usable_buffer;
                temp->cur_usable_buffer = temp->cur_usable_buffer + size;
                return res;
            }
            temp = temp->next_block;
        } while (temp);
        //-如果最后一个small block都不够分配，则创建新的small block;
        //-该small block在创建后,直接预先分配size大小的空间,所以返回即可.
        return createNewSmallBlock(pool, size);
    }
    //-分配大内存
    return mallocBigBlock(pool, size);
}

//-释放大内存的buffer，链表
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
    //-分配小内存
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

    //-测试分配不足开辟新的small block
    char* p6 = (char*)memory_pool::poolMalloc(pool, 512);
    cout << "little malloc1:" << &p6 << endl;

    //-测试分配大内存
    char* p7 = (char*)memory_pool::poolMalloc(pool, 2048);
    cout << "big malloc1:" << &p7 << endl;

    char* p8 = (char*)memory_pool::poolMalloc(pool, 4096);
    cout << "big malloc1:" << &p8 << endl;

    //-测试free大内存
    memory_pool::freeBigBlock(pool, p8);

    //-测试再次分配大内存
    char* p9 = (char*)memory_pool::poolMalloc(pool, 2048);
    cout << "big malloc1:" << &p9 << endl;

    //-销毁内存池
    memory_pool::destroyPool(pool);

    return 0;
}