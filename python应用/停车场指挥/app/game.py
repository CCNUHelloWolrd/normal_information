# -*- coding: utf-8 -*-
# app.game.py

import pygame
import random
import os
from .car import Car
from .prop import Prop


class Game:
    """游戏界面类

    一个对象对应一个游戏关卡，是游戏游玩性的主要点
    通过恒定的随机数种子来随机生成不同关卡的内容
    """
    def __init__(self, main_game, level):
        """配置游戏界面属性"""
        # 界面属性
        self.main_game = main_game
        self.width, self.height = main_game.width, main_game.height
        self.level = level
        random.seed(level)  # 使用关卡号作为随机种子，确保每关地图固定
        # todo（zrk）: 一般而言，WINDOWS系统默认具有此字体, 单独将此字体加入游戏资源
        self.title_font = pygame.font.Font("C:/Windows/Fonts/STXINWEI.TTF", 36)
        self.button_font = pygame.font.Font("C:/Windows/Fonts/STXINWEI.TTF", 24)
        # 按钮属性
        self.back_button = {"rect": pygame.Rect(20, 20, 100, 40),
                            "text": "返回", "action": self.main_game.return_screen}

        # 交互参数
        self.selected_car = None
        self.selected_prop = None
        self.props = [Prop("reverse", pygame.image.load(os.getcwd() + r"\app" + r"\assets\reverse.png"))]
        self.state = "playing"  # playing, won, lost
        # self.cars = []
        # 初始化地图
        self.setup_map()

    def setup_map(self):
        self.cars = []
        # 随机生成120辆车，当一辆车与之前生成的 车辆不重叠的时候保留
        # 实现随机摆放和随机数量的目的
        # 可以手动调节车辆的坐标的方向来自定义关卡
        for i in range(120):
            x = random.randint(2, 18) * 40
            y = random.randint(2, 13) * 40
            car = Car(x, y, random.choice(["right", "up", "left", "down"]))
            self.cars.append(car)
            # 检查其他汽车碰撞，发生碰撞时移除
            for other_car in self.cars:
                if other_car != car and car.rect.colliderect(other_car.rect):
                    self.cars.remove(car)
                    break

        # todo(zrk):效果不好看，实际上也用不到，后面可以添加特效
        # # 停车场边界
        # self.walls = []
        # self.walls.append(pygame.Rect(0, self.height // 10, self.width, 20))
        # self.walls.append(pygame.Rect(self.width - self.width // 10, 0, 20, self.height))
        # self.walls.append(pygame.Rect(0, self.height - self.height // 10, self.width, 20))
        # self.walls.append(pygame.Rect(self.width // 10, 0, 20, self.height))

    def handle_event(self, event):
        """交互处理"""
        if self.state == "won":  # 游戏胜利后单击返回选关界面
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.main_game.return_screen()
            return

        # 主要逻辑为：当单击时，若选中道具，则结束判断，
        #           若点击返回按钮，返回，
        #           若选中小车，若有已经选中的道具，执行道具效果，移除道中选中状态，返回
        #                     若有选中的小车（发生双击），小车移动，返回，
        #                     若没有选中小车，选中小车，返回
        #           否则，返回
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键点击
                if self.back_button["rect"].collidepoint(event.pos):
                    self.main_game.return_screen()
                    return
                pos = pygame.mouse.get_pos()
                # 检查是否点击了道具
                for prop in self.props:
                    if prop.rect.collidepoint(pos):
                        self.selected_prop = prop
                        return

                # 检查是否点击了汽车
                clicked_car = None
                for car in self.cars:
                    if car.rect.collidepoint(pos):
                        clicked_car = car
                        break

                if self.selected_prop:
                    # 使用道具
                    if clicked_car:
                        self.selected_prop.use(clicked_car)
                        self.selected_prop = None
                else:
                    # 选择汽车或移动汽车
                    if clicked_car:
                        if clicked_car == self.selected_car:
                            # 移动选中的汽车
                            while self.can_move_forward(clicked_car):   # 为了检测所有碰撞，小车实际上是一步步进行移动的
                                clicked_car.move_forward()
                                # 小车全部移走，游戏结束
                                if self.check_car_exited(clicked_car):
                                    self.cars.remove(clicked_car)
                                    if not self.cars:
                                        self.state = "won"
                                        # self.main_game.save_data.complete_level(self.level)
                                    break
                        else:
                            # 选中新汽车
                            self.selected_car = clicked_car
                    else:
                        # 未点击任何汽车，取消选择
                        self.selected_car = None

    def can_move_forward(self, car):
        # 检查汽车前方是否有障碍物或其他汽车
        test_rect = car.get_forward_rect()

        # todo(zrk): 实际上此处也是不必要检测，但是留着后续加功能
        # # 检查墙壁碰撞
        # for wall in self.walls:
        #     if test_rect.colliderect(wall):
        #         return False

        # 检查其他汽车碰撞
        for other_car in self.cars:
            if other_car != car and test_rect.colliderect(other_car.rect):
                return False

        return True

    def check_car_exited(self, car):
        # 检查汽车是否已经开出停车场
        if car.rect.left < 0 or car.rect.right > self.width or \
                car.rect.top < 0 or car.rect.bottom > self.height:
            return True
        return False

    def update(self):
        pass

    def draw(self):
        self.main_game.screen.fill((200, 200, 200))  # 灰色背景

        # # 绘制墙壁
        # for wall in self.walls:
        #     pygame.draw.rect(self.main_game.screen, (50, 50, 50), wall)

        # 绘制汽车
        for car in self.cars:
            car.draw(self.main_game.screen)
            if car == self.selected_car:
                pygame.draw.rect(self.main_game.screen, (100, 100, 100), car.rect, 3)

        # 绘制道具栏
        for i, prop in enumerate(self.props):
            prop.rect.topleft = (10 + i * 60, self.height - 60)
            pygame.draw.rect(self.main_game.screen, (100, 100, 100), prop.rect)
            self.main_game.screen.blit(prop.image, prop.rect)
            if prop == self.selected_prop:
                pygame.draw.rect(self.main_game.screen, (255, 255, 0), prop.rect, 3)

        # 绘制关卡信息
        # font = pygame.font.SysFont("Arial", 24)
        level_text = self.button_font.render(f"关卡 {self.level}", True, (0, 0, 0))
        self.main_game.screen.blit(level_text, (self.width - 100, 10))

        # 绘制返回按钮
        pygame.draw.rect(self.main_game.screen, (200, 200, 200), self.back_button["rect"])
        pygame.draw.rect(self.main_game.screen, (100, 100, 100), self.back_button["rect"], 2)
        button_text = self.button_font.render(self.back_button["text"], True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=self.back_button["rect"].center)
        self.main_game.screen.blit(button_text, button_text_rect)

        # 如果游戏胜利，显示胜利信息
        if self.state == "won":
            # font = pygame.font.SysFont("Arial", 48)
            win_text = self.button_font.render("胜利！点击返回关卡选择", True, (0, 150, 0))
            text_rect = win_text.get_rect(center=(self.width // 2, self.height // 2))
            pygame.draw.rect(self.main_game.screen, (255, 255, 255),
                             (text_rect.x - 20, text_rect.y - 20,
                              text_rect.width + 40, text_rect.height + 40))
            self.main_game.screen.blit(win_text, text_rect)
