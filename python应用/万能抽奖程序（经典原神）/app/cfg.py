import pygame
from moviepy.editor import *
import sys
import os
import random


class Image(object):
    """图像类：一个可以方便贴图的类"""

    def __init__(self, path=""):
        self.path = path
        # self.img = pygame.image.load(self.path).convert_alpha()
        self.img = pygame.image.load(self.path)
        self.rect = self.img.get_rect()

    def show(self, pos, screen, mode=0):
        if mode == 0:
            self.rect.topleft = pos
        elif mode == 1:
            self.rect.midtop = pos
        elif mode == 2:
            self.rect.topright = pos
        elif mode == 3:
            self.rect.midleft = pos
        elif mode == 4:
            self.rect.center = pos
        elif mode == 5:
            self.rect.midright = pos
        elif mode == 6:
            self.rect.bottomleft = pos
        elif mode == 7:
            self.rect.midbottom = pos
        elif mode == 8:
            self.rect.bottomright = pos
        screen.blit(self.img, self.rect)

    def setting(self, path=""):
        self.path = path
        self.img = pygame.image.load(self.path).convert_alpha()
        self.rect = self.img.get_rect()

    def get_path(self):
        return self.path


class Write(object):
    """文字类: 用于直接绘制少量文字"""
    font_all = "C:/Windows/Fonts/STXINWEI.TTF"
    size_all = 20
    color_all = (0, 0, 0)

    def __init__(self, text_in="", color=color_all, font=font_all, size=size_all):
        # 传入 文本、文本颜色[、文体路径、文体大小]
        self.size = size
        self.font = font
        self.text = text_in
        self.color = color
        # todo:优化
        self.x = 0

    def show(self, pos, screen, mode=0):

        font = pygame.font.Font(self.font, self.size)
        now_text = font.render(self.text, True, self.color)
        text_rect = now_text.get_rect()
        self.x = text_rect[2]
        if mode == 0:
            text_rect.topleft = pos
        elif mode == 1:
            text_rect.midtop = pos
        elif mode == 2:
            text_rect.topright = pos
        elif mode == 3:
            text_rect.midleft = pos
        elif mode == 4:
            text_rect.center = pos
        elif mode == 5:
            text_rect.midright = pos
        elif mode == 6:
            text_rect.bottomleft = pos
        elif mode == 7:
            text_rect.midbottom = pos
        elif mode == 8:
            text_rect.bottomright = pos
        screen.blit(now_text, text_rect)

    def setting(self, text_in="", color=color_all, font=font_all, size=size_all):
        self.size = size
        self.font = font
        self.text = text_in
        self.color = color

    def get_text(self):
        return self.text

    def set_text(self, text_in=""):
        self.text = text_in

    def get_color(self):
        return self.color

    def set_color(self, color=color_all):
        self.color = color

    def get_font(self):
        return self.font

    def set_font(self, font=font_all):
        self.font = font

    def get_size(self):
        return self.size

    def set_size(self, size=size_all):
        self.size = size

    def get_y(self):
        return self.x


class Paragraph(object):
    """用于解决大量文字的段落显示问题"""
    font_all = "C:/Windows/Fonts/STXINWEI.TTF"
    size_all = 20
    color_all = (0, 0, 0)
    length_all = 20

    def __init__(self, text_in="", color=color_all, font=font_all, size=size_all):
        """初始化文字内容与打印参数与滚屏参数"""
        self.size = size
        self.font = font
        self.text = text_in
        self.color = color
        self.text_all = self.text
        self.text_show_len = 0
        self.text_adjust = []

    def _adjust(self, length=length_all):
        """解决多行显示与换行问题"""
        text_len = len(self.text)
        text_adjust = []
        text_len_key = 0
        text_key = ""
        for i in range(text_len):
            if self.text[i] == "\n":
                text_key += self.text[i]
                text_adjust.append(text_key)
                text_len_key = 0
                text_key = ""
                continue
            text_key += self.text[i]
            text_len_key += 1
            if text_len_key >= length:
                text_adjust.append(text_key)
                text_key = ""
                text_len_key = 0
        if text_len_key != 0:
            text_adjust.append(text_key)
        self.text_adjust = [Write(text_, self.color, self.font, self.size) for text_ in text_adjust]

    def show(self, pos, screen):
        """默认打印或者再次打印"""
        if len(self.text_adjust) == 0:
            self._adjust()
        for i in range(len(self.text_adjust)):
            self.text_adjust[i].show((pos[0], pos[1] + i * self.size), screen)

    def show_len(self, pos, screen, length=length_all):
        """进行打印宽度调整的打印"""
        self._adjust(length)
        for i in range(len(self.text_adjust)):
            self.text_adjust[i].show((pos[0], pos[1] + i * self.size), screen)

    def show_slow(self, pos, screen, show_length=1, length=length_all):
        if self.text_show_len + show_length <= len(self.text_all):
            self.text_show_len += show_length
        self.text = self.text_all[:self.text_show_len]
        self._adjust(length)
        self.show(pos, screen)

    def show_all(self, pos, screen, length=length_all):
        if self.text != self.text_all:
            self.text = self.text_all
            self._adjust(length)
        self.show(pos, screen)

    def setting(self, text_in="", color=color_all, font=font_all, size=size_all):
        """重新设定参数"""
        self.size = size
        self.font = font
        self.text = text_in
        self.color = color
        self.text_all = self.text
        self.text_show_len = 0
        self.text_adjust = []

    def is_show_all(self):
        return self.text == self.text_all

    def get_text(self):
        return self.text

    def set_text(self, text_in=""):
        self.text = text_in

    def get_color(self):
        return self.color

    def set_color(self, color=color_all):
        self.color = color

    def get_font(self):
        return self.font

    def set_font(self, font=font_all):
        self.font = font

    def get_size(self):
        return self.size

    def set_size(self, size=size_all):
        self.size = size


class Show:
    """进行视频播放，可以提高软件效率"""
    def __init__(self):
        # try:
        #     self.clip1 = VideoFileClip(r'./data/一等奖.mp4')
        #     self.clip2 = VideoFileClip(r'./data/二等奖.mp4')
        #     self.clip3 = VideoFileClip(r'./data/三等奖.mp4')
        #     self.clip4 = VideoFileClip(r'./data/参与奖.mp4')
        # except OSError:
        #     self.clip1 = VideoFileClip(r'../data/一等奖.mp4')
        #     self.clip2 = VideoFileClip(r'../data/二等奖.mp4')
        #     self.clip3 = VideoFileClip(r'../data/三等奖.mp4')
        #     self.clip4 = VideoFileClip(r'../data/参与奖.mp4')
        # except:
        #     print("文件错误或文件路径不存在")
        pass

    def show_1(self):
        try:
            self.clip1 = VideoFileClip(r'./data/一等奖.mp4')
        except OSError:
            self.clip1 = VideoFileClip(r'../data/一等奖.mp4')
        except:
            print("文件错误或文件路径不存在")
        self.clip1.preview()
        self.clip1.close()

    def show_2(self):
        try:
            self.clip2 = VideoFileClip(r'./data/二等奖.mp4')
        except OSError:
            self.clip2 = VideoFileClip(r'../data/二等奖.mp4')
        except:
            print("文件错误或文件路径不存在")
        self.clip2.preview()
        self.clip2.close()

    def show_3(self):
        try:
            self.clip3 = VideoFileClip(r'./data/三等奖.mp4')
        except OSError:
            self.clip3 = VideoFileClip(r'../data/三等奖.mp4')
        except:
            print("文件错误或文件路径不存在")
        self.clip3.preview()
        self.clip3.close()

    def show_4(self):
        try:
            self.clip4 = VideoFileClip(r'./data/参与奖.mp4')
        except OSError:
            self.clip4 = VideoFileClip(r'../data/参与奖.mp4')
        except:
            print("文件错误或文件路径不存在")
        self.clip4.preview()
        self.clip4.close()


def is_tick(x, y, inf):
    if (x > inf[0][0]) and (x < inf[0][1]):
        if (y > inf[1][0]) and (y < inf[1][1]):
            return 1
    return 0


VIDEOSHOW = Show()
