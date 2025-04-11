"""
打开摄像头0，
并通过计算帧切换的时间间隔来计算fps（frame per second）
实时计算，我的电脑在25-45之间
"""
import cv2
import time

capture = cv2.VideoCapture(0)

if capture.isOpened() is False:
    print("Error opening the camera")

while capture.isOpened():
    ret, frame = capture.read()
    if ret is True:
        processing_start = time.time()
        cv2.imshow("Input frame from the camera", frame)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale input camera', gray_frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        processing_end = time.time()
        processing_time_frame = processing_end - processing_start
        print("FPS: {}".format(1.0 / processing_time_frame))
    else:
        break

capture.release()
cv2.destroyAllWindows()
