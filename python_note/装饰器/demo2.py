# -*- coding: utf-8 -*-
# demo2.py

# 装饰器应用示例：测量函数运行时长
# 被测量函数，使用递归算法和dp算法的爬楼梯
# 初始在第0层，每次可以走1或2步，请问到第n层有几种走法


def timer(func):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()    # 开始时间（时间戳）

        result = func(*args, **kwargs)      # 执行目标函数

        end_time = time.perf_counter()      # 结束时间（时间戳）
        elapsed = end_time - start_time     # 计算时间差
        print(f"[{func.__name__}] 执行耗时: {elapsed:.9f} ")
        return result
    return wrapper


@timer
def recursion_fun(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return recursion_fun(n - 1) + recursion_fun(n - 2)


@timer
def dp_fun(n):
    dp = [0, 1]
    for _ in range(2, n + 1):
        dp.append(dp[_ - 1] + dp[_ - 2])
    return dp[n]


print(recursion_fun(10))
print(dp_fun(10))

# 结果：
#
# [recursion_fun] 执行耗时: 0.003266600
# 55
# [dp_fun] 执行耗时: 0.000003200
# 55
#
# 不出意外
