import cv2
import numpy as np

# 加载原始图像
img = cv2.imread("rgb.png")

# OpenCV 提供了 getRotationMatrix2D() 函数来计算旋转矩阵，
# 并使用 warpAffine() 函数来执行图像的旋转操作
#
# getRotationMatrix2D函数 主要用于获得图像绕着 某一点的旋转矩阵
# getRotationMatrix2D(Point2f center, double angle, double scale)
# Point2f center：表示旋转的中心点
# double angle：表示旋转的角度（逆时针）
# double scale：图像缩放因子
#
# 得到旋转矩阵,2行3列，前两列为旋转角度、第三列为图片平移距离

# 仿射变换，包括平移(transform)、旋转(rotate)、缩放(scale)、剪切(shear)
# 是一种二维坐标到二维坐标之间的线性变换
# img_out = cv.warpAffine(img, mat, size)
#
# img_out -- 输出图像
# img -- 原始图像
# mat -- 2×3的变换矩阵
# size -- 变换后图像尺寸
#
# 本质上是另外两种简单变换的叠加：一个是线性变换，一个是平移变换。
# 该变换能保证图像的平直性和平行性，原来的直线仿射变换后还是直线，
# 原来的平行线经过仿射变换之后还是平行线。
# 进行哪种形式的仿射变换完全取决于变换矩阵mat。
# #           平移变换
# # mat = [[1,0,dx],
# #        [0,1,dy]]
# #           旋转变换
# # mat = cv2.getRotationMatrix2D(center, angle, scale)
# #           仿射变换
# # 变换矩阵mat可通过cv.getAffineTransfrom(points1, points2)函数获得
# # 变换矩阵的获取需要至少三组变换前后对应的点坐标，设取原图上的三个点组成矩阵points1，变换后的三个点组成的矩阵points2
# # mat = cv.getAffineTransform(points1, points2)

##
# 一、普通旋转
height, width = img.shape[:2]

# 计算旋转矩阵
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)

# 旋转图像
rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

# 显示旋转后的图像
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##
# 二、旋转后完全显示
# 虽然已经能够绕任意点旋转，但是图片并不能显示完全，
# 所以还可以使用如下代码进行自适应调整图片大小。
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 145, 1)

# 自适应图片边框大小,实际上就是简单的几何运算
cos = np.abs(M[0, 0])
sin = np.abs(M[0, 1])
new_w = rows * sin + cols * cos
new_h = rows * cos + cols * sin
M[0, 2] += (new_w - cols) * 0.5
M[1, 2] += (new_h - rows) * 0.5
w = int(np.round(new_w))
h = int(np.round(new_h))
res2 = cv2.warpAffine(img, M, (w, h))

# 显示旋转后的图像
cv2.imshow('Dynamic Rotated Image', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
##
# 平移图片
height, width = img.shape[:2]

dx = 50
dy = 100
mat_shift = np.float32([[1, 0, dx],
                        [0, 1, dy]])

res2 = cv2.warpAffine(img, mat_shift, (width, height))

cv2.imshow('Shift Image', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
##
# 一般仿射变换
height, width = img.shape[:2]
points1 = np.float32([[30, 30], [100, 40], [40, 100]])
points2 = np.float32([[60, 60], [200, 80], [80, 200]])
mat_affine = cv2.getAffineTransform(points1, points2)
image_affine = cv2.warpAffine(img, mat_affine, (width, height))
cv2.imshow("image_affine", image_affine)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()

##
# 透视变换
# 透视变换（Perspective Transformation） 也叫视角转换，
# 是将图片投影到一个新的视平面，也称作投影映射。
# 顾名思义，将图片从一个视角转换到另一个视角
# 该变换能保证图像的平直性，不保证平行性，透视变换可保持直线不变形，但是平行线可能不再平行。
#
# img_out = cv.warpPerspective(img, mat, size)
#
# img_out -- 输出图像
# img -- 原始图像
# mat -- 3×3的变换矩阵
# size -- 变换后图像尺寸
#
# 变换矩阵mat可通过cv.getPerspectiveTransform()函数获得，
# 原理和cv.getAffineTransform()相同
# 透视变换至少需要四组变换前后对应的点坐标
# 设取原图上的四个点组成矩阵points1，变换后的四个点组成的矩阵points2

height, width = img.shape[:2]

points1 = np.float32([[30, 30], [10, 40], [40, 10], [5, 15]])
points2 = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])

mat_perspective = cv2.getPerspectiveTransform(points1, points2)
image_perspective = cv2.warpPerspective(img, mat_perspective, (width, height))

cv2.imshow("image_perspective", image_perspective)
cv2.waitKey(delay=0)
cv2.destroyAllWindows()

# 总结：
# 仿射变换可以将矩形图片映射为平行四边形，
# 透视变换可以将矩形图片映射为任意四边形。
#
# 仿射变换是透视变换的一种特殊形式，它是把二维转到三维，变换后在映射回之前的二维空间，而不是另一个二维空间。
# 仿射变换至少需要三个对应的点坐标，透视变换至少需要四个。
#
# 补充：数学原理
