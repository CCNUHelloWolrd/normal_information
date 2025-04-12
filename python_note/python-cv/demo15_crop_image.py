import cv2


# 加载原始图像
img = cv2.imread("rgb.png")


# 裁剪图像
# 一、中心部分
height, width = img.shape[:2]
cropped_img = img[height//4:height*3//4, width//4:width*3//4]

# 显示裁剪后的图像
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 二、 间隔取样
cropped_img = img[::2, ::2]

# 显示裁剪后的图像
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 备注：实际上就是对二维数组进行操作，不过是操作尺寸罢了


