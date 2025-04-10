import cv2
from matplotlib import pyplot as plt
import numpy as np

# # 以bgr顺序加载图像
# img_OpenCV = cv2.imread('rgb.png')
# # 将图像氛围三个通道（b, g, r）
# b, g, r = cv2.split(img_OpenCV)
# print(b, g, r)
# # 合并通道，采取r, g, b
# img_matplotlib = cv2.merge([r, g, b])
# # 分别绘制并进行比较
# cv2.imshow("b, g, r", img_OpenCV)
# cv2.imshow("r, g, b", img_matplotlib)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # 利用matplotlib库绘制，绘制子图进行比较
# plt.subplot(121)
# plt.imshow(img_OpenCV)
# plt.subplot(122)
# plt.imshow(img_matplotlib)
# plt.show()

# 结论：opencv和matplotlib的通道顺序不同，且通过改变颜色通道，三原色发生变化

# cv中拼接图像
# np.concatenate 在axis上进行堆叠
# # 水平堆叠
# img_concats = np.concatenate((img_OpenCV, img_matplotlib), axis=1)
# cv2.imshow('bgr image and rgb image', img_concats)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # 竖直堆叠
# img_concats = np.concatenate((img_OpenCV, img_matplotlib), axis=0)
# cv2.imshow('bgr image and rgb image', img_concats)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # 修改通道的技巧
# B = img_OpenCV[:, :, 0]
# G = img_OpenCV[:, :, 1]
# R = img_OpenCV[:, :, 2]
# # 技巧
# img_matplotlib = img_OpenCV[:, :, ::-1]
# img_concats = np.concatenate((img_OpenCV, img_matplotlib), axis=1)
# cv2.imshow('bgr image and rgb image', img_concats)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 技巧：numpy,matplotlib辅助操作

# 彩色图像访问和操作像素
img = cv2.imread("rgb.png")
# # 展示并等待
# cv2.imshow("original image", img)
# cv2.waitKey(0)
# 打印图像的形状
print(img.shape)  # 输出是 (height, width, channels)（高，宽，通道）
# 打印图像的大小（元素的总数）
print(img.size)  # 输出是 height * width * channels
# 打印图像的数据类型
print(img.dtype)  # 输出是 uint8
# 读取某一个像素
(b, g, r) = img[6, 40]
print((b, g, r))
# 读取某一个像素的某一个通道的数值
b = img[6, 40, 0]
print(b)
# 同样的方式对某一个像素进行修改
img[6, 40] = (0, 0, 255)
# 对图片进行切片，可以看做是另一个图片
top_left_corner = img[0:50, 0:50]
cv2.imshow("original image", top_left_corner)
cv2.waitKey(0)

# 灰色图像访问
gray_img = cv2.imread("rgb.png", cv2.IMREAD_GRAYSCALE)
dimensions = gray_img.shape
total_number_of_elements = gray_img.size
image_dtype = gray_img.dtype
print(dimensions, total_number_of_elements, image_dtype)

# 结论：不同通道模式尺寸相同，单数诗句不同，本质上就是一个二维数组