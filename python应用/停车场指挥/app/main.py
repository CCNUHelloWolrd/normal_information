# -*- coding: utf-8 -*-
# app.main.py

import pygame
import sys
from .menu import Menu


class Engine:
    """游戏启动类

    所有游戏操作由此进入，所有游戏界面逻辑由此控制
    """

    def __init__(self):
        """配置环境属性、初始化游戏、用于操控界面逻辑"""
        pygame.init()
        # 界面属性
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_list = []
        # 界面显示
        self.name = "停车场小游戏"
        pygame.display.set_caption(self.name)
        # 游戏属性配置
        self.clock = pygame.time.Clock()
        # self.save_data = SaveData()
        self.current_screen = Menu(self)
        self.running = True

    def run(self):
        """游戏运行，处理交互"""
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.current_screen.handle_event(event)
            self.current_screen.update()
            self.current_screen.draw()
            pygame.display.flip()
        # 退出前工作
        pygame.quit()
        sys.exit()

    def change_screen(self, screen):
        """进入新的界面"""
        self.screen_list.append(self.current_screen)
        self.current_screen = screen

    def return_screen(self):
        """返回上一级界面"""
        if self.screen_list is not None:
            self.current_screen = self.screen_list.pop(-1)


def start():
    game = Engine()
    game.run()


if __name__ == "__main__":
    start()
