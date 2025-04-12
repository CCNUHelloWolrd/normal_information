import cv2
import numpy as np

# 加载原始图像
img = cv2.imread("rgb.png")

# todo：原理较为复杂
# cv2.GaussianBlur（ SRC，ksize，sigmaX [，DST [，sigmaY [，borderType ] ] ] ） →DST
#
# src –输入图像；图像可以具有任何数量的信道，其独立地处理的，但深度应CV_8U，CV_16U，CV_16S，CV_32F或CV_64F。
# dst –输出与图像大小和类型相同的图像src。
# ksize –高斯核大小。 ksize.width 并且 ksize.height 可以有所不同，但它们都必须是正数和奇数。或者，它们可以为零，然后从计算 sigma*。
# sigmaX – X方向上的高斯核标准偏差。
# sigmaY – Y方向上的高斯核标准差；如果 sigmaY 为零，则将其设置为等于 sigmaX；如果两个西格玛均为零，则分别根据ksize.width 和 进行计算 ksize.height（getGaussianKernel()有关详细信息，请参见 link)；完全控制的结果，无论这一切的语义未来可能的修改，建议指定所有的ksize，sigmaX和sigmaY。
# borderType –像素外推方法。


