import cv2
import argparse

parser = argparse.ArgumentParser()
# cv2.VideoCapture(args.index_camera) 中index_camera为相机的索引，通常为0,1，..
parser.add_argument("index_camera", help="index of the camera to read from", type=int)
args = parser.parse_args()

# 创建对象 capture
capture = cv2.VideoCapture(args.index_camera)
# 检测是否连接成功
if capture.isOpened()is False:
    print("Error opening the camera")
while capture.isOpened():
    # 返回一个图像帧，并返回一个bool值表示是否正确捕捉图像
    ret, frame = capture.read()

    if ret is True:
        # 对于捕获到的frame，可以当做一个正常的图像进行处理
        cv2.imshow('Input frame from the camera', frame)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale input camera', gray_frame)
        # 仅获取cv2.waitKey()后八位，并且判断是否为按键q返回的ASC码
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break
# 释放所有资源
capture.release()
cv2.destroyAllWindows()

