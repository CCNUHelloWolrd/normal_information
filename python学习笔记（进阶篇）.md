# python学习个人感悟，汇集成笔记
在此记录目录，详细内容进入个人分支查看

## 参考资料

[进阶书籍1_在线阅读](https://eastlakeside.gitbook.io/interpy-zh/author)

[进阶书籍1_pdf链接](https://app.readthedocs.org/projects/intermediatepythongithubio/downloads/pdf/latest/)

## 摘要

1. python 环境配置，虚拟环境与主环境关系。（合适的工作场景）
2. python 代码执行，代码-->字节码-->汇编（理论工作效率）
3. python 库、包、模块、类、函数、语句 关系（大项目的工作理论）
4. python 自定义库并提交（让python几百万个库中有你的一份）
5. python Exception报错基类
6. python 装饰器
7. python os命令
7. python Log库日志
8. python 类型提示与.ipy文件
9. python 代码编写辅助工具(自动扩写、ai翻译、uml工具)
10. python 爬虫（静态、动态）
11. python 爬虫（绕过反爬虫）
12. python 调用api
13. python 游戏开发(pygame GUI)
14. python flask后端
15. python tkinter 应用开发
16. python postgresql 数据库连接

## 笔记（随笔）

以下内容随机排序

### 1. *args,  **kwargs

    python中可以采用 *来处理不定长变量，*args, **kwargs为约定俗成的处理不定长参数列表、参数字典，
    一般在函数定义中使用，和缺省型函数有点同样考虑,命名并不重要，重要的是*的语法。但是在函数外也可以使用，个人理解为解包和打包。
    当def fun(fargs, *args, **kwargs)时，除fargs形参外，没有键值对关系的变量被打包成列表args，
    有键值对关系的变量被打包成字典kwargs。当函数外有列表args, 字典kwargs时，使用 *和 ** 分别解包, 
    但是一般解包是为了解析数据或者作为形参传递给函数，不过需要注意解包后得到的数据格式是否合法。

用途： 装饰器、猴子补丁、数据集可视化

### 2. debug

    通常代码无法一次达到理想状态，此时需要debug，实际上debug的代码比实际代码还多。
    debug是痛苦的，但是debug收获是更多的。

方法: 断点打印法、IDE控制台分析法、pdb命令行调试法、

### 3. 迭代

    使用迭代器对可迭代对象进行迭代，可以减少代码对内存的消耗，有时还会提高运行效率。
    在py3中，迭代器已经成为了隐式的标准。
    最常用的迭代器是生成器，也就是仅储存必要的数值，每次调用现场计算返回值。
    迭代是一种思想，需要迭代器和迭代对象 两个元素，迭代操作。
    自定义迭代器需要在函数中使用yield关键字，对迭代对象进行迭代使用for语法糖或next()内置函数，
    将可迭代对象转化成迭代器使用iter()内置函数

用途：内存优化、软件效率提高、range、数据结构管理

示例：斐波那契数列的省内存、高效率、可控的实现,for, next, iter示例，注意for和next对StopIteration的处理
    def fun(n):
        a = 1
        for _ in range(1, n + 1):
            yield a
            a *= _
    
    
    # next 内置函数
    fang = fun(100000000000000000)
    for i in range(10):
        print(f"{i}的阶乘是：{next(fang)}")
    
    # for 算法糖
    text_1 = "我是一个可迭代对象，我现在可以通过for算法糖来迭代"
    for str_ in text_1:
        print(str_)
    
    # iter 内置函数
    text_1 = "我是一个可迭代对象，我现在可以通过iter 内置函数来迭代"
    text_1 = iter(text_1)
    for i in range(100000):
        print(next(text_1))

### 4. 高阶函数(快捷但不必须)
    map用于映射，用法map(function_to_apply, list_of_inputs), 返回迭代器
    匿名函数用于快捷处理，用法lambda x: x**2，两者相互配合
    filter用于过滤，用法filter(function_to_apply, list_of_inputs), 返回迭代器
    reduce用于整体处理列表，用法reduce(function_to_apply, list_of_inputs),返回一个变量
    需from functools import reduce 
    
示例：

    list_1 = [i for i in range(10)]
    ans = map(lambda x: x ** 2, list_1)
    print(list(ans))

    ans = filter(lambda x: x > 5, list_1)
    print(list(ans))

    from functools import reduce
    ans = reduce(lambda x, y: x * y, list_1)
    print(ans)

### 5. 条件表达式、推导式（常用到极致）
    
    条件表达式、列表推导式、字典推导式、元组推导式

### 6. 函数的定义（感悟）（万物皆可类）

    函数名和变量名一样，使用同样的命名规则，函数和变量  也都是某个类的对象。
    在python中使用变量实际上就是调用方法，使用函数也是，函数仅仅是多了一个__call__的魔法方法，
    所以可以把函数当做变量？应该把函数和变量都当成类，python里面一切都是类。
    所以我们在函数内部定义函数？实际上就是为类添加成员类，局部变量？局部函数？
    我很难说清什么，但是一句话——万物皆可类

### 7. 可变变量与不可变变量
    
    
    深拷贝和浅拷贝的问题在python里面非常值得注意，
    对于可变类型变量，进行赋值仅仅为具体的数据起了别名，这点类似于c中指针指向同一片空间
    同样出现在函数定义中，默认参数若为可变变量，其仅会在第一次调用时创建，后续就是对其重复操作，这会使函数功能出乎意料
    这会降低我们对内存的控制力，同时降低代码的掌控力，尽可能的避免，避免方式——好的码风

### 8. .ipy文件 与 typing
    
    有一次我去看某个标准库，发现python其实和c一样是有类型提示的，一般我们省略不写，实际上是默认存在的。
    .ipy文件和.h文件一样，声明函数、给定类型提示，区别在于python中的.ipy仅供参考，而.h起到声明作用
    因为python灵活的数据结构，我们使用typing来进行类型提示，很累也比较复杂，可以看懂就可以了

### 9. PEP8 标准
    
    python应当遵循PEP8的编码规范，但是实际上我们都不遵守，毕竟不是上班，诶嘿~
    PEP8标准是帮助协作的，不仅是多人协作，也可以是单人多终端协作，
    如果有一天代码不能在两个电脑上执行一样，看看PEP8对文件开头的要求吧
    main函数（程序入口）处标记，文件编码格式标记，文件名标记，文件作用标记，引用、类定义、函数定义、具体语句、注释、
    非常有必要试一试，降低出bug的概率

### 10. 虚拟环境 与 requirements.txt
[学习链接](https://www.bilibili.com/video/BV1V7411n7CM/?spm_id_from=333.1391.0.0&p=6&vd_source=b6a01e89362733f2efeffc207b2b89f2)
    
    虚拟环境就是一个为新项目保持独立性所创建的python环境，有很多实现方式，介绍通过cmd创建和控制。  
    一般项目所需要的第三方库或者依赖，在requirements.txt列出名称和版本


    在命令行中运行下面指令
    
    python -m venv 虚拟环境名            --- 创建虚拟环境
    cd 虚拟环境名                        --- 路径跳转
    cd Scripts                          --- 路径跳转
    activate                            --- 启动虚拟环境
    pip install -r requirements.txt     --- 依赖安装、启动虚拟环境后，此时安装python中的库仅对此环境进行安装
    deactivate                          --- 退出虚拟环境

    虚拟环境没有使用限制，在pycharm等编译软件中选择即可
    
**我们不禁有一个问题，为什么要这么操作？**

    这就涉及到python调用第三方库的方式了，
    当我们代码import某个库时，若电脑上有很多同名的库或包，
    首先从当前目录下寻找包，然后是环境变量 PYTHONPATH，
    然后是标准库目录（Python安装路径下的标准库（如/usr/lib/python3.x）），
    然后是第三方库目录（site-packages（/usr/local/lib/python3.x/site-packages））
    通过sys.path查看和修改。

**注意！下面是我的回忆，目前没找到资料，可能不正确**

    一种说法是，不同的虚拟环境仅仅是，site-packages的不同，这个可以在虚拟环境中lib目录找到
    其他的.exe和标准库是通过某种链接方式和主环境联系的，这样仅需花费第三方库的内存即可
    
    一种说法是，不同的虚拟环境中的.exe和标准库是拷贝的，但是也是通过site-packages的不同来实现隔离效果
    
    两者都是通过sys.path来作用的。


### 11. collections容器库 （数据结构很常用，这里列举好用的，但是一般也不用不上这些高级功能）
    defaultdict 更加强大的字典数据结构，支持无键支持嵌套幅值
    favourite_colours = defaultdict(list)
    
    计数器Counter
    favs = Counter(name for name, colour in colours)

    双端队列deque 

    命名元组namedtuple 一个可以像字典一样利用键来搜索值的元组，拥有所有元组的性质, 自文档？

有趣的示例：任一小说，利用jieba库分词，然后用Counter计数，最后用cloud库绘制词云。早前写的博客：[词云绘制](https://blog.csdn.net/m0_73666951/article/details/134432006)

    这是全球高武这本小说分析的数据，最高频的词是主角的名字，嗯，很合理。

    分词完成，共得到 2502099 个有效词汇
    高频词汇TOP30:
    1. 方平    (72754次)
    2. 他们    (16721次)
    3. 自己    (15716次)
    4. 强者    (14635次)
    5. 现在    (14634次)
    6. 这些    (13515次)
    7. 不是    (13494次)
    8. 武者    (13137次)
    9. 知道    (12470次)
    10. 有些    (12424次)
    11. 可以    (10922次)
    12. 什么    (10810次)
    13. 就是    (10441次)
    14. 还是    (10272次)
    15. 一些    (9720次)
    16. 此刻    (9485次)
    17. 地窟    (9467次)
    18. 本源    (9111次)
    19. 我们    (9021次)
    20. 你们    (8812次)
    21. 不过    (8169次)
    22. 这么    (7818次)
    23. 一声    (7758次)
    24. 真的    (7650次)
    25. 九品    (7272次)
    26. 之前    (7178次)
    27. 天王    (7047次)
    28. 一个    (6892次)
    29. 气血    (6770次)
    30. 没有    (6747次)

### 12.迭代器 Enumerate, range, zip


### 13.自省 dir, type, id, 

    dir  函数返回一个列表，列出了一个对象所拥有的属性和方法。如果某个数据结构忘了他的用法，这个东西很好用。
    type 函数返回一个对象的类型。方便调试的时候查逻辑或者一些特殊的业务
    id() 函数返回任意不同种类对象的唯一ID。跟踪对象在内存中的位置，但是要注意生命周期。
    对于自定义类型，利用唯一标识符来进行哈希。
    同时对于上面的可变类型与不可变类型，可以通过id来辨别浅拷贝与深拷贝的问题。
    同时可以在多线程中实现锁的相关逻辑，解决并发问题。    
    inspect 函数, 给定一个类型, 返回正处在生命周期的实例


### 14.with as 与 open  


### 15.Exception报错基类
    
    处理可预见的报错可提高代码稳健性。
    使用try except else finally, 一般用前两个。

    常用：处理多种错误类型
    try: ...  except (Error1, Error2) as e: ...
    try: ...  except Error1 as e: ... except Error2 as e: ...
    except Exception: raise 

    我们捕获到的错误，实际上是类，所有报错与自定义错误都是Exception的子类

    # 输出示例：
    # 错误类型: FileNotFoundError
    # 错误信息: [Errno 2] No such file or directory: 'missing_file.txt'
    # 错误号: 2
    # 系统错误信息: No such file or directory
    # 相关文件名: missing_file.txt

    那么错误是怎么触发的呢？当然是断言和掷出啦    assert 和 raise 关键字
    当我们通过判断检测到错误即将发生时，使用这两个其中一个。
    前者用于底层开发，后者用于中高层开发，推荐使用raise。
    前者只能触发AssertionError，后者触发自定义错误类型，
    
示例（不推荐断言）：
    
    class ValidationError(Exception):
        """基础验证错误"""
        def __init__(self, message, field=None):
            self.message = message
            self.field = field
            super().__init__(f"{field}: {message}" if field else message)
    
    class RequiredFieldError(ValidationError):
        """必填字段缺失错误"""
        def __init__(self, field):
            super().__init__("This field is required", field)
    
    class InvalidTypeError(ValidationError):
        """类型错误"""
        def __init__(self, field, expected_type):
            super().__init__(f"Expected type {expected_type}", field)
            self.expected_type = expected_type

    def create_user(username, email):
        if not username:
            raise RequiredFieldError("username")
        
        if not email:
            raise RequiredFieldError("email")
        
        if "@" not in email:
            raise ValidationError("Invalid email format", "email")
        
### 16.类 的感悟
    
    类是很复杂的，基础默认会的，写几点感悟.
    在py3中，所有类都是object基类的子类，即使不写，也是隐式的继承。
    类变量与实例变量区别很大，但是关键在与可变类型与不可变类型。
    魔法方法：所有官方定义的类中有的，但是自定义类没有的，都可以使用魔法方法来扩展，左右都有两个下划线， getitem

### 17.lambada匿名函数

    data = zip(list1, list2)
    data = sorted(data)
    list1, list2 = map(lambda t: list(t), zip(*data))

### 18. 一行式


### 19. for else语句
    类似于try else, 当for循环没有因break而退出时，执行else语句内容

### 20. cpython（一般用不上）

1. 简单方式：ctypes（windows系统下）  
将c文件编译成dll动态库，在python代码中from ctypes import * 然后 adder = CDLL('./adder.dll')，就可以把c文件变成adder库了。
怎么将c文件编译成dll静态库？vs软件选择新建dll打包项目，cmake文件release，注意dll和python都是64位或32位才能兼容
2. 高级方式：cffi、cython  

这是一个很复杂的东西，一般我用不上，简单成功后就没有尝试了，下面是示例  
**我使用vs编译dll, 注意选择winX86, 严格遵守格式要求, py读取dll时选择合适的格式**

    // allmain.cpp
    #include<stdio.h>
    
    extern "C" __declspec(dllexport) int add_int(int a, int b) {
        return a + b;
    }
    
    extern "C" __declspec(dllexport) float add_float(float a, float b) {
        return a + b;
    }
    
    extern "C" __declspec(dllexport) double add_double(double a, double b) {
        return a + b;
    }

    # -*-：main.py
    import ctypes
    import os
    
    # 加载DLL
    dll_path = os.path.abspath("./Dll1.dll")
    dll = ctypes.WinDLL(dll_path)  # Windows 使用 WinDLL
    
    # 定义add_int函数原型
    dll.add_int.argtypes = [ctypes.c_int, ctypes.c_int]
    dll.add_int.restype = ctypes.c_int
    
    # 定义add_float函数原型
    dll.add_float.argtypes = [ctypes.c_float, ctypes.c_float]
    dll.add_float.restype = ctypes.c_float
    
    # 定义add_double函数原型
    dll.add_double.argtypes = [ctypes.c_double, ctypes.c_double]
    dll.add_double.restype = ctypes.c_double
    
    # 测试整数加法
    result_int = dll.add_int(5, 3)
    print(f"5 + 3 = {result_int}")
    
    # 测试浮点数加法
    result_float = dll.add_float(ctypes.c_float(2.5), ctypes.c_float(3.7))
    print(f"2.5 + 3.7 = {result_float:.2f}")
    
    # 测试双精度加法
    result_double = dll.add_double(1.23456789, 9.87654321)
    print(f"1.23456789 + 9.87654321 = {result_double:.8f}")
    
    # 输出：
    # 5 + 3 = 8
    # 2.5 + 3.7 = 6.20
    # 1.23456789 + 9.87654321 = 11.11111110

**性能测试**
    
    依次调用cpython, lambda, def定义的函数实现两数和，采用上述的装饰器测试运行时长
    add_int_c = timer(dll.add_int)(10, 10)
    add_int_lambda = timer(lambda x, y: x + y)(10, 10)
    add_int_def = timer(add_int2)(10, 10)
    
    [add_int] 执行耗时: 0.000002000 
    [<lambda>] 执行耗时: 0.000000900 
    [add_int2] 执行耗时: 0.000000500 
    发现资源花费 cpython >> lambda ~= def

