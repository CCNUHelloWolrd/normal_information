# -*- coding: utf-8 -*-
# demo5.py

# 装饰器的使用


def repeat(num_times, a = 123):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper

    print(f"a={a}")
    return decorator_repeat


@repeat(num_times=3)
def greet_1(name):
    print(f"Hello, {name}!")


def greet_2(name):
    print(f"Hello, {name}!")


greet_1("Alice")
repeat(3)(greet_2)("Alice")
