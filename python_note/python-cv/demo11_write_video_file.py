"""
将摄像头0 捕获到的信息储存成视频文件
仅需给出视频保存路径，自动调用摄像头0
"""
import cv2
import argparse

# 命令行参数
parser = argparse.ArgumentParser()
parser.add_argument("output_video_path", help="path to the video file to write")
args = parser.parse_args()

# 打开摄像头
capture = cv2.VideoCapture(0)

# 设定保存文件格式
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# 算法糖* 解码成列表传递
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out_gray = cv2.VideoWriter(args.output_video_path, fourcc, int(fps), (int(frame_width), int(frame_height)), False)

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 写入一帧
        out_gray.write(gray_frame)

        cv2.imshow('gray', gray_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
out_gray.release()
cv2.destroyAllWindows()
