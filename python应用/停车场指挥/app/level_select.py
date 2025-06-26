# -*- coding: utf-8 -*-
# app.level_select.py
import pygame
from .game import Game


class LevelSelect:
    """关卡界面类"""
    def __init__(self, main_game):
        """配置关卡界面属性"""
        # 界面属性
        self.main_game = main_game
        self.width, self.height = main_game.width, main_game.height
        # todo（zrk）: 一般而言，WINDOWS系统默认具有此字体, 单独将此字体加入游戏资源
        self.title_font = pygame.font.Font("C:/Windows/Fonts/STXINWEI.TTF", 36)
        self.button_font = pygame.font.Font("C:/Windows/Fonts/STXINWEI.TTF", 24)
        # 按钮属性
        self.back_button = {"rect": pygame.Rect(20, 20, 100, 40),
                            "text": "返回", "action": self.main_game.return_screen}
        # 功能参数
        self.levels = 20  # 总关卡数
        self.levels_per_row = 5  # 每行显示的关卡按钮
        self.level_buttons = self.create_level_buttons()

    def create_level_buttons(self):
        # todo： 此处有关卡依次解锁的功能，但是我不想要所以重写了一份没有这个功能的
        # buttons = []
        # # completed_levels = self.main_game.save_data.get_completed_levels()
        # button_size = 60
        # spacing = 20
        #
        # start_x = (self.width - (self.levels_per_row * button_size + (self.levels_per_row - 1) * spacing)) // 2
        # start_y = self.height // 3
        #
        # for i in range(self.levels):
        #     row = i // self.levels_per_row
        #     col = i % self.levels_per_row
        #     x = start_x + col * (button_size + spacing)
        #     y = start_y + row * (button_size + spacing)
        #
        #     level_num = i + 1
        #     # is_completed = level_num in completed_levels
        #     # is_locked = level_num > 1 and level_num - 1 not in completed_levels
        #
        #     buttons.append({
        #         "rect": pygame.Rect(x, y, button_size, button_size),
        #         "level": level_num,
        #         "completed": 0,
        #         "locked": 0
        #     })

        buttons = []
        button_size = 60
        spacing = 20

        # 起始点保证关卡按钮横坐标居中、纵坐标从三分之一开始
        start_x = (self.width - (self.levels_per_row * button_size + (self.levels_per_row - 1) * spacing)) // 2
        start_y = self.height // 3

        for i in range(self.levels):
            row = i // self.levels_per_row
            col = i % self.levels_per_row
            x = start_x + col * (button_size + spacing)
            y = start_y + row * (button_size + spacing)
            level_num = i + 1
            buttons.append({
                "rect": pygame.Rect(x, y, button_size, button_size),
                "level": level_num
            })
        return buttons

    def handle_event(self, event):
        """交互处理"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键点击
                if self.back_button["rect"].collidepoint(event.pos):
                    self.main_game.return_screen()
                else:
                    for button in self.level_buttons:
                        if button["rect"].collidepoint(event.pos):
                            self.main_game.change_screen(Game(self.main_game, button["level"]))

    def update(self):
        pass

    def draw(self):
        """绘制"""
        self.main_game.screen.fill((240, 240, 240))

        # 绘制标题
        title = self.title_font.render("选择关卡", True, (0, 0, 0))
        title_rect = title.get_rect(center=(self.width // 2, 50))
        self.main_game.screen.blit(title, title_rect)

        # 绘制返回按钮
        pygame.draw.rect(self.main_game.screen, (200, 200, 200), self.back_button["rect"])
        pygame.draw.rect(self.main_game.screen, (100, 100, 100), self.back_button["rect"], 2)
        button_text = self.button_font.render(self.back_button["text"], True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=self.back_button["rect"].center)
        self.main_game.screen.blit(button_text, button_text_rect)

        # 绘制关卡按钮
        for button in self.level_buttons:
            pygame.draw.rect(self.main_game.screen, (200, 200, 200), button["rect"])
            pygame.draw.rect(self.main_game.screen, (100, 100, 100), button["rect"], 2)
            text = self.button_font.render(str(button["level"]), True, (0, 0, 0))
            text_rect = text.get_rect(center=button["rect"].center)
            self.main_game.screen.blit(text, text_rect)

            # if button["locked"]:
            #     pygame.draw.rect(self.main_game.screen, (150, 150, 150), button["rect"])
            #     # 绘制锁图标
            #     pygame.draw.circle(self.main_game.screen, (50, 50, 50),
            #                        button["rect"].center, button["rect"].width // 4)
            # else:
            #     if button["completed"]:
            #         pygame.draw.rect(self.main_game.screen, (100, 200, 100), button["rect"])
            #     else:
            #         pygame.draw.rect(self.main_game.screen, (200, 200, 200), button["rect"])
            #     pygame.draw.rect(self.main_game.screen, (100, 100, 100), button["rect"], 2)
            #
            #     # 绘制关卡数字
            #     font = pygame.font.SysFont("Arial", 24)
            #     text = font.render(str(button["level"]), True, (0, 0, 0))
            #     text_rect = text.get_rect(center=button["rect"].center)
            #     self.main_game.screen.blit(text, text_rect)
