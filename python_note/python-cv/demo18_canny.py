import cv2
import numpy as np

# 加载原始图像
img = cv2.imread("rgb.png")

# Canny 边缘检测是一种使用多级边缘检测算法检测边缘的方法。
# Canny 边缘检测分为如下几个步骤：
# 步骤 1：去噪。噪声会影响边缘检测的准确性，因此首先要将噪声过滤掉。
# 步骤 2：计算梯度的幅度与方向。
# 步骤 3：非极大值抑制，即适当地让边缘“变瘦”。
# 步骤 4：确定边缘。使用双阈值算法确定最终的边缘信息。
#
# edges = cv.Canny( image, threshold1, threshold2[, apertureSize[, L2gradient]])
# edges 为计算得到的边缘图像。
#  image 为 8 位输入图像。
#  threshold1 表示处理过程中的第一个阈值。
#  threshold2 表示处理过程中的第二个阈值。
#  apertureSize 表示 Sobel 算子的孔径大小。
#  L2gradient 为计算图像梯度幅度（gradient magnitude）的标识。
#   其默认值为 False。如果为 True，则使用更精确的 L2 范数进行计算（即两个方向的导数的平方和再开方），
#   否则使用 L1 范数（直接将两个方向导数的绝对值相加）。

o=gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
r1=cv2.Canny(o,128,200)
r2=cv2.Canny(o,32,128)
cv2.imshow("original",o)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()

# 当函数 cv2.Canny()的参数 threshold1 和 threshold2 的值较小时，能够捕获更多的边缘信息。

