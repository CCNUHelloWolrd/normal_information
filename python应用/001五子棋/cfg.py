import os

# 大小
SCREEN_size=(640,640)

# 资源路径
'''字体路径'''
FONT_PATH = os.path.join(os.getcwd(), r'resources\font\STKAITI.TTF')
FONT_SIZE = 30
'''BGM路径'''
BGM_PATH = os.path.join(os.getcwd(), 'resources/music/bgm.mp3')
'''颜色代码路径'''
COLOR_PATH = os.path.join(os.getcwd(), r'resources\images\颜色代码.txt')

# 颜色
BLACK_COLOR = "black"
WHITE_COLOR = "white"
BOARD_COLOR = [238,154,73]
# 读取文档中的颜色代码
SCREEN_COLOR = {}
f1 = open(COLOR_PATH,mode = "r",encoding="UTF-8")
i=0
for line in f1.readlines():
    SCREEN_COLOR.update({i:line})
    i+=1
