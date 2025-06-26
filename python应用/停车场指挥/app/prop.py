# -*- coding: utf-8 -*-
# app.prop.py


class Prop:
    """道具类

    存储道具信息和对应功能
    """
    def __init__(self, name, image):
        """基本属性"""
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()

    def use(self, car):
        """道具功能"""
        if self.name == "reverse":
            car.reverse_direction()
