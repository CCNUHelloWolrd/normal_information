import cv2

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("index_camera", help="index of the camera to read from", type=int)
args = parser.parse_args()

capture = cv2.VideoCapture(args.index_camera)

# 获取 VideoCapture 的属性 (frame width, frame height and frames per second (fps)):
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# 打印属性值
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))
print("CAP_PROP_FPS : '{}'".format(fps))

# 用于保存图像是构建文件名
frame_index = 0

if capture.isOpened() is False:
    print("Error opening the camera")

while capture.isOpened():
    ret, frame = capture.read()

    if ret is True:
        cv2.imshow('Input frame from the camera', frame)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 保存相机画面
        # 同demo6，在此检测是否按下按键c
        if cv2.waitKey(20) & 0xFF == ord('c'):
            frame_name = "camera_frame_{}.png".format(frame_index)
            gray_frame_name = "grayscale_camera_frame_{}.png".format(frame_index)
            # 将当前帧保存到磁盘(同时保存 BGR 和灰度帧)
            cv2.imwrite(frame_name, frame)
            cv2.imwrite(gray_frame_name, gray_frame)
            frame_index += 1
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()

