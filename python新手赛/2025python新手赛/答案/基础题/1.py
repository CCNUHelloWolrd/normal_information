import matplotlib.pyplot as plt  # 可用turtle等替代
import numpy as np  # 可用math替代

def func(x):
    return np.sin(x) - np.log(x)

x = np.arange(0.01 ,10.01, 0.01)
y = func(x)

plt.scatter(x, y)
plt.show()



a = 2
b = 3
mid = (a + b) / 2

while  (b - a)>= 1e-4 :

    if func(a) * func(mid) < 0:
        b  = mid
    else:
        a  = mid
    mid = (a + b) / 2

print("%.4f" % mid)