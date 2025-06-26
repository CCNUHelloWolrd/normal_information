# -*- coding: utf-8 -*-
# app.menu.py

import pygame
from .level_select import LevelSelect
from .settings import Settings


class Menu:
    """游戏菜单界面类

    提供游戏菜单
    """
    def __init__(self, main_game):
        """配置菜单界面属性"""
        # 界面属性
        self.main_game = main_game
        self.width, self.height = main_game.width, main_game.height
        # 按钮属性与绑定的功能
        self.buttons = [
            {"rect": pygame.Rect(self.width//2-100, self.height//2-75, 200, 50),
             "text": "开始游戏", "action": self.start_game},
            {"rect": pygame.Rect(self.width//2-100, self.height//2-15, 200, 50),
             "text": "游戏设置", "action": self.game_settings},
            {"rect": pygame.Rect(self.width//2-100, self.height//2+45, 200, 50),
             "text": "退出游戏", "action": self.quit_game}
        ]
        # todo（zrk）: 一般而言，WINDOWS系统默认具有此字体, 单独将此字体加入游戏资源
        self.title_font = pygame.font.Font("C:/Windows/Fonts/STXINWEI.TTF", 48)
        self.button_font = pygame.font.Font("C:/Windows/Fonts/STXINWEI.TTF", 24)

    def handle_event(self, event):
        """处理菜单界面交互"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键点击
                for button in self.buttons:
                    # 检测事件碰撞
                    if button["rect"].collidepoint(event.pos):
                        button["action"]()

    def start_game(self):
        """界面按钮绑定的功能函数：跳转到关卡选择界面"""
        self.main_game.change_screen(LevelSelect(self.main_game))

    def game_settings(self):
        """界面按钮绑定的功能函数：跳转到游戏设置界面"""
        self.main_game.change_screen(Settings(self.main_game))

    def quit_game(self):
        """界面按钮绑定的功能函数：退出游戏"""
        # todo(zrk):退出游戏时应当执行保存数据等操作
        self.main_game.running = False

    def update(self):
        pass

    def draw(self):
        # 背景
        self.main_game.screen.fill((240, 240, 240))

        # 加载标题
        title_text = self.title_font.render(self.main_game.name, True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(self.width//2, self.height//4))
        self.main_game.screen.blit(title_text, title_rect)

        # 绘制按钮
        for button in self.buttons:
            pygame.draw.rect(self.main_game.screen, (200, 200, 200), button["rect"])
            pygame.draw.rect(self.main_game.screen, (100, 100, 100), button["rect"], 2)
            text = self.button_font.render(button["text"], True, (0, 0, 0))
            text_rect = text.get_rect(center=button["rect"].center)
            self.main_game.screen.blit(text, text_rect)
