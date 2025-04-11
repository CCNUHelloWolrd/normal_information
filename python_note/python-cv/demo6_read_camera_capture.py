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

# Check if camera opened successfully
if capture.isOpened() is False:
    print("Error opening the camera")

while capture.isOpened():
    ret, frame = capture.read()

    if ret is True:
        cv2.imshow('Input frame from the camera', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()





