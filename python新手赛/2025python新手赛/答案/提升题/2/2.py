import random
import math

# 统一采样点数
sample = 1000000

# 1. 蒙特卡洛方法计算圆周率
inside_circle = 0
for i in range(sample):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside_circle += 1
pi_approx = 4 * (inside_circle / sample)
print("圆周率近似值：%.4f" % pi_approx)
print("实际圆周率值：%.4f\n" % math.pi)

# 2. 蒙特卡洛方法计算曲线围成的面积
under_curve = 0
for i in range(sample):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if x == 0:
        curve_value = 1.0
    else:
        curve_value = math.sin(x) / x
    if y <= curve_value:
        under_curve += 1
area = under_curve / sample
print("曲线y=sinx/x与指定区域围成的面积近似值：%.4f" % area)