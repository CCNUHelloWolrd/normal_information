# -*- coding: utf-8 -*-
# demo4.py

# 装饰器应用示例：编写函数日志


##
# 成功示例
from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def func(x):
    pass


print("示例一")
result = func(4)
print(func.__name__)

# 输出：
# 示例一
# func was called
# func

##
# 失败示例


def logit(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return wrapper


@logit
def func(x):
    pass


print("示例二")
result = func(4)
print(func.__name__)

# 输出：
# 示例二
# func was called
# wrapper
