# -*- coding: utf-8 -*-
# app.car.py
import pygame
import os


class Car:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction  # "right" 、 "up"、 "left" 、 "down"
        self.speed = 5
        self.width = 80
        self.height = 40
        self.image = None
        self.rect = None
        self.load_images()
        self.update_rect()

    def load_images(self):
        # 当图片资源无法加载时，绘制矩形代替
        try:
            self.image = pygame.image.load(os.getcwd() + r"\app" + r"\assets\car1.png")
            if self.direction == "right":
                # self.image = pygame.image.load(WORK_PATH + "/assets/car1.png")
                self.image = pygame.transform.scale(self.image, (80, 40))

            elif self.direction == "left":
                # self.image = pygame.image.load("./assets/car1.png")
                self.image = pygame.transform.scale(self.image, (80, 40))
                self.image = pygame.transform.flip(self.image, True, False)

            elif self.direction == "up":
                # self.image = pygame.image.load("./assets/car1.png")
                self.image = pygame.transform.scale(self.image, (80, 40))
                self.image = pygame.transform.rotate(self.image, 90)

            else:
                # self.image = pygame.image.load("./assets/car1.png")
                self.image = pygame.transform.scale(self.image, (80, 40))
                self.image = pygame.transform.rotate(self.image, 270)

        except FileNotFoundError:
            if self.direction == "right":
                self.image = pygame.Surface((self.width, self.height))
                self.image.fill((155, 0, 0))
                pygame.draw.line(self.image, (0, 255, 0), (self.width - 5, 0), (self.width - 5, self.height), 2)
            elif self.direction == "left":
                self.image = pygame.Surface((self.width, self.height))
                self.image.fill((155, 0, 0))
                pygame.draw.line(self.image, (0, 255, 0), (5, 0), (5, self.height), 2)
            elif self.direction == "up":
                self.image = pygame.Surface((self.height, self.width))
                self.image.fill((0, 0, 155))
                pygame.draw.line(self.image, (0, 255, 0), (0, 5), (self.height, 5), 2)
            else:
                self.image = pygame.Surface((self.height, self.width))
                self.image.fill((0, 0, 155))
                pygame.draw.line(self.image, (0, 255, 0), (0, self.width - 5), (self.height, self.width - 5), 2)

    def update_rect(self):
        """更新小车整体区域"""
        if self.direction == "right":
            self.rect = pygame.Rect(self.x - self.width // 2, self.y - self.height // 2,
                                    self.width, self.height)

        elif self.direction == "left":
            self.rect = pygame.Rect(self.x - self.width // 2, self.y - self.height // 2,
                                    self.width, self.height)

        elif self.direction == "down":
            self.rect = pygame.Rect(self.x - self.height // 2, self.y - self.width // 2,
                                    self.height, self.width)

        else:
            self.rect = pygame.Rect(self.x - self.height // 2, self.y - self.width // 2,
                                    self.height, self.width)

    def move_forward(self):
        """小车前进"""
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        else:
            self.y -= self.speed
        self.update_rect()

    def reverse_direction(self):
        """车辆翻转方向"""
        if self.direction == "right":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "right"
        elif self.direction == "up":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "up"

        self.load_images()
        self.update_rect()

    def get_forward_rect(self):
        # 获取汽车向前移动一格后的矩形
        if self.direction == "right":
            return pygame.Rect(self.rect.x + self.speed, self.rect.y,
                               self.rect.width, self.rect.height)
        elif self.direction == "left":
            return pygame.Rect(self.rect.x - self.speed, self.rect.y,
                               self.rect.width, self.rect.height)
        elif self.direction == "down":
            return pygame.Rect(self.rect.x, self.rect.y + self.speed,
                               self.rect.width, self.rect.height)
        else:
            return pygame.Rect(self.rect.x, self.rect.y - self.speed,
                               self.rect.width, self.rect.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
