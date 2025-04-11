import cv2
import argparse


def decode_fourcc(fourcc):
    fourcc_int = int(fourcc)
    print("int value of fourcc: '{}'".format(fourcc_int))
    fourcc_decode = ""
    for i in range(4):
        int_value = fourcc_int >> 8 * i & 0xFF
        print("int_value: '{}'".format(int_value))
        fourcc_decode += chr(int_value)
    return fourcc_decode


parser = argparse.ArgumentParser()
# 添加 'video_path' 参数用于输入视频文件名
parser.add_argument("video_path", help="path to the video file")
# 添加 'output_video_path' 参数用于输出视频文件名
parser.add_argument("output_video_path", help="path to the video file to write")
args = parser.parse_args()

capture = cv2.VideoCapture(args.video_path)

# 获取 VideoCapture 属性
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
codec = decode_fourcc(capture.get(cv2.CAP_PROP_FOURCC))

print("codec: '{}'".format(codec))

fourcc = cv2.VideoWriter_fourcc(*codec)

# 创建 VideoWriter 对象，使用与输入视频文件相同的属性
out = cv2.VideoWriter(args.output_video_path, fourcc, int(fps), (int(frame_width), int(frame_height)), True)

# Check if camera opened successfully
if capture.isOpened() is False:
    print("Error opening video stream or file")
frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1

while capture.isOpened() and frame_index >= 0:
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = capture.read()

    if ret is True:
        # 显示处理结果帧
        cv2.imshow('Original frame', frame)
        # 将处理结果帧写入视频
        out.write(frame)
        frame_index = frame_index - 1
        # Press q on keyboard to exit the program:
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

# Release everything:
capture.release()
out.release()
cv2.destroyAllWindows()
