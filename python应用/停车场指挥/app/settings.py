# -*- coding: utf-8 -*-
# app.settings.py

import pygame


class Settings:
    """设置界面类"""
    def __init__(self, main_game):
        """配置设置界面属性"""
        # 界面属性
        self.main_game = main_game
        self.width, self.height = main_game.width, main_game.height
        # 按钮属性
        self.back_button = pygame.Rect(20, 20, 100, 40)
        # 滑块属性
        self.sliders = []
        self.setup_settings()
        # todo（zrk）: 一般而言，WINDOWS系统默认具有此字体, 单独将此字体加入游戏资源
        self.title_font = pygame.font.Font("C:/Windows/Fonts/STXINWEI.TTF", 48)
        self.button_font = pygame.font.Font("C:/Windows/Fonts/STXINWEI.TTF", 24)

    def setup_settings(self):
        # 音量设置
        self.sliders.append({
            "name": "音量",
            "rect": pygame.Rect(self.width // 2 - 100, self.height // 2 - 50, 200, 20),
            # "value": self.main_game.save_data.get_setting("volume", 70),
            "value": 70,
            "min": 0, "max": 100
        })

        # 音效设置
        self.sliders.append({
            "name": "音效",
            "rect": pygame.Rect(self.width // 2 - 100, self.height // 2 + 10, 200, 20),
            # "value": self.main_game.save_data.get_setting("sfx", 80),
            "value": 70,
            "min": 0, "max": 100
        })

        # 灵敏度设置
        self.sliders.append({
            "name": "灵敏度",
            "rect": pygame.Rect(self.width // 2 - 100, self.height // 2 + 70, 200, 20),
            # "value": self.main_game.save_data.get_setting("sensitivity", 50),
            "value": 70,
            "min": 10, "max": 100
        })

    def handle_event(self, event):
        """交互处理"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键点击
                if self.back_button.collidepoint(event.pos):
                    self.main_game.return_screen()
                else:
                    for slider in self.sliders:
                        if slider["rect"].collidepoint(event.pos):
                            slider["value"] = self.calculate_slider_value(slider, event.pos[0])
                            # self.main_game.save_data.set_setting(slider["name"].lower(), slider["value"])

        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:  # 左键拖动
                for slider in self.sliders:
                    if slider["rect"].collidepoint(event.pos):
                        slider["value"] = self.calculate_slider_value(slider, event.pos[0])
                        # self.main_game.save_data.set_setting(slider["name"].lower(), slider["value"])

    @staticmethod
    def calculate_slider_value(slider, x_pos):
        """计算得出滑块值"""
        rel_x = x_pos - slider["rect"].x
        value = (rel_x / slider["rect"].width) * (slider["max"] - slider["min"]) + slider["min"]
        value = max(slider["min"], min(slider["max"], value))
        return int(value)

    def update(self):
        pass

    def draw(self):
        """绘制"""
        self.main_game.screen.fill((240, 240, 240))

        # 绘制标题
        title = self.title_font.render("游戏设置", True, (0, 0, 0))
        title_rect = title.get_rect(center=(self.width // 2, 50))
        self.main_game.screen.blit(title, title_rect)

        # 绘制返回按钮
        pygame.draw.rect(self.main_game.screen, (200, 200, 200), self.back_button)
        pygame.draw.rect(self.main_game.screen, (100, 100, 100), self.back_button, 2)
        button_text = self.button_font.render("返回", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=self.back_button.center)
        self.main_game.screen.blit(button_text, button_text_rect)

        # 绘制滑块
        for slider in self.sliders:
            # 绘制滑块背景
            pygame.draw.rect(self.main_game.screen, (150, 150, 150), slider["rect"])

            # 绘制滑块当前值
            rel_value = (slider["value"] - slider["min"]) / (slider["max"] - slider["min"])
            handle_x = slider["rect"].x + int(rel_value * slider["rect"].width)
            handle_rect = pygame.Rect(handle_x - 8, slider["rect"].y - 8, 16, 36)
            pygame.draw.rect(self.main_game.screen, (50, 100, 200), handle_rect)

            # 绘制滑块名称和值
            name_text = self.button_font.render(slider["name"], True, (0, 0, 0))
            name_rect = name_text.get_rect(midright=(slider["rect"].x - 10, slider["rect"].centery))
            self.main_game.screen.blit(name_text, name_rect)

            value_text = self.button_font.render(str(slider["value"]), True, (0, 0, 0))
            value_rect = value_text.get_rect(midleft=(slider["rect"].x + slider["rect"].width + 10,
                                                      slider["rect"].centery))
            self.main_game.screen.blit(value_text, value_rect)
