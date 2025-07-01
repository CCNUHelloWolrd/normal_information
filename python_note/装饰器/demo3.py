# -*- coding: utf-8 -*-
# demo3.py

# 装饰器的原理


def decorator(func):
    def wrapper():
        func()
        print("函数已被装饰")
    return wrapper


@decorator
def fun_1():
    print("我是func1")


def fun_2():
    print("我是func2")


# 调用一个被装饰的函数
fun_1()
fun_2()
# 利用装饰器装饰函数，然后运行
fun_2 = decorator(fun_2)
fun_2()

# 输出：
#
# 我是func1
# 函数已被装饰
# 我是func2
# 我是func2
# 函数已被装饰