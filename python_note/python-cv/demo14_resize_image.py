import cv2


# 加载原始图像
img = cv2.imread("rgb.png")

# 缩放图像
# dst = cv.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
# src	numpy.ndarray	必须	原图像
# dsize	tuple<int>	必须	缩放后的图像大小
# dst	无所谓	不必须	目标图像，但是在 Python 里面没有任何意义。一般不传参或者设成 None
# fx, fy	数值类型	不必须	x 和 y 方向上的缩放比例
# interpolation	int	不必须	插值方式表示代码，本质是一个 int 数值，一般用 OpenCV 内置的参数代号以提高可读性。

# 示例1，所有方式的基础
# 备注：（400， 300）为将要放缩到的尺寸
dst = cv2.resize(img, (400, 300))

# 显示图像
cv2.imshow("dst: %d x %d" % (dst.shape[0], dst.shape[1]), dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 示例2
# 利用fx 和 fy，指定缩放后图像长宽相对于原图的比例。
# 如果利用这两个参数，dsize 要写成一个不合法的形式（比如：(0, 0)）
# # 指明形参
resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# 显示缩放后的图像
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 示例3
# 利用fx 和 fy，指定缩放后图像长宽相对于原图的比例。
# 如果利用这两个参数，dsize 要写成一个不合法的形式（比如：(0, 0)）
# # 形参缺省
resized_img = cv2.resize(img, (0, 0), None, 0.5, 0.3)

# 显示缩放后的图像
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# OpenCV 会先检查 dsize 是否合法，即图像的宽和高是否都是非 0 的。
# 如果是，就按照这个缩放，忽略后面的 fx 和 fy；如果不是，就按照 fx，fy 来计算
# 。即优先级： dsize > fx fy.
#
# 另外，两种方式是独立定义的，也就是不能混着，用数值指定长却用比率指定宽。
# 不存在 cv.resize(img, (0, 400), fx=0.42) 这种用法！
# 注意的是，缩放后的图像宽高是根据 round(img.shape[0] * fx) 和 round(img.shape[1] * fy) 来计算的，
# 所以即使 fx 和 fy 并不是0，只要这两个计算结果中有一个是 0，也会报错。

# todo：关于插值
#  7 种 方式 下面进行比较，看不出来差别
# 要缩小图片，一般来说最好的插值方法是 cv.INTER_AREA，
# 而要放大一张图片的话，一般来说效果最好的是 cv.INTER_CUBIC （速度慢）
# 或者 cv.INTER_LINEAR （速度快一些但结果仍然不错）
#
# 图像缩放用于对图像进行缩小或扩大，
# 当图像缩小时需要对输入图像重采样去掉部分像素，
# 当图像扩大时需要在输入图像中根据算法生成部分像素，
# 二者都会利用插值算法来实现

interMethod = [cv2.INTER_NEAREST,cv2.INTER_LINEAR,cv2.INTER_CUBIC,cv2.INTER_AREA,cv2.INTER_LANCZOS4,cv2.INTER_LINEAR_EXACT]
interMethodInf = ['INTER_NEAREST', 'INTER_LINEAR', 'INTER_CUBIC', 'INTER_AREA', 'INTER_LANCZOS4','INTER_LINEAR_EXACT']

for mi in zip(interMethod,interMethodInf):
    m,i = mi
    imgM = cv2.resize(img,(0, 0), fx=0.8, fy=0.8, interpolation=m)
    cv2.imshow(f"缩小插值算法{i}", imgM)

cv2.waitKey(0)
cv2.destroyAllWindows()

for mi in zip(interMethod, interMethodInf):
    m, i = mi
    imgM = cv2.resize(img, (0, 0), fx=1.8, fy=1.8, interpolation=m)
    cv2.imshow(f"放大插值算法{i}", imgM)

cv2.waitKey(0)
cv2.destroyAllWindows()


# todo: 验证
# 扩展 —— 相关函数
# OpenCV 为缩放图像的大小提供了其他的选择，这里说两个函数：cv.pyrUp 和cv.pyrDown。
#
# 这两个函数可以用于构建图像金字塔，
# pyrUp 可以将图像长宽均放大为原来的 2 倍，
# 而 pyrDown 则可以将图像长宽缩小为原来的 1/2.
# 与 resize 不同的是，这两个函数和高斯卷积核紧密相关。
# pyrUp 是对图像升采样，隔行隔列插入零向量之后用高斯核卷积，
# 而 pyrDown 则是对图像高斯卷积后隔行隔列采样。两个的卷积核成倍数关系，前者是后者的4倍



