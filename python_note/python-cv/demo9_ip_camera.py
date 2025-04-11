# 获取IP摄像头的URL
# 每个IP摄像头都有一个特定的URL用来访问其视频流。
# 这个URL通常遵循以下格式：
#
# RTSP(Real Time Streaming Protocol): rtsp: // < ip_address > / path
# HTTP: http: // < ip_address > / path
# <ip_address> 是您的IP摄像头的IP地址，而 /path 则是访问视频流的具体路径。
#
# 如果您的摄像头需要身份验证，那么URL格式可能会有所不同，例如：
#
# 带认证的RTSP: rtsp://username:password@ip_address/path
# 带认证的HTTP: http://username:password@ip_address/path

# todo:在这个网址里查看公共ip摄像头请求 https://wxyzwebcams.com/zhcn/

import cv2

# 指定IP摄像头的URL
# todo: 仅需配置这行代码
url = 'rtsp://admin:123456@192.168.1.216/H264?ch=1&subtype=0'

# 创建一个VideoCapture对象，参数是视频源，这里是我们指定的IP摄像头URL
cap = cv2.VideoCapture(url)

# 检查是否成功打开视频流
if not cap.isOpened():
    print("Error: Could not open video stream.")
else:
    print("Video stream opened successfully.")

# 开始循环读取视频帧
while True:
    # 读取一帧视频
    ret, frame = cap.read()

    # 如果读取成功（ret为True），则显示这一帧
    if ret:
        # 显示视频帧
        cv2.imshow('Capturing', frame)

        # 检测按键，如果按下'q'键则退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # 如果读取失败，打印错误信息并尝试重新连接
        print("Error: Failed to read frame from video stream.")
        # 可选：尝试重新连接
        cap.release()
        cap = cv2.VideoCapture(url)

# 清理资源
cap.release()
cv2.destroyAllWindows()


