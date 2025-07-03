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

### 5. 条件表达式、推导式
    
    常用到显而易见，不常用的将被淘汰

### 6. 函数的定义（感悟）


