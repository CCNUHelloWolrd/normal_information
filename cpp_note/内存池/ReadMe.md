此目录存放本周课后作业，可以在此文件添加作业题目、设计思路和流程图等

# 问题:

    实现内存池

# 设计思想

参考链接[Nginx 内存池实现](https://zhuanlan.zhihu.com/p/631952956)

适用场景、用户每隔一段时间会清空整个内存池，用户请求极端化分为两类：一类内存开销小，一类内存开销大，且后者的频次小。

特点：将内存分为大内存和小内存，使用不同的数据结构来存储。认定小内存仅需要在应用结束时释放，而大内存实时释放。

small_block 和 small_suffer 应当连续。且大小固定。
big_block 和 big_suffer 不需连续。大小不固定。

## 内存池数据结构

[整体结构](https://pic3.zhimg.com/v2-6d4351c9fb083df6169360bd2f164de4_1440w.jpg)
class memory_pool{
public:
size_t small_buffer_capacity;
small_block _ cur_usable_small_block;
big_block _ big_block_start;
small_block small_block_start[0];
static memory_pool _ createPool(size_t capacity);
static void destroyPool(memory_pool _ pool);
static char* createNewSmallBlock(memory_pool * pool,size_t size);
static char* mallocBigBlock(memory_pool * pool,size_t size);
static void* poolMalloc(memory_pool * pool,size_t size);
static void freeBigBlock(memory_pool * pool, char *buffer_ptr);
};

### 属性：

small_buffer_capacity：该值代表了 small buffer 的容量，在创建内存池的时候作为参数确定。
cur_usable_small_block：每次要分配小内存的时候，并不会从头开始找合适的空间，而是从这个指针指向的 small_block 开始找。
big_block_start：big block 链的链头
small_block_start：small block 的链头

注意点： small_block small_block_start[0];

### 方法：

createPool：创建内存池，同时创建第一个 small_block
destroyPool：回收内存池
createNewSmallBlock：创建新的小内存
mallocBigBlock：当遇到大内存时，分配内存
poolMalloc：分配内存，当遇到小内存时，在该方法实现，若大内存，evoke mallocBigBlock
freeBigBlock: 释放大内存

## small block 数据结构：

    class small_block{
    public:
    char * cur_usable_buffer;
    char * buffer_end;
    small_block * next_block;
    int no_enough_times;
    };

cur_usable_buffer：指向该 block 的可用 buffer 的首地址
buffer_end：指向该 block 的 buffer 的结尾地址
next_block: 指向 block 链的下一个 small block
no_enough_times：每次分配内存，看是否有足够分配的内存,如果在该 block 没找到，就会将该值+1,代表没有足够空间命中的次数。

## big block 的数据结构:

    class big_block{
    public:
    char * big_buffer;
    big_block * next_block;
    };

big_buffer：大内存 buffer 的首地址
next_block：指向下一个 big block

## 应用思路：

分配内存（poolMalloc）：

我们判断 poolMalloc 的 size 是一个大内存还是小内存。

如果是小内存，就从 cur_usable_small_block 这个 small block 开始找足够的空间去分配内存，不从 small block 链的开头开始寻找是为了加快搜索效率。
对于每个 small block，我们直接用 buffer_end 和 cur_usable_buffer 相减就可以得到一个 small buffer 的剩余容量去判断是否能分配。
如果空间足够，就从 cur_usable_buffer 开始分配 size 大小的空间，并返回这段空间的首地址，同时更新 cur_usable_buffer 指向新的剩余空间。
如果直到链的末尾都没有足够的 size 大小的空间，那就需要创建新的 small block。每次到了创建新的 small block 的环节，就意味着目前链上的 small buffer 空间已经都分配得差不多了，可能需要更新 cur_usable_small_block，这就需要用到 small block 的 no_enough_times 成员，将 cur_usable_small_block 开始的每个 small block 的该值++，Nginx 设置的经验值阈值是 4，超过 4，意味着该 block 不适合再成为寻找的开始了，需要往后继续尝试。

如果是大内存，只要从头开始遍历，如果有空 buffer 就返回该 block，如果超过 3 个还没找到就直接不找了，创建新的 big block。

释放内存（destroyPool）

big_buffer 是个大内存，所以其是个 malloc 的随机地址，

但是 big_block 本身是一个小内存，那就不应该还是用随机地址，应该保存在内存池内部的空间。

freeBigBlock
由于 big block 是一个链式结构，所以要找到对应的 buffer 并 free 掉，就需要从这个链的开头开始遍历，一直到找到位置。

pool 中有两条链分别指向大内存和小内存，那么分别沿着这两条链去 free 掉内存即可，由于大内存的 buffer 和 big block 不是一起 malloc 的，所以只需要 free 掉 buffer，而 big block 是分配在小内存池中的，所以，之后 free 掉小内存的时候会顺带一起 free 掉。

small 链的 free 不是从第一个 small block 开始的，第一个 small block 的空间是和 pool 一起 malloc 出来的，不需要 free，只要最后的时候 free pool 就会一起释放掉。

buffer_head_ptr = (char\*)small_block + sizeof(small_block);

整个内存池 pool 中有两条链，一条是 big block 链，一条是 small block 链。

一个 small block 我们可以看做是一个小缓冲区，而整条链的小缓冲区串起来组成一个大缓冲区，就是内存池了。

buffer_head_ptr = (char\*)small_block + sizeof(small_block);
