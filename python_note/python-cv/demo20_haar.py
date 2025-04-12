import cv2
import argparse

# 命令行参数
parser = argparse.ArgumentParser()
parser.add_argument("index_camera", help="index of the camera to read from", type=int)
parser.add_argument("output_video_path", help="path to the video file to write")
args = parser.parse_args()

# 配置模型文件
MODEL_PATHS = {
    "face": "haarcascade_frontalface_default.xml",
    "eyes": "haarcascade_eye.xml",
    "smile": "haarcascade_smile.xml"
}

# 加载所有分类器
face_cascade = cv2.CascadeClassifier(MODEL_PATHS["face"])
eye_cascade = cv2.CascadeClassifier(MODEL_PATHS["eyes"])
smile_cascade = cv2.CascadeClassifier(MODEL_PATHS["smile"])

# 打开摄像头
capture = cv2.VideoCapture(args.index_camera)

# 设定保存文件格式
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# 打印属性值
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))
print("CAP_PROP_FPS : '{}'".format(fps))

# 视频保存
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_color = cv2.VideoWriter(args.output_video_path, fourcc, int(fps), (int(frame_width), int(frame_height)), True)
while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        # 图像处理
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 人脸检测
        faces = face_cascade.detectMultiScale(
            gray_frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50, 50)  # 提高最小尺寸减少误检
        )

        # 遍历每个检测到的人脸
        for (x, y, w, h) in faces:
            # 绘制人脸矩形（蓝色）
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # 定义人脸ROI区域
            roi_gray = gray_frame[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # 眼睛检测（在人脸上半部分）
            eyes = eye_cascade.detectMultiScale(
                roi_gray[0:int(h / 2), 0:w],  # 限制在上半脸
                scaleFactor=1.05,  # 更精细的缩放
                minNeighbors=8,
                minSize=(20, 20)
            )
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            # 微笑检测（在下半脸）
            smiles = smile_cascade.detectMultiScale(
                roi_gray[int(h / 2):h, 0:w],
                scaleFactor=1.2,
                minNeighbors=25,  # 较高阈值减少误检
                minSize=(40, 20)
            )
            for (sx, sy, sw, sh) in smiles:
                # 坐标需要偏移到下半脸区域
                cv2.rectangle(roi_color,
                              (sx, sy + int(h / 2)),
                              (sx + sw, sy + int(h / 2) + sh),
                              (0, 0, 255), 2)
        # 写入一帧
        out_color.write(frame)
        # 展示
        cv2.imshow('color', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
out_color.release()
cv2.destroyAllWindows()