# -*- coding: utf-8 -*-
# demo1.py

# 最简单的装饰器


def decorator(func):
    def wrapper():
        func()
        print("函数已被装饰")
    return wrapper


@decorator
def fun_1():
    print("我是func1")


@decorator
def fun_2():
    print("我是func2")


fun_1()
fun_2()

# 输出结果：
#
# 我是func1
# 函数已被装饰
# 我是func2
# 函数已被装饰