import cv2
import numpy as np

# 加载原始图像
img = cv2.imread("rgb.png")



# cv2.cvtColor(input_image, flag)
# input_image	需要转换的图片
# flag	转换的类型
# 返回：颜色空间转换后的图片矩阵
#
# 全部信息查看：https://i-blog.csdnimg.cn/blog_migrate/811b26226e8222026d04b999da011f36.jpeg
#
# cv2.COLOR_BGR2GRAY	BGR -> Gray
# cv2.COLOR_BGR2RGB	BGR -> RGB
# cv2.COLOR_BGR2HSV	BGR -> HSV


# 将图像转换为灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 显示灰度图像
cv2.imshow('Grayscale Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 将图像转换为RBG图像
rbg_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 显示RBG图像
cv2.imshow('RBG Image', rbg_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
