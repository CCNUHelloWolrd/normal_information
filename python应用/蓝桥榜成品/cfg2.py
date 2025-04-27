import pygame
import cfg
pygame.init()

# This file contains font, music, color, image, func which to get the true resource by number
##
# 字体
# 1为花体字
# 2为粗体字
# 3为宋体字
font_path1 = "resource/font/FZSTK.TTF"
font_path2 = "resource/font/STHUPO.TTF"
font_path3 = "resource/font/STZHONGS.TTF"
story_font_size = 20
title_font_size = 30
choose_font_size = 20
game_font_size = 50

##
# 音效
music_path1 = "resource/music/命中.mp3"
music_path2 = "resource/music/命中2.mp3"
music_path3 = "resource/music/格挡.mp3"
music_path4 = "resource/music/格挡2.mp3"
music_path5 = "resource/music/死亡.mp3"
sound1 = pygame.mixer.Sound(music_path1)
sound2 = pygame.mixer.Sound(music_path2)
sound3 = pygame.mixer.Sound(music_path3)
sound4 = pygame.mixer.Sound(music_path4)
sound5 = pygame.mixer.Sound(music_path5)

##
# 颜色
color_white = (255, 255, 255)
color_white10 = (10, 10, 10)
color_white20 = (20, 20, 20)
color_white30 = (30, 30, 30)
color_white40 = (40, 40, 40)
color_white50 = (50, 50, 50)
color_white60 = (60, 60, 60)
color_white70 = (70, 70, 70)
color_white80 = (80, 80, 80)
color_white90 = (90, 90, 90)
color_white100 = (100, 100, 100)
color_white110 = (110, 110, 110)
color_white120 = (120, 120, 120)
color_white130 = (130, 130, 130)
color_white140 = (140, 140, 140)
color_white150 = (150, 150, 150)
color_white160 = (160, 160, 160)
color_white170 = (170, 170, 170)
color_white180 = (180, 180, 180)
color_white190 = (190, 190, 190)
color_white200 = (200, 200, 200)
color_white210 = (210, 210, 210)
color_white220 = (220, 220, 220)
color_white230 = (230, 230, 230)
color_white240 = (240, 240, 240)
color_white250 = (250, 250, 250)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)
color_choose = "darkorange"
color_choose1 = "darkorange"
color_choose2 = "darkorange"
color_choose3 = "darkorange"
color_choose4 = "darkorange"
color_choose5 = "darkorange"
color_choose6 = "darkorange"
color_choose7 = "darkorange"
color_choose8 = "darkorange"
color_choose9 = "darkorange"
##
# 图片素材

# 背景图片
image_kg1 = "resource/picture/背景（结局一）.png"
image_kg2 = "resource/picture/背景（决战）.png"
image_kg3 = "resource/picture/背景（出山）.png"
image_kg4 = "resource/picture/背景（大雪）.png"
image_kg5 = "resource/picture/背景（对战）.png"
image_kg6 = "resource/picture/背景（灭门）.png"
image_kg7 = "resource/picture/背景（窃取）.png"
image_kg8 = "resource/picture/背景（结局一）.png"
image_kg9 = "resource/picture/背景（结局二）.png"
image_kg10 = "resource/picture/背景（结局三）.png"
image_kg11 = "resource/picture/背景2.jpg"
image_kg01 = "resource/picture/背景1（自由替换勿改文件名).png"
image_kg02 = "resource/picture/背景2（自由替换勿改文件名).png"
image_kg03 = "resource/picture/背景3（自由替换勿改文件名).png"
image_kg04 = "resource/picture/背景4（自由替换勿改文件名).png"
image_kg05 = "resource/picture/背景5（自由替换勿改文件名).png"
image_kg06 = "resource/picture/背景6（自由替换勿改文件名).png"
image_kg07 = "resource/picture/背景7（自由替换勿改文件名).png"
image_kg08 = "resource/picture/背景8（自由替换勿改文件名).png"
image_kg09 = "resource/picture/背景9（自由替换勿改文件名).png"
image_kg010 = "resource/picture/背景10（自由替换勿改文件名).png"

# 人物图片
image_pl1 = "resource/picture/人物（少年1）.png"
image_pl2 = "resource/picture/人物（少年出山1）.png"
image_pl3 = "resource/picture/人物（师傅1）.png"
image_pl4 = "resource/picture/人物（师兄1）.png"
image_pl5 = "resource/picture/人物（反派2）(已去底).png"
image_pl6 = "resource/picture/人物（反派3）(已去底).png"
image_pl7 = "resource/picture/人物（反派4）(已去底).png"
image_pl8 = "resource/picture/人物（反派5）(已去底).png"
image_pl9 = "resource/picture/人物（女助理）.png"
image_pl10 = "resource/picture/人物（女助理）.png"
image_pl11 = "resource/picture/人物（守卫）.png"
image_pl12 = "resource/picture/人物（景凤）.png"
image_pl13 = "resource/picture/人物（法贾）.png"
image_pl14 = "resource/picture/人物（西装男子）.png"
image_pl15 = "resource/picture/人物（黑木弟子）.png"
image_pl16 = "resource/picture/人物（黑木）.png"
image_pl17 = "resource/picture/人物（女助理）.png"
image_pl18 = "resource/picture/人物（女助理）.png"
image_pl19 = "resource/picture/人物（女助理）.png"
image_pl20 = "resource/picture/人物（女助理）.png"
image_pl01 = "resource/picture/人物1（自由替换勿改文件名).png"
image_pl02 = "resource/picture/人物2（自由替换勿改文件名).png"
image_pl03 = "resource/picture/人物3（自由替换勿改文件名).png"
image_pl04 = "resource/picture/人物4（自由替换勿改文件名).png"
image_pl05 = "resource/picture/人物5（自由替换勿改文件名).png"
image_pl06 = "resource/picture/人物6（自由替换勿改文件名).png"
image_pl07 = "resource/picture/人物7（自由替换勿改文件名).png"
image_pl08 = "resource/picture/人物8（自由替换勿改文件名).png"
image_pl09 = "resource/picture/人物9（自由替换勿改文件名).png"
image_pl010 = "resource/picture/人物10（自由替换勿改文件名).png"
# 道具图片（依次为玉佩暗、玉佩亮、线索）
image_th1 = "resource/picture/道具（暗1）.png"
image_th2 = "resource/picture/道具（亮1）.png"
image_th3 = "resource/picture/道具（线索1）.png"
# 攻击特效
image_ak1 = "resource/picture/攻击1.png"
image_ak2 = "resource/picture/攻击2.png"
image_ak3 = "resource/picture/攻击3.png"
image_ak01 = "resource/picture/攻击01.png"
image_ak02 = "resource/picture/攻击02.png"
image_ak03 = "resource/picture/攻击03.png"

##
# 剧情


# 文案：储存在"resource/font/text1.txt"等
# 剧情读取函数
def text_get(filename=""):
    if filename == "":
        return None
    file_chapter1 = open(filename, mode="r", encoding="utf-8")
    text_chapter1 = []
    text_swap = []
    for lines in file_chapter1.readlines():
        if lines[1] == "#":
            text_chapter1.append(text_swap)
            text_swap = []
        else:
            text_swap.append(lines)
    text_chapter1.append(text_swap)
    return text_chapter1


# 图片素材位置参数：储存在"resource/font/image1.txt"等
# 图片素材位置参数读取函数
def image_get(filename=""):
    if filename == "":
        return None
    file_chapter1 = open(filename, mode="r", encoding="utf-8")
    image_chapter1 = []
    image_swap = []
    for lines in file_chapter1.readlines():
        if lines[0] == "#":
            image_chapter1.append(image_swap)
            image_swap = []
        else:
            image_chapter1.append(lines)
    return image_chapter1


# 根据编号对应得到素材
# 背景图片获取
def get_bg_image(num):
    if num == 1:
        return image_kg1
    if num == 2:
        return image_kg2
    if num == 3:
        return image_kg3
    if num == 4:
        return image_kg4
    if num == 5:
        return image_kg5
    if num == 6:
        return image_kg6
    if num == 7:
        return image_kg7
    if num == 8:
        return image_kg8
    if num == 9:
        return image_kg9
    if num == 10:
        return image_kg10
    if num == 11:
        return image_kg11
    if num == 101:
        return image_kg01
    if num == 102:
        return image_kg02
    if num == 103:
        return image_kg03
    if num == 104:
        return image_kg04
    if num == 105:
        return image_kg05
    if num == 106:
        return image_kg06
    if num == 107:
        return image_kg07
    if num == 108:
        return image_kg08
    if num == 109:
        return image_kg09
    if num == 110:
        return image_kg10


# 人物图片获取
def get_pl_image(num):
    if num == 1:
        return image_pl1
    if num == 2:
        return image_pl2
    if num == 3:
        return image_pl3
    if num == 4:
        return image_pl4
    if num == 5:
        return image_pl5
    if num == 6:
        return image_pl6
    if num == 7:
        return image_pl7
    if num == 8:
        return image_pl8
    if num == 9:
        return image_pl9
    if num == 10:
        return image_pl10
    if num == 11:
        return image_pl11
    if num == 12:
        return image_pl12
    if num == 13:
        return image_pl13
    if num == 14:
        return image_pl14
    if num == 15:
        return image_pl15
    if num == 16:
        return image_pl16
    if num == 17:
        return image_pl17
    if num == 18:
        return image_pl18
    if num == 19:
        return image_pl19
    if num == 20:
        return image_pl20
    if num == 101:
        return image_pl01
    if num == 102:
        return image_pl02
    if num == 103:
        return image_pl03
    if num == 104:
        return image_pl04
    if num == 105:
        return image_pl05
    if num == 106:
        return image_pl06
    if num == 107:
        return image_pl07
    if num == 108:
        return image_pl08
    if num == 109:
        return image_pl09
    if num == 110:
        return image_pl10

##
# 游戏主要参数


game_name = "蓝桥榜"
title_name = "贺新岁"
screen_size = (800, 600)

##
# 重要元素位置参数
pos_title_button = (325, 100)
pos_return_button = (50, 50)
pos_choose1_button = (340, 300)
pos_choose2_button = (50, 50)
pos_set_button = (660, 20)
pos_start_button = (340, 300)
pos_mean_button = (340, 350)
pos_gift_button = (724, 20)
pos_out_button = (758, 20)
pos_pl = [(1000, 1000)]
for i in range(10, 60):
    pos_pl.append((i * 10, 200))

##
# 兑换码
# 兑换码信息储存
gift1_password = ["ccnu1024", "CCNU1024"]
gift2_password = ["ccnu1024", "CCNU1024"]
gift3_password = ["ccnu1024", "CCNU1024"]
gift4_password = ["ccnu1024", "CCNU1024"]
gift5_password = ["ccnu1024", "CCNU1024"]
# 兑换码状态储存
gift1_pass = False
gift2_pass = False
gift3_pass = False
gift4_pass = False
gift5_pass = False

##
# 剧情选择累计
choose_ch1 = [10]
choose_ch2 = [10]
choose_ch3 = [10]
choose_ch4 = [10]
choose_ch5 = [10]


