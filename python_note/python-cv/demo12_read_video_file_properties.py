import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video_path", help='path to the video fiel')
args = parser.parse_args()

# 打开视频
capture = cv2.VideoCapture(args.video_path)

if capture.isOpened() is False:
    print("Error opening vieo stream or file")

# 读取视频总帧数，实现倒放
frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1
print("Starting in frame: '{}'".format(frame_index))

while capture.isOpened() and frame_index >= 0:
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = capture.read()

    if ret:
        cv2.imshow('Original frame', frame)
        # 切换帧数
        frame_index = frame_index - 1
        # print("next index to read: '{}'".format(frame_index))

        # Press q on keyboard to exit the program:
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

capture.release()
cv2.destroyAllWindows()


# todo：在此查看视频信息

# 辅助函数，查看视频视频编码格式
def decode_fourcc(fourcc):
    """
    传入一个int对象，
    因为int为32位2进制，故而每八位可以转化为一个256进制数，
    可以转换对应成ASCII字符
    :param fourcc:
    :return:
    """
    fourcc_int = int(fourcc)

    # # 查看信息
    # print("int value of fourcc: '{}'".format(fourcc_int))

    fourcc_decode = ""
    for i in range(4):
        int_value = fourcc_int >> 8 * i & 0xFF
        # print("int_value: '{}',acsii: {}".format(int_value, chr(int_value)))
        fourcc_decode += chr(int_value)

    return fourcc_decode

# print(decode_fourcc(828_601_953))

print("CV_CAP_PROP_FRAME_WIDTH:'{}'".format(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("CV_CAP_PROP_FRAME_HEIGHT :'{}'".format(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("CAP_PROP_FPS : '{}'".format(capture.get(cv2.CAP_PROP_FPS)))
print("CAP_PROP_POS_MSEC :'{}'".format(capture.get(cv2.CAP_PROP_POS_MSEC)))
print("CAP_PROP_POS_FRAMES :'{}'".format(capture.get(cv2.CAP_PROP_POS_FRAMES)))
print("CAP_PROP_FOURCC :'{}'".format(decode_fourcc(capture.get(cv2.CAP_PROP_FOURCC))))
print("CAP_PROP_FRAME_COUNT :'{}'".format(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
print("CAP_PROP_MODE : '{}'".format(capture.get(cv2.CAP_PROP_MODE)))
print("CAP_PROP_BRIGHTNESS :'{}'".format(capture.get(cv2.CAP_PROP_BRIGHTNESS)))
print("CAP_PROP_CONTRAST :'{}'".format(capture.get(cv2.CAP_PROP_CONTRAST)))
print("CAP_PROP_SATURATION :'{}'".format(capture.get(cv2.CAP_PROP_SATURATION)))
print("CAP_PROP_HUE : '{}'".format(capture.get(cv2.CAP_PROP_HUE)))
print("CAP_PROP_GAIN : '{}'".format(capture.get(cv2.CAP_PROP_GAIN)))
print("CAP_PROP_EXPOSURE :'{}'".format(capture.get(cv2.CAP_PROP_EXPOSURE)))
print("CAP_PROP_CONVERT_RGB :'{}'".format(capture.get(cv2.CAP_PROP_CONVERT_RGB)))
print("CAP_PROP_RECTIFICATION :'{}'".format(capture.get(cv2.CAP_PROP_RECTIFICATION)))
print("CAP_PROP_ISO_SPEED :'{}'".format(capture.get(cv2.CAP_PROP_ISO_SPEED)))
print("CAP_PROP_BUFFERSIZE :'{}'".format(capture.get(cv2.CAP_PROP_BUFFERSIZE)))
