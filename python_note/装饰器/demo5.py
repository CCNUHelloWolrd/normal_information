# -*- coding: utf-8 -*-
# demo5.py

# 装饰器的原理


def decorator_1(func):
    def wrapper(*arg, **kwarg):
        print("decorator_1 running")
        result = func(*arg, **kwarg)
        return result
    return wrapper


def decorator_2(func):
    def wrapper(*arg, **kwarg):
        print("decorator_2 running")
        result = func(*arg, **kwarg)
        return result
    return wrapper

def decorator_3(func):
    def wrapper(*arg, **kwarg):
        print("decorator_3 running")
        result = func(*arg, **kwarg)
        return result
    return wrapper


@decorator_1
@decorator_2
@decorator_3
def fun_1(x):
    return x ** 2


@decorator_2
@decorator_1
@decorator_1
def fun_2(x):
    return x ** 2


def fun_3(x):
    return x ** 2


print(fun_1(2))
print(fun_2(2))
print(fun_3(2))
print(fun_3(fun_3(fun_3(2))))
print(decorator_1(decorator_1(decorator_1(fun_3)))(2))

# 输出：
# decorator_1 running
# decorator_2 running
# decorator_3 running
# 4
# decorator_2 running
# decorator_1 running
# decorator_1 running
# 4
# 4
# 256
# decorator_1 running
# decorator_1 running
# decorator_1 running
# 4
