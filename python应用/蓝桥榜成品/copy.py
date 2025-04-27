# import pygame
# import sys
# import random
# import cfg2
#
# # 为了实现游戏功能，自定义类相比于初始进行了很多不可取的调节，但是可以修改后程序可以跑通
# # todo:后续优化重构
# ##
# # 自定义类
#
#
# class Image(object):
#     """图像类：一个可以方便贴图的类"""
#
#     def __init__(self, path=""):
#         self.path = path
#         # self.img = pygame.image.load(self.path).convert_alpha()
#         self.img = pygame.image.load(self.path)
#         self.rect = self.img.get_rect()
#
#     def show(self, pos, screen, mode=0):
#         if mode == 0:
#             self.rect.topleft = pos
#         elif mode == 1:
#             self.rect.midtop = pos
#         elif mode == 2:
#             self.rect.topright = pos
#         elif mode == 3:
#             self.rect.midleft = pos
#         elif mode == 4:
#             self.rect.center = pos
#         elif mode == 5:
#             self.rect.midright = pos
#         elif mode == 6:
#             self.rect.bottomleft = pos
#         elif mode == 7:
#             self.rect.midbottom = pos
#         elif mode == 8:
#             self.rect.bottomright = pos
#         screen.blit(self.img, self.rect)
#
#     def setting(self, path=""):
#         self.path = path
#         self.img = pygame.image.load(self.path).convert_alpha()
#         self.rect = self.img.get_rect()
#
#     def get_path(self):
#         return self.path
#
#
# class Write(object):
#     """文字类: 用于直接绘制少量文字"""
#     font_all = cfg2.font_path3
#     size_all = 20
#     color_all = cfg2.color_black
#
#     def __init__(self, text_in="", color=color_all, font=font_all, size=size_all):
#         # 传入 文本、文本颜色[、文体路径、文体大小]
#         self.size = size
#         self.font = font
#         self.text = text_in
#         self.color = color
#         # todo:优化
#         self.x = 0
#
#     def get_y(self):
#         return self.x
#
#     def show(self, pos, screen, mode=0):
#
#         font = pygame.font.Font(self.font, self.size)
#         now_text = font.render(self.text, True, self.color)
#         text_rect = now_text.get_rect()
#         self.x = text_rect[2]
#         if mode == 0:
#             text_rect.topleft = pos
#         elif mode == 1:
#             text_rect.midtop = pos
#         elif mode == 2:
#             text_rect.topright = pos
#         elif mode == 3:
#             text_rect.midleft = pos
#         elif mode == 4:
#             text_rect.center = pos
#         elif mode == 5:
#             text_rect.midright = pos
#         elif mode == 6:
#             text_rect.bottomleft = pos
#         elif mode == 7:
#             text_rect.midbottom = pos
#         elif mode == 8:
#             text_rect.bottomright = pos
#         screen.blit(now_text, text_rect)
#
#     def setting(self, text_in="", color=color_all, font=font_all, size=size_all):
#         self.size = size
#         self.font = font
#         self.text = text_in
#         self.color = color
#
#     def get_text(self):
#         return self.text
#
#     def set_text(self, text_in=""):
#         self.text = text_in
#
#     def get_color(self):
#         return self.color
#
#     def set_color(self, color=color_all):
#         self.color = color
#
#     def get_font(self):
#         return self.font
#
#     def set_font(self, font=font_all):
#         self.font = font
#
#     def get_size(self):
#         return self.size
#
#     def set_size(self, size=size_all):
#         self.size = size
#
#
# class Paragraph(object):
#     """用于解决大量文字的段落显示问题"""
#     font_all = cfg2.font_path3
#     size_all = 20
#     color_all = cfg2.color_black
#     length_all = 20
#
#     def __init__(self, text_in="", color=color_all, font=font_all, size=size_all):
#         """初始化文字内容与打印参数与滚屏参数"""
#         self.size = size
#         self.font = font
#         self.text = text_in
#         self.color = color
#         self.text_all = self.text
#         self.text_show_len = 0
#         self.text_adjust = []
#
#     def _adjust(self, length=length_all):
#         """解决多行显示与换行问题"""
#         text_len = len(self.text)
#         text_adjust = []
#         text_len_key = 0
#         text_key = ""
#         for i in range(text_len):
#             if self.text[i] == "\n":
#                 text_key += self.text[i]
#                 text_adjust.append(text_key)
#                 text_len_key = 0
#                 text_key = ""
#                 continue
#             text_key += self.text[i]
#             text_len_key += 1
#             if text_len_key >= length:
#                 text_adjust.append(text_key)
#                 text_key = ""
#                 text_len_key = 0
#         if text_len_key != 0:
#             text_adjust.append(text_key)
#         self.text_adjust = [Write(text_, self.color, self.font, self.size) for text_ in text_adjust]
#
#     def show(self, pos, screen):
#         """默认打印或者再次打印"""
#         if len(self.text_adjust) == 0:
#             self._adjust()
#         for i in range(len(self.text_adjust)):
#             self.text_adjust[i].show((pos[0], pos[1] + i * self.size), screen)
#
#     def show_len(self, pos, screen, length=length_all):
#         """进行打印宽度调整的打印"""
#         self._adjust(length)
#         for i in range(len(self.text_adjust)):
#             self.text_adjust[i].show((pos[0], pos[1] + i * self.size), screen)
#
#     def show_slow(self, pos, screen, show_length=1, length=length_all):
#         if self.text_show_len + show_length <= len(self.text_all):
#             self.text_show_len += show_length
#         self.text = self.text_all[:self.text_show_len]
#         self._adjust(length)
#         self.show(pos, screen)
#
#     def show_all(self, pos, screen, length=length_all):
#         if self.text != self.text_all:
#             self.text = self.text_all
#             self._adjust(length)
#         self.show(pos, screen)
#
#     def setting(self, text_in="", color=color_all, font=font_all, size=size_all):
#         """重新设定参数"""
#         self.size = size
#         self.font = font
#         self.text = text_in
#         self.color = color
#         self.text_all = self.text
#         self.text_show_len = 0
#         self.text_adjust = []
#
#     def is_show_all(self):
#         return self.text == self.text_all
#
#     def get_text(self):
#         return self.text
#
#     def set_text(self, text_in=""):
#         self.text = text_in
#
#     def get_color(self):
#         return self.color
#
#     def set_color(self, color=color_all):
#         self.color = color
#
#     def get_font(self):
#         return self.font
#
#     def set_font(self, font=font_all):
#         self.font = font
#
#     def get_size(self):
#         return self.size
#
#     def set_size(self, size=size_all):
#         self.size = size
#
#
# class CtBase(object):
#     """控件基类，用于储存互动按钮的激活状态信息"""
#
#     def __init__(self):
#         self.active = False
#
#     def enable(self):
#         self.active = True
#
#     def disable(self):
#         self.active = False
#
#     def update(self, event: pygame.event) -> ...:
#         raise NotImplementedError
#
#
# class Button(CtBase):
#     """用于集成一个按钮的全部属性"""
#     # todo:补充音效
#     text_font_all = cfg2.font_path3
#     text_size_all = 20
#     text_color_all = cfg2.color_black
#     click_sound_all = None
#     size_all = (87, 27)
#     up_color_all = cfg2.color_white200
#     down_color_all = cfg2.color_white130
#     outer_edge_color_all = cfg2.color_black
#     inner_edge_color_all = cfg2.color_white
#     fill_color_all = True
#     edge_color_all = True
#
#     def __init__(self, surface: pygame.Surface, pos,
#                  text_in="", text_color=text_color_all, text_font=text_font_all, text_size=text_size_all,
#                  up_color=up_color_all, down_color=down_color_all,
#                  outer_edge_color=outer_edge_color_all, inner_edge_color=inner_edge_color_all,
#                  fill_color=fill_color_all, edge_color=edge_color_all,
#                  call_function=None, click_sound=click_sound_all, size=size_all):
#         """
#         text_in="" 按钮显示文字
#         text_color=text_color_all 按钮显示文字颜色
#         text_font=text_font_all 按钮显示文字字体
#         text_size=text_size_all 按钮显示文字大小
#          up_color=up_color_all 按钮未按下时颜色
#          down_color=down_color_all 按钮按下时颜色
#          outer_edge_color=outer_edge_color_all 按钮框外边缘颜色
#          inner_edge_color=inner_edge_color_all 按钮框内边缘颜色
#          fill_color=fill_color_all 按钮框内部填充颜色
#          call_function=None 按钮按下时进行的功能
#          click_sound=click_sound_all 按钮按下时的音效
#          size=size_all 按钮框的大小（一般由文字来自行决定？）
#         """
#         super(Button, self).__init__()
#
#         if isinstance(click_sound, str):
#             click_sound = pygame.mixer.Sound(click_sound)
#
#         # 按钮的绘制位置（左上角）
#         # if isinstance(pos[0], str):
#         #     assert pos[0] == "center"
#         #     # pos[0] = (surface.get_width() - size[0]) // 2
#         # if isinstance(pos[1], str):
#         #     assert pos[1] == "center"
#         #     # pos[1] = (surface.get_height() - size[1]) // 2
#         if isinstance(click_sound, str):
#             click_sound = pygame.mixer.Sound(click_sound)
#         # 按钮surface
#         self.pos = pos
#         self.button_surface = surface.subsurface(pos[0], pos[1], size[0], size[1])
#
#         # todo:测试合适大小或者根据文本更新
#         self.outer_rect = 0, 0, size[0], size[1]
#         self.inner_rect = self.outer_rect[0] + 1, self.outer_rect[1] + 1, self.outer_rect[2] - 2, self.outer_rect[3] - 2
#         self.text_size = text_size
#         self.text_font = text_font
#         self.text = text_in
#         self.text_color = text_color
#         self.text_show = Write(self.text, self.text_color, self.text_font, self.text_size)
#         self.size = size
#         self.call_function = call_function
#         self.click_sound = click_sound
#         self.up_color = up_color
#         self.down_color = down_color
#         self.outer_edge_color = outer_edge_color
#         self.inner_edge_color = inner_edge_color
#         self.fill_color = fill_color
#         self.edge_color = edge_color
#         # 按钮是否被按下
#         self.is_down = False
#
#     # def draw_up(self):
#     #     """绘制未被点击的按钮"""
#     #     self.is_down = False
#     #     self.draw(self.up_color)
#     #
#     # def draw_down(self):
#     #     """绘制已被点击的按钮"""
#     #     self.is_down = True
#     #     self.draw(self.down_color)
#
#     def show(self):
#         """根据按钮的按下与否，对按钮显示效果进行更新"""
#         if self.fill_color is True:
#             if self.is_down is True:
#                 base_color = self.down_color
#             else:
#                 base_color = self.up_color
#             # 填充按钮底色
#             self.button_surface.fill(base_color)
#         if self.edge_color is True:
#             # 绘制外框
#             pygame.draw.rect(self.button_surface, self.outer_edge_color, self.outer_rect, width=1)
#             # 绘制内框
#             pygame.draw.rect(self.button_surface, self.inner_edge_color, self.inner_rect, width=1)
#         # 绘制按钮文本
#         self.text_show.show((2, 2), self.button_surface)
#
#     # todo:将激活与被激活联系起来
#     # def enable(self):
#     #     """激活按钮"""
#     #     self.active = True
#     #     self.draw_up()
#     #
#     # def disable(self):
#     #     """冻结按钮"""
#     #     self.active = False
#     #     self.draw_down()
#
#     def update(self, event: pygame.event):
#         """根据pygame.event对按钮进行状态更新和方法调用"""
#         """
#         当鼠标按下时，按钮处于按下状态
#         当鼠标移动时，鼠标离开按钮范围且按钮处于按下状态时，按钮转化为松开状态
#         当鼠标松开时，按钮处于按下状态且鼠标停留在按钮上，执行鼠标功能
#         """
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             # 鼠标左键按下
#             if self._pos_in_surface(event.pos):
#                 self.is_down = True
#         elif event.type == pygame.MOUSEMOTION:
#             # 鼠标移动事件，用来检测按钮是否应该弹起
#             if not self._pos_in_surface(event.pos) and self.is_down:
#                 self.is_down = False
#         elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
#             # 鼠标左键弹起事件
#             if self._pos_in_surface(event.pos) and self.is_down:
#                 # todo:播放按钮点击音效(补充)
#                 # 调用相应方法
#                 if self.call_function is not None:
#                     self.call_function()
#                     return True
#         return False
#
#     def _pos_in_surface(self, pos):
#         # print(f"pos:->{pos}")
#         # print(f"self.pos:->{self.pos}")
#         if (pos[0] > self.pos[0]) and (pos[0] < self.pos[0] + self.size[0]):
#             if (pos[1] > self.pos[1]) and (pos[1] < self.pos[1] + self.size[1]):
#                 return True
#         return False
#
#
# class PlayerValue(object):
#     """最基础的战斗人物的各种属性,仅支持数据的储存"""
#     # todo:角色状态的绘制与角色玩法的支持
#     # todo:角色的状态
#     #       属性：
#     #           生命基础值、生命系数
#     #           护盾基础值，护盾系数
#     #           攻击基础值，攻击系数
#     #       状态：
#     #           攻击状态，格挡状态，连击状态
#     #           各种状态下所需要的参数
#     #       buff:
#     #           影响上述属性与状态
#     # todo:角色的绘制
#     #       包含元素：
#     #           立绘
#     #           静止与运动时的动画
#     #           名称与血条
#     #           各种状态下的特殊需求
#     # todo:角色的玩法支持
#     #       互动：
#     #           发起攻击与承受攻击（与bullet类互动）
#     #           与各种场外函数进行互动
#     #           每场结束后状态不清除而是仅有最基本的清除
#     #           关于小怪的智能问题，（设置循环列表）
#     #
#     health_all = 100
#     health_kis_all = 10
#     shield_all = 20
#     shield_kis_all = 1.0
#     attack_all = 10
#     attack_kis_all = 1.0
#
#     def __init__(self, pl_name="",
#                  health=health_all, health_kis=health_kis_all,
#                  shield=shield_all, shield_kis=shield_kis_all,
#                  attack=attack_all, attack_kis=attack_kis_all):
#         """
#         属性：
#           生命基础值、生命系数
#           护盾基础值，护盾系数
#           攻击基础值，攻击系数
#         状态：
#           攻击状态，格挡状态，连击状态
#           各种状态下所需要的参数
#         """
#         super().__init__()
#         self.name = pl_name
#         self.health = health
#         self.health_kis = health_kis
#         self.attack = attack
#         self.attack_kis = attack_kis
#         self.shield = shield
#         self.shield_kis = shield_kis
#         self.mode_attack = True
#         self.mode_shield = False
#         self.mode_continue = False
#
#     def _set_mode(self, mode):
#         if mode == 1:
#             self.mode_attack = True
#             self.mode_shield = False
#             self.mode_continue = False
#         elif mode == 2:
#             self.mode_attack = False
#             self.mode_shield = True
#             self.mode_continue = False
#         elif mode == 3:
#             self.mode_attack = False
#             self.mode_shield = False
#             self.mode_continue = True
#
#     def set_mode_attack(self):
#         self._set_mode(1)
#
#     def set_mode_shield(self):
#         self._set_mode(2)
#
#     def set_mode_continue(self):
#         self._set_mode(3)
#
#     def get_mode(self):
#         if self.mode_attack is True:
#             return "attack"
#         elif self.mode_shield is True:
#             return "shield"
#         elif self.mode_continue is True:
#             return "continue"
#         return ""
#
#     def set_health(self, health):
#         self.health = health
#
#     def set_health_kis(self, health_kis):
#         self.health_kis = health_kis
#
#     def set_shield(self, shield):
#         self.shield = shield
#
#     def set_shield_kis(self, shield_kis):
#         self.shield_kis = shield_kis
#
#     def set_attack(self, attack):
#         self.attack = attack
#
#     def set_attack_kis(self, attack_kis):
#         self.attack_kis = attack_kis
#
#     def set_basic(self, health, attack, shield):
#         """生命，攻击，防御"""
#         self.health = health
#         self.attack = attack
#         self.shield = shield
#
#     def get_basic(self):
#         """生命，攻击，防御"""
#         return [self.health, self.attack, self.shield]
#
#     def set_kis(self, health_kis, attack_kis, shield_kis):
#         """生命，攻击，防御"""
#         self.health_kis = health_kis
#         self.attack_kis = attack_kis
#         self.shield_kis = shield_kis
#
#     def get_kis(self):
#         """生命，攻击，防御"""
#         return [self.health_kis, self.attack_kis, self.shield_kis]
#
#     def is_die(self):
#         if self.health <= 0:
#             return True
#         return False
#
#     def get_name(self):
#         return self.name
#
#
# class Player(pygame.sprite.Sprite):
#     """战斗界面的角色类，进行角色属性与外界的交互，负责实现战斗的特效"""
#     # todo:角色状态的绘制与角色玩法的支持
#     # todo:角色的绘制
#     #       包含元素：
#     #           立绘
#     #           静止与运动时的动画
#     #           名称与血条
#     #           各种状态下的特殊需求
#     # todo:角色的玩法支持
#     #       互动：
#     #           发起攻击与承受攻击（与bullet类互动）
#     #           与各种场外函数进行互动
#     #           每场结束后状态不清除而是仅有最基本的清除
#     #           关于小怪的智能问题，（设置循环列表）
#     #
#     health_all = 100
#     health_kis_all = 10
#     shield_all = 20
#     shield_kis_all = 1.0
#     attack_all = 10
#     attack_kis_all = 1.0
#     pl_pos_all = (100, 500)
#
#     def __init__(self, pl_image="", pl_name="", pl_pos=pl_pos_all,
#                  health=health_all, health_kis=health_kis_all,
#                  shield=shield_all, shield_kis=shield_kis_all,
#                  attack=attack_all, attack_kis=attack_kis_all,
#                  show_mode=0, attack_set_area=20):
#         """
#         继承精灵类以用于和子弹类进行碰撞检验
#         通过事件来改变相应的人物属性与人物状态
#         绘制相应人物属性与人物状态的特效
#         """
#         super().__init__()
#         # 储存数值
#         self.value = PlayerValue(pl_name=pl_name, health=health, health_kis=health_kis,
#                                  shield=shield, shield_kis=shield_kis, attack=attack, attack_kis=attack_kis)
#         # 用于精灵类的绘制
#         self.image = pygame.image.load(pl_image)
#         self.rect = self.image.get_rect()
#         self.pos = pl_pos
#         self.rect.bottomleft = self.pos
#         # 用于血条特效的显示
#         self.health_value_show = Write(f"100")
#         self.show_mode = show_mode
#         # 用于攻击状态的蓄力显示
#         self.attack_len = 0
#         self.attack_speed = 0
#         self.attack_set_len = 200
#         self.attack_set_area = [160, attack_set_area]
#         self.attack_area = random.randint(20, 160)
#         self.attack_area = [self.attack_area, self.attack_area + self.attack_set_area[1]]
#         # 用于连击状态的显示
#         self.continue_set_max_num = 20
#         self.continue_set_max_time = 20
#         self.continue_num = 0
#         self.continue_time = 0
#         self.continue_num_show = Write(f"当前连击数：0", color=cfg2.color_black, font=cfg2.font_path2, size=30)
#         # 用于表示攻击后的打断时间
#         self.get_attack_sleep = 5
#
#     # todo:人物动画特效动画
#     def update(self):
#         """根据人物的状态更新人物的属性"""
#         if self.get_attack_sleep > 0:
#             self.get_attack_sleep -= 1
#             return
#         if self.value.get_mode() == "attack":
#             self.attack_len += self.attack_speed
#         if self.value.get_mode() == "shield":
#             self.attack_len = 0
#             self.attack_speed = 0
#             self.continue_num = 0
#             self.continue_time = 0
#         if self.value.get_mode() == "continue":
#             self.continue_time -= 1
#             if self.continue_time == 0:
#                 self.continue_num = 0
#                 self.value.set_mode_attack()
#                 self.attack_speed = 0
#
#     # todo:完善子弹类，并进行补足
#     def attack(self):
#         """根据人物的状态发动攻击"""
#         if self.value.get_mode() == "attack":
#             # 判断是否处于连击状态
#             if (self.attack_len > self.attack_area[0]) and (self.attack_len < self.attack_area[1]):
#                 self.value.set_mode_continue()
#                 health = int(self.value.get_basic()[1] * self.value.get_kis()[1])
#                 self.attack_len = 0
#                 self.attack_area = random.randint(20, 160)
#                 self.attack_area = [self.attack_area, self.attack_area + self.attack_set_area[1]]
#                 self.continue_time = self.continue_set_max_time
#                 pygame.mixer.Sound.play(cfg2.sound2)
#                 return self._attack_push(health=health, mode=0)
#             else:
#                 kis = self.attack_len / 50
#                 health = int(self.value.get_kis()[1] * kis)
#                 self.attack_len = 0
#                 pygame.mixer.Sound.play(cfg2.sound1)
#                 return self._attack_push(health=health, mode=0)
#         else:
#             self.continue_time = self.continue_set_max_time
#             self.continue_num += 1
#             if self.continue_num == self.continue_set_max_num:
#                 self.continue_num = 0
#                 self.continue_time = 0
#                 self.value.set_mode_attack()
#                 self.attack_speed = 0
#             health = int(self.value.get_basic()[1] * self.value.get_kis()[1])
#             return self._attack_push(health=health, mode=1)
#
#     def attack_get(self, bullet):
#         if self.value.get_mode() == "shield":
#             pygame.mixer.Sound.play(cfg2.sound3)
#             pass
#         else:
#             pygame.mixer.Sound.play(cfg2.sound4)
#             bu = bullet.get_value()
#             health = bu.get_health()
#             print(health)
#             health_now = self.value.get_basic()[0] - health / self.value.get_kis()[0]
#             print(self.value.get_kis()[0])
#             print(health_now)
#             self.value.set_health(self.value.get_basic()[0] - health / self.value.get_kis()[0])
#             # print("Attack")
#
#     def draw(self, screen):
#         self.draw_health(screen)
#         self.draw_shield(screen)
#         self.draw_attack(screen)
#         self.draw_continue(screen)
#
#     def draw1(self, screen):
#         self.draw_health(screen)
#         self.draw_shield(screen)
#
#     def draw_health(self, screen):
#         health = self.value.get_basic()[0]
#         pygame.draw.rect(screen, cfg2.color_white180, [self.pos[0] + 120, self.pos[1] - 350, 100, 15], 0)
#         pygame.draw.rect(screen, cfg2.color_white, [self.pos[0] + 120, self.pos[1] - 350, health, 15], 0)
#         pygame.draw.rect(screen, cfg2.color_black, [self.pos[0] + 120, self.pos[1] - 350, 100, 15], 2)
#         self.health_value_show.setting(text_in="{:.2f}".format(health))
#         self.health_value_show.show((self.pos[0] + 120, self.pos[1] - 380), screen)
#
#     def draw_shield(self, screen):
#         """当角色处于防御状态时，依据朝向来绘制护盾"""
#         if self.value.get_mode() == "shield":
#             if self.show_mode == 0:
#                 pygame.draw.rect(screen, cfg2.color_black, [self.pos[0] + 180, self.pos[1] - 250, 3, 200], 0)
#             if self.show_mode == 1:
#                 pygame.draw.rect(screen, cfg2.color_black, [self.pos[0] - 20, self.pos[1] - 250, 3, 200], 0)
#
#     def draw_attack(self, screen):
#         if self.value.get_mode() == "attack":
#             pygame.draw.rect(screen, cfg2.color_white80, [300, 450, 200, 30], 0)
#             pygame.draw.rect(screen, "yellow",
#                              [300 + self.attack_area[0], 450, self.attack_area[1] - self.attack_area[0], 30], 0)
#             pygame.draw.rect(screen, cfg2.color_white, [300, 450, self.attack_len, 30], 0)
#             pygame.draw.rect(screen, cfg2.color_black, [300, 450, 200, 30], 2)
#
#     def draw_continue(self, screen):
#         if self.value.get_mode() == "continue":
#             pygame.draw.rect(screen, cfg2.color_white80, [300, 100, 200, 10], 2)
#             pygame.draw.rect(screen, cfg2.color_white, [300, 100, self.continue_time * 10, 10], 0)
#             pygame.draw.rect(screen, cfg2.color_black, [300, 100, 200, 10], 2)
#             con_num = self.continue_num
#             self.continue_num_show.setting(f"当前连击数：{con_num}")
#             self.continue_num_show.show((300, 70), screen)
#
#     def is_event(self, event: pygame.event):
#         """根据pygame.event对人物状态进行更新，返回攻击或者None"""
#         """
#         鼠标左键按下时，若处于攻击状态，进行蓄力
#         鼠标左键抬起时，若不处于防御状态，发动攻击（攻击状态根据蓄力情况发动攻击）（联机状态直接攻击）
#         鼠标右键按下时，若不处于连击状态，切换为防御状态
#         鼠标右键抬起时，若处于防御状态，切换为攻击状态
#         """
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             # 鼠标左键按下且处于攻击状态
#             if self.value.get_mode() == "attack":
#                 self.attack_speed = 4
#         elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
#             # 鼠标左键弹起且不处于防御状态
#             if self.value.get_mode() != "shield":
#                 self.attack_speed = 0
#                 return self.attack()
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
#             # 鼠标右键按下且处于攻击状态
#             if self.value.get_mode() == "attack":
#                 self.value.set_mode_shield()
#         elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
#             # 鼠标右键弹起且处于防御状态
#             if self.value.get_mode() == "shield":
#                 self.value.set_mode_attack()
#         return None
#
#     def push_attack(self, health, mode):
#         pygame.mixer.Sound.play(cfg2.sound1)
#         if mode == 0:
#             image1 = cfg2.image_ak1
#             image01 = cfg2.image_ak01
#         else:
#             image1 = cfg2.image_ak2
#             image01 = cfg2.image_ak02
#         if self.show_mode == 0:
#             return Bullet(pl_name=self.value.get_name(), health=health,
#                           bu_image=image1, bu_move=[10, 0],
#                           bu_pos=(self.pos[0] + 200, self.pos[1] - 200))
#         else:
#             return Bullet(pl_name=self.value.get_name(), health=health,
#                           bu_image=image01, bu_move=[-10, 0],
#                           bu_pos=(self.pos[0] - 20, self.pos[1] - 200))
#
#     def mode_change(self, int):
#         if int == 0:
#             pass
#         elif int == 1:
#             self.value.set_mode_attack()
#         elif int == 2:
#             self.value.set_mode_shield()
#         else:
#             self.value.set_mode_continue()
#
#     def get_mode(self):
#         return self.value.get_mode()
#
#     def _attack_push(self, health, mode=0):
#         if mode == 0:
#             image1 = cfg2.image_ak1
#             image01 = cfg2.image_ak01
#         else:
#             image1 = cfg2.image_ak2
#             image01 = cfg2.image_ak2
#         if self.show_mode == 0:
#             return Bullet(pl_name=self.value.get_name(), health=health,
#                           bu_image=image1, bu_move=[10, 0],
#                           bu_pos=(self.pos[0] + 200, self.pos[1] - 200))
#         else:
#             return Bullet(pl_name=self.value.get_name(), health=health,
#                           bu_image=image01, bu_move=[-10, 0],
#                           bu_pos=(self.pos[0] - 20, self.pos[1] - 200))
#
#     def is_die(self):
#         if self.value.get_basic()[0] <= 0:
#             pygame.mixer.Sound.play(cfg2.sound5)
#             return True
#         return False
#
#
# class Plot(object):
#     """进行一幕剧情的绘制和显示"""
#     # todo:优化剧情的操作与显示
#     #  分析：剧情元素有背景、人物、文案（但是背景往往应该最开始的时候铺设）
#     # todo:对于单个剧情
#     #  元素的绘制：背景与其他分开绘制，
#     #  剧情应当有寿命：文案播放完毕或者动画显示完毕或者跳过(需要一个全局参数)或者选择做完
#     #  感觉抽象的不够彻底，看看能不能将功能再拆分
#     # todo:对于多个剧情（分支或者继承关系不进行考虑），应当在剧情元素中的按钮子元素中完成
#     # todo:关于显示，
#     #  关于文案显示：分为背景文案显示，分为对话文案显示
#     #               两者的区别：前者仅显示文案，后者需显示讲话者，并且文案要在屏幕的下面显示，要有对话框
#     #  关于图像的显示：人物与物体图像，图像的行动（每一幕需要传入图像列表，传入图像列表的行为）
#     #  关于音效的显示：音效的特殊显示--》（传入音乐素材，传入播放条件（剧情的寿命或者循环矩阵））
#     #  关于选择：定义各种局外函数（Plot类的类函数，战斗界面与其他界面的转入）（按钮列表，按钮是固定的）
#     #  关于剧情的行动的先后，定义一个根据剧情的寿命或者寿命参数的外部函数，直接传入？（是否可以调用实例内部的属性）
#
#     """基础文本参数"""
#     font_all = cfg2.font_path3
#     size_all = 20
#     color_all = cfg2.color_white
#     """基础文本坐标参数"""
#     text_name_pos_all = (30, 400)
#     text_show_pos_all = (100, 400)
#
#     plot_number_all = 0
#
#     def __init__(self, text_in="", text_mode=0, text_color=color_all, text_font=font_all, text_size=size_all,
#                  image_list: list[str] = None, image_list_pos: list[list[tuple]] = None,
#                  music_list: list[str] = None, music_list_pos: list[list[int]] = None,
#                  image_bg: str = None, image_bg_pos: tuple = (0, 100),
#                  button_list: list[Button] = None, plot_mode=0):
#         """
#         文案、文案类型
#         图像列表、图像行为列表
#         音效列表、音效行为列表
#         按钮列表
#         寿命函数
#         """
#         """文本参数"""
#         self.text_size = text_size
#         self.text_font = text_font
#         self.text = text_in
#         self.text_color = text_color
#         self.text_mode = text_mode
#         """图像参数"""
#         self.image_list = image_list
#         self.image_list_pos = image_list_pos
#         self.image_bg = image_bg
#         self.image_bg_pos = image_bg_pos
#         """音乐参数"""
#         self.music_list = music_list
#         self.music_list_pos = music_list_pos
#         """按钮参数"""
#         self.button_list = button_list
#         """原始参数进行处理，预备显示"""
#         self.text_show = None
#         self.text_name = None
#         self.image_show = None
#         self.image_bg_show = None
#         self.music_show = None
#         """寿命函数，控制一个剧情的发展"""
#         self.age = 0
#         self.age_key = False
#         self._text_show_adjust()
#         self._image_show_adjust()
#
#     def set_text(self, text_in="", text_mode=0, text_color=color_all, text_font=font_all, text_size=size_all):
#         """文本参数"""
#         self.text_size = text_size
#         self.text_font = text_font
#         self.text = text_in
#         self.text_color = text_color
#         self.text_mode = text_mode
#         """寿命函数，控制一个剧情的发展"""
#         self.age = 0
#         self.age_key = False
#         self._text_show_adjust()
#
#     def set_image(self, image_list: list[str] = None, image_list_pos: list[tuple] = None,
#                   image_bg: str = None, image_bg_pos: tuple = (0, 100)):
#         """图像参数"""
#         self.image_list = image_list
#         self.image_list_pos = image_list_pos
#         self.image_bg = image_bg
#         self.image_bg_pos = image_bg_pos
#         """寿命函数，控制一个剧情的发展"""
#         self.age = 0
#         self.age_key = False
#         self._image_show_adjust()
#
#     def set_music(self):
#         """寿命函数，控制一个剧情的发展"""
#         self.age = 0
#         self.age_key = False
#
#     def set_button(self, button_list: list[Button] = None):
#         """按钮参数"""
#         self.button_list = button_list
#         """寿命函数，控制一个剧情的发展"""
#         self.age = 0
#         self.age_key = False
#
#     def _text_show_adjust(self):
#         """文本分为环境文本与对话文本"""
#         self.text_show = None
#         self.text_name = None
#         # 对话文本
#         if self.text_mode == 1:
#             self.text_name, self.text = self.text.split("：")[0], self.text.split("：")[1]
#             self.text_name = Write(self.text_name, self.text_color, self.text_font, self.text_size)
#             self.text_show = Paragraph(self.text, self.text_color, self.text_font, self.text_size)
#         if self.text_mode == 2:
#             self.text_show = Paragraph(self.text, self.text_color, self.text_font, self.text_size)
#
#     def _image_show_adjust(self):
#         self.image_show = None
#         self.image_bg_show = None
#         if self.image_list is not None:
#             length = len(self.image_list)
#             if length == 0:
#                 return
#             self.image_show = []
#             for i in range(length):
#                 self.image_show.append(Image(self.image_list[i]))
#         if self.image_bg is not None:
#             self.image_bg_show = Image(self.image_bg)
#
#     def _music_show_adjust(self):
#         # raise NotImplementedError
#         self.music_show = None
#         return
#
#     def show(self, screen):
#         """依据剧情寿命展现不同效果"""
#         """
#         寿命为0，打字机效果
#         寿命为1，无影响，文本直接显示
#         寿命为2，无影响
#         寿命为3，全部结束
#         """
#         # self.show_bg(screen)
#         self.show_image(screen)
#         self.show_text(screen)
#         self.show_button()
#
#     def show_button(self):
#         if self.button_list is not None:
#             for i in range(len(self.button_list)):
#                 self.button_list[i].show()
#
#     def show_bg(self, screen):
#         self.image_bg_show.show(self.image_bg_pos, screen)
#
#     def show_text(self, screen, text_name_pos=text_name_pos_all, text_show_pos=text_show_pos_all):
#         if self.age == 0:
#             if self.text_mode == 1:
#                 pygame.draw.rect(screen, color=cfg2.color_white, rect=[10, 390, 780, 200], width=2)
#                 self.text_name.show(text_name_pos, screen)
#                 self.text_show.show_slow(text_show_pos, screen)
#                 if self.text_show.is_show_all():
#                     self.age = 2
#             if self.text_mode == 2:
#                 self.text_show.show_slow(text_show_pos, screen)
#                 if self.text_show.is_show_all():
#                     self.age = 2
#         if self.age == 2:
#             if self.text_mode == 1:
#                 pygame.draw.rect(screen, color=cfg2.color_white, rect=[10, 390, 780, 200], width=2)
#                 self.text_name.show(text_name_pos, screen)
#                 self.text_show.show_all(text_show_pos, screen)
#             if self.text_mode == 2 or self.text_mode == 3:
#                 self.text_show.show_all(text_show_pos, screen)
#
#     def show_image(self, screen):
#         if self.image_show is not None:
#             for i in range(len(self.image_show)):
#                 self.image_show[i].show(self.image_list_pos[i], screen)
#
#     def is_event(self, event):
#         if self.button_list is None:
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 if self.age == 2:
#                     self.age = 3
#                 else:
#                     self.age = 2
#         else:
#             for i in range(len(self.button_list)):
#                 self.age_key = self.button_list[i].update(event)
#
#     def is_die(self):
#         if self.age == 3:
#             return True
#         return False
#
#
# class BulletValue(object):
#     """用于储存攻击的数值"""
#
#     def __init__(self, pl_name="", health=0, mode="", buff=None):
#         """攻击的发起者，攻击的数值，攻击的类型，攻击附带的buff"""
#         self.pl_name = pl_name
#         self.health = health
#         self.mode = mode
#         self.buff = buff
#
#     def setting(self, pl_name="", health=0, mode="", buff=None):
#         """攻击的发起者，攻击的数值，攻击的类型，攻击附带的buff"""
#         self.pl_name = pl_name
#         self.health = health
#         self.mode = mode
#         self.buff = buff
#
#     def get_name(self):
#         return self.pl_name
#
#     def get_health(self):
#         return self.health
#
#     def get_mode(self):
#         return self.mode
#
#     def get_buff(self):
#         return self.buff
#
#     def set_name(self, pl_name):
#         self.pl_name = pl_name
#
#     def set_health(self, health):
#         self.health = health
#
#     def set_mode(self, mode):
#         self.mode = mode
#
#     def set_buff(self, buff=None):
#         self.buff = buff
#
#
# class Bullet(pygame.sprite.Sprite):
#     """角色攻击的可视化与角色间战斗的属性传递"""
#
#     # todo:子弹的显示与数值的传递问题
#     # todo:子弹的显示：图像、移动方式
#     #       产生条件为发动攻击，消失条件为触碰角色消失，（利用精灵组与精灵类实现）
#     # todo:关于数值的传递问题
#     #       攻击的发起者，攻击的类型，攻击的buff，攻击的数值
#     def __init__(self, pl_name="", health=0, mode="", buff=None,
#                  bu_image="", bu_move=None, bu_pos=None):
#         """
#         攻击的属性：发起者、数值、种类、buff
#         子弹的属性：图像、运动轨迹、起始位置
#         """
#         super().__init__()
#         # 储存数值
#         self.value = BulletValue(pl_name=pl_name, health=health, mode=mode, buff=buff)
#         # 用于精灵类的绘制
#         self.image = pygame.image.load(bu_image)
#         self.rect = self.image.get_rect()
#         self.pos = bu_pos
#         self.rect.center = self.pos
#         self.speed = bu_move
#
#     def update(self):
#         self.rect.x += self.speed[0]
#         self.rect.y += self.speed[1]
#
#     def get_name(self):
#         return self.value.get_name()
#
#     def get_value(self):
#         return self.value
# import pygame
# pygame.init()
#
# # This file contains font, music, color, image, func which to get the true resource by number
# ##
# # 字体
# # 1为花体字
# # 2为粗体字
# # 3为宋体字
# font_path1 = "resource/font/FZSTK.TTF"
# font_path2 = "resource/font/STHUPO.TTF"
# font_path3 = "resource/font/STZHONGS.TTF"
# story_font_size = 20
# title_font_size = 30
# choose_font_size = 20
# game_font_size = 50
#
# ##
# # 音效
# music_path1 = "resource/music/命中.mp3"
# music_path2 = "resource/music/命中2.mp3"
# music_path3 = "resource/music/格挡.mp3"
# music_path4 = "resource/music/格挡2.mp3"
# music_path5 = "resource/music/死亡.mp3"
# sound1 = pygame.mixer.Sound(music_path1)
# sound2 = pygame.mixer.Sound(music_path2)
# sound3 = pygame.mixer.Sound(music_path3)
# sound4 = pygame.mixer.Sound(music_path4)
# sound5 = pygame.mixer.Sound(music_path5)
#
# ##
# # 颜色
# color_white = (255, 255, 255)
# color_white10 = (10, 10, 10)
# color_white20 = (20, 20, 20)
# color_white30 = (30, 30, 30)
# color_white40 = (40, 40, 40)
# color_white50 = (50, 50, 50)
# color_white60 = (60, 60, 60)
# color_white70 = (70, 70, 70)
# color_white80 = (80, 80, 80)
# color_white90 = (90, 90, 90)
# color_white100 = (100, 100, 100)
# color_white110 = (110, 110, 110)
# color_white120 = (120, 120, 120)
# color_white130 = (130, 130, 130)
# color_white140 = (140, 140, 140)
# color_white150 = (150, 150, 150)
# color_white160 = (160, 160, 160)
# color_white170 = (170, 170, 170)
# color_white180 = (180, 180, 180)
# color_white190 = (190, 190, 190)
# color_white200 = (200, 200, 200)
# color_white210 = (210, 210, 210)
# color_white220 = (220, 220, 220)
# color_white230 = (230, 230, 230)
# color_white240 = (240, 240, 240)
# color_white250 = (250, 250, 250)
# color_black = (0, 0, 0)
# color_red = (255, 0, 0)
# color_green = (0, 255, 0)
# color_blue = (0, 0, 255)
# color_choose1 = "darkorange"
# color_choose2 = "darkorange"
# color_choose3 = "darkorange"
# color_choose4 = "darkorange"
# color_choose5 = "darkorange"
# color_choose6 = "darkorange"
# color_choose7 = "darkorange"
# color_choose8 = "darkorange"
# color_choose9 = "darkorange"
# ##
# # 图片素材
#
# # 背景图片
# image_kg1 = "resource/picture/背景（结局一）.png"
# image_kg2 = "resource/picture/背景（决战）.png"
# image_kg3 = "resource/picture/背景（出山）.png"
# image_kg4 = "resource/picture/背景（大雪）.png"
# image_kg5 = "resource/picture/背景（对战）.png"
# image_kg6 = "resource/picture/背景（灭门）.png"
# image_kg7 = "resource/picture/背景（窃取）.png"
# image_kg8 = "resource/picture/背景（结局一）.png"
# image_kg9 = "resource/picture/背景（结局二）.png"
# image_kg10 = "resource/picture/背景（结局三）.png"
# image_kg11 = "resource/picture/背景2.jpg"
# image_kg01 = "resource/picture/背景1（自由替换勿改文件名).png"
# image_kg02 = "resource/picture/背景2（自由替换勿改文件名).png"
# image_kg03 = "resource/picture/背景3（自由替换勿改文件名).png"
# image_kg04 = "resource/picture/背景4（自由替换勿改文件名).png"
# image_kg05 = "resource/picture/背景5（自由替换勿改文件名).png"
# image_kg06 = "resource/picture/背景6（自由替换勿改文件名).png"
# image_kg07 = "resource/picture/背景7（自由替换勿改文件名).png"
# image_kg08 = "resource/picture/背景8（自由替换勿改文件名).png"
# image_kg09 = "resource/picture/背景9（自由替换勿改文件名).png"
# image_kg010 = "resource/picture/背景10（自由替换勿改文件名).png"
#
# # 人物图片
# image_pl1 = "resource/picture/人物（少年1）.png"
# image_pl2 = "resource/picture/人物（少年出山1）.png"
# image_pl3 = "resource/picture/人物（师傅1）.png"
# image_pl4 = "resource/picture/人物（师兄1）.png"
# image_pl5 = "resource/picture/人物（反派2）(已去底).png"
# image_pl6 = "resource/picture/人物（反派3）(已去底).png"
# image_pl7 = "resource/picture/人物（反派4）(已去底).png"
# image_pl8 = "resource/picture/人物（反派5）(已去底).png"
# image_pl9 = "resource/picture/人物（女助理）.png"
# image_pl10 = "resource/picture/人物（女助理）.png"
# image_pl11 = "resource/picture/人物（守卫）.png"
# image_pl12 = "resource/picture/人物（景凤）.png"
# image_pl13 = "resource/picture/人物（法贾）.png"
# image_pl14 = "resource/picture/人物（西装男子）.png"
# image_pl15 = "resource/picture/人物（黑木弟子）.png"
# image_pl16 = "resource/picture/人物（黑木）.png"
# image_pl17 = "resource/picture/人物（女助理）.png"
# image_pl18 = "resource/picture/人物（女助理）.png"
# image_pl19 = "resource/picture/人物（女助理）.png"
# image_pl20 = "resource/picture/人物（女助理）.png"
# image_pl01 = "resource/picture/人物1（自由替换勿改文件名).png"
# image_pl02 = "resource/picture/人物2（自由替换勿改文件名).png"
# image_pl03 = "resource/picture/人物3（自由替换勿改文件名).png"
# image_pl04 = "resource/picture/人物4（自由替换勿改文件名).png"
# image_pl05 = "resource/picture/人物5（自由替换勿改文件名).png"
# image_pl06 = "resource/picture/人物6（自由替换勿改文件名).png"
# image_pl07 = "resource/picture/人物7（自由替换勿改文件名).png"
# image_pl08 = "resource/picture/人物8（自由替换勿改文件名).png"
# image_pl09 = "resource/picture/人物9（自由替换勿改文件名).png"
# image_pl010 = "resource/picture/人物10（自由替换勿改文件名).png"
# # 道具图片（依次为玉佩暗、玉佩亮、线索）
# image_th1 = "resource/picture/道具（暗1）.png"
# image_th2 = "resource/picture/道具（亮1）.png"
# image_th3 = "resource/picture/道具（线索1）.png"
# # 攻击特效
# image_ak1 = "resource/picture/攻击1.png"
# image_ak2 = "resource/picture/攻击2.png"
# image_ak3 = "resource/picture/攻击3.png"
# image_ak01 = "resource/picture/攻击01.png"
# image_ak02 = "resource/picture/攻击02.png"
# image_ak03 = "resource/picture/攻击03.png"
#
# ##
# # 剧情
#
#
# # 文案：储存在"resource/font/text1.txt"等
# # 剧情读取函数
# def text_ch1(filename=""):
#     if filename == "":
#         return None
#     file_chapter1 = open(filename, mode="r", encoding="utf-8")
#     text_chapter1 = []
#     text_swap = []
#     for lines in file_chapter1.readlines():
#         if lines[1] == "#":
#             text_chapter1.append(text_swap)
#             text_swap = []
#         else:
#             text_swap.append(lines)
#     text_chapter1.append(text_swap)
#     return text_chapter1
#
#
# # 图片素材位置参数：储存在"resource/font/image1.txt"等
# # 图片素材位置参数读取函数
# def image_ch1(filename=""):
#     if filename == "":
#         return None
#     file_chapter1 = open(filename, mode="r", encoding="utf-8")
#     image_chapter1 = []
#     image_swap = []
#     for lines in file_chapter1.readlines():
#         if lines[0] == "#":
#             image_chapter1.append(image_swap)
#             image_swap = []
#         else:
#             image_chapter1.append(lines)
#     return image_chapter1
#
#
# # 根据编号对应得到素材
# # 背景图片获取
# def get_bg_image(num):
#     if num == 1:
#         return image_kg1
#     if num == 2:
#         return image_kg2
#     if num == 3:
#         return image_kg3
#     if num == 4:
#         return image_kg4
#     if num == 5:
#         return image_kg5
#     if num == 6:
#         return image_kg6
#     if num == 7:
#         return image_kg7
#     if num == 8:
#         return image_kg8
#     if num == 9:
#         return image_kg9
#     if num == 10:
#         return image_kg10
#     if num == 11:
#         return image_kg11
#     if num == 101:
#         return image_kg01
#     if num == 102:
#         return image_kg02
#     if num == 103:
#         return image_kg03
#     if num == 104:
#         return image_kg04
#     if num == 105:
#         return image_kg05
#     if num == 106:
#         return image_kg06
#     if num == 107:
#         return image_kg07
#     if num == 108:
#         return image_kg08
#     if num == 109:
#         return image_kg09
#     if num == 110:
#         return image_kg10
#
#
# # 人物图片获取
# def get_pl_image(num):
#     if num == 1:
#         return image_pl1
#     if num == 2:
#         return image_pl2
#     if num == 3:
#         return image_pl3
#     if num == 4:
#         return image_pl4
#     if num == 5:
#         return image_pl5
#     if num == 6:
#         return image_pl6
#     if num == 7:
#         return image_pl7
#     if num == 8:
#         return image_pl8
#     if num == 9:
#         return image_pl9
#     if num == 10:
#         return image_pl10
#     if num == 11:
#         return image_pl11
#     if num == 12:
#         return image_pl12
#     if num == 13:
#         return image_pl13
#     if num == 14:
#         return image_pl14
#     if num == 15:
#         return image_pl15
#     if num == 16:
#         return image_pl16
#     if num == 17:
#         return image_pl17
#     if num == 18:
#         return image_pl18
#     if num == 19:
#         return image_pl19
#     if num == 20:
#         return image_pl20
#     if num == 101:
#         return image_pl01
#     if num == 102:
#         return image_pl02
#     if num == 103:
#         return image_pl03
#     if num == 104:
#         return image_pl04
#     if num == 105:
#         return image_pl05
#     if num == 106:
#         return image_pl06
#     if num == 107:
#         return image_pl07
#     if num == 108:
#         return image_pl08
#     if num == 109:
#         return image_pl09
#     if num == 110:
#         return image_pl10
#
# ##
# # 游戏主要参数
#
#
# game_name = "蓝桥榜"
# title_name = "贺新岁"
# screen_size = (800, 600)
#
# ##
# # 重要元素位置参数
# pos_title_button = (325, 100)
# pos_return_button = (50, 50)
# pos_choose1_button = (340, 300)
# pos_choose2_button = (50, 50)
# pos_set_button = (670, 20)
# pos_start_button = (340, 300)
# pos_mean_button = (340, 350)
# pos_gift_button = (730, 20)
#
# pos_pl = [(1000, 1000)]
# for i in range(10, 60):
#     pos_pl.append((i * 10, 200))
#
# ##
# # 兑换码
# # 兑换码信息储存
# gift1_password = ["ccnu1024", "CCNU1024"]
# gift2_password = ["ccnu1024", "CCNU1024"]
# gift3_password = ["ccnu1024", "CCNU1024"]
# gift4_password = ["ccnu1024", "CCNU1024"]
# gift5_password = ["ccnu1024", "CCNU1024"]
# # 兑换码状态储存
# gift1_pass = False
# gift2_pass = False
# gift3_pass = False
# gift4_pass = False
# gift5_pass = False
#
# import cfg
# import cfg2
# from cfg import *
# from cfg2 import *
# import meaning_surface
# import choose_surface
# import gift_surface
# import setting_surface
#
#
# def show():
#     # 相关素材绘制
#     screen.fill(cfg2.color_black)
#     background.show((400, 280), screen, mode=4)
#     title_button.show()
#     start_button.show()
#     mean_button.show()
#     gife_button.show()
#
#
# def is_event(event):
#     # 相关事件判定
#     start_button.update(event)
#     mean_button.update(event)
#     gife_button.update(event)
#
#
# def func1():
#     mean_surface.main()
#
#
# def func2():
#     choose_surface.main()
#
# def func3():
#     gife_surface.main()
#
#
# def main():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
#                 is_event(event)
#         show()
#         pygame.display.flip()
#         clock.tick(60)
#
#
# # 相关背景素材设置
# pygame.init()
# screen = pygame.display.set_mode(cfg2.screen_size)
# pygame.display.set_caption(cfg2.title_name)
# start_button = Button(screen, (340, 300),
#                       text_in="游戏开始", text_color=cfg2.color_red,
#                       text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
#                       fill_color=False, edge_color=True, size=(124, 34),
#                       call_function=func2)
# title_button = Button(screen, (325, 100),
#                       text_in="蓝桥榜", text_color=cfg2.color_red,
#                       text_font=cfg2.font_path2, text_size=cfg2.game_font_size,
#                       fill_color=False, edge_color=True, size=(154, 54))
# mean_button = Button(screen, (340, 350),
#                      text_in="游戏说明", text_color=cfg2.color_red,
#                      text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
#                      fill_color=False, edge_color=True, size=(124, 34),
#                      call_function=func1)
# gife_button = Button(screen, (730, 20),
#                      text_in="兑", text_color=cfg2.color_red,
#                      text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
#                      fill_color=True, edge_color=True, size=(34, 34),
#                      call_function=func3)
# clock = pygame.time.Clock()
# background = Image(path=cfg2.image_kg9)
#
#
# if __name__ == '__main__':
#     main()
#
#
# from cfg import *
# from cfg2 import *
# import meaning_surface
# import choose_surface
# import gift_surface
# import setting_surface
#
#
# def is_event(event):
#     # 相关事件判定
#     global start_button
#     global meaning_button
#     global gift_button
#     global setting_button
#     if title_button is not None:
#         start_button.update(event)
#         meaning_button.update(event)
#         gift_button.update(event)
#         setting_button.update(event)
#
# def show():
#     global screen
#     global title_button
#     global start_button
#     global meaning_button
#     global gift_button
#     global setting_button
#     global background
#     screen.fill(cfg2.color_black)
#     background.show((400, 280), screen, mode=4)
#     title_button.show()
#     start_button.show()
#     meaning_button.show()
#     gift_button.show()
#     setting_button.show()
#
#
# def func_start():
#     meaning_surface.main()
#
# def func_meaning():
#     print("2")
#
# def func_gift():
#     print("3")
#
# def func_setting():
#     print("4")
#
#
# def setting_first():
#     global screen
#     global title_button
#     global start_button
#     global meaning_button
#     global gift_button
#     global setting_button
#     global background
#     pygame.init()
#     screen = pygame.display.set_mode(cfg2.screen_size)
#     pygame.display.set_caption(cfg2.title_name)
#     title_button = Button(screen, cfg2.pos_title_button,
#                           text_in=cfg2.game_name, text_color=cfg2.color_red,
#                           text_font=cfg2.font_path2, text_size=cfg2.game_font_size,
#                           fill_color=False, edge_color=True, size=(154, 54))
#     start_button = Button(screen, cfg2.pos_start_button,
#                           text_in="游戏开始", text_color=cfg2.color_red,
#                           text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
#                           fill_color=False, edge_color=True, size=(124, 34),
#                           call_function=func_start())
#     meaning_button = Button(screen, cfg2.pos_mean_button,
#                             text_in="游戏说明", text_color=cfg2.color_red,
#                             text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
#                             fill_color=False, edge_color=True, size=(124, 34),
#                             call_function=func_meaning())
#     gift_button = Button(screen, cfg2.pos_gift_button,
#                          text_in="兑", text_color=cfg2.color_red,
#                          text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
#                          fill_color=True, edge_color=True, size=(34, 34),
#                          call_function=func_gift())
#     setting_button = Button(screen, cfg2.pos_set_button,
#                             text_in="设置", text_color=cfg2.color_red,
#                             text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
#                             fill_color=True, edge_color=True, size=(64, 34),
#                             call_function=func_setting())
#     background = Image(path=cfg2.image_kg9)
#
#
# def main():
#     setting_first()
#     clock = pygame.time.Clock()
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
#                 # is_event(event)
#                 start_button.update(event)
#                 meaning_button.update(event)
#                 gift_button.update(event)
#                 setting_button.update(event)
#         show()
#         pygame.display.flip()
#         clock.tick(60)
#
#
# screen = None
# title_button = None
# start_button = None
# meaning_button = None
# gift_button = None
# setting_button = None
# background = None
#
# if __name__ == '__main__':
#     main()
#
# # todo: 内嵌套函数start_surface.py
# """
# from cfg import *
# from cfg2 import *
# import meaning_surface
# import choose_surface
# import gift_surface
# import setting_surface
#
#
# def func_start():
#     meaning_surface.main()
#
#
# def func_meaning():
#     print("2")
#
#
# def func_gift():
#     print("3")
#
#
# def func_setting():
#     print("4")
#
#
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode(cfg2.screen_size)
#     pygame.display.set_caption(cfg2.title_name)
#     clock = pygame.time.Clock()
#     title_button = Button(screen, cfg2.pos_title_button,
#                           text_in=cfg2.game_name, text_color=cfg2.color_red,
#                           text_font=cfg2.font_path2, text_size=cfg2.game_font_size,
#                           fill_color=False, edge_color=True, size=(154, 54))
#     start_button = Button(screen, cfg2.pos_start_button,
#                           text_in="游戏开始", text_color=cfg2.color_red,
#                           text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
#                           fill_color=False, edge_color=True, size=(124, 34),
#                           call_function=func_start())
#     meaning_button = Button(screen, cfg2.pos_mean_button,
#                             text_in="游戏说明", text_color=cfg2.color_red,
#                             text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
#                             fill_color=False, edge_color=True, size=(124, 34),
#                             call_function=func_meaning())
#     gift_button = Button(screen, cfg2.pos_gift_button,
#                          text_in="兑", text_color=cfg2.color_red,
#                          text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
#                          fill_color=True, edge_color=True, size=(34, 34),
#                          call_function=func_gift())
#     setting_button = Button(screen, cfg2.pos_set_button,
#                             text_in="设置", text_color=cfg2.color_red,
#                             text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
#                             fill_color=True, edge_color=True, size=(64, 34),
#                             call_function=func_setting())
#     background = Image(path=cfg2.image_kg9)
#
#     def is_event(event):
#         start_button.update(event)
#         meaning_button.update(event)
#         gift_button.update(event)
#         setting_button.update(event)
#
#     def show():
#         screen.fill(cfg2.color_black)
#         background.show((400, 280), screen, mode=4)
#         title_button.show()
#         start_button.show()
#         meaning_button.show()
#         gift_button.show()
#         setting_button.show()
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
#                 is_event(event)
#         show()
#         pygame.display.flip()
#         clock.tick(60)
#
#
# if __name__ == '__main__':
#     main()
# """
# """
# gift_surface.py
# import pygame
#
# import cfg
# from cfg import *
#
#
#
#
# def func_return():
#     global running
#     running = False
#
#
#
#
# def main():
#     # 初始化
#     pygame.init()
#     screen = pygame.display.set_mode(cfg.screen_size)
#     pygame.display.set_caption(cfg.title_name)
#     clock = pygame.time.Clock()
#
#     # 相关背景素材设置
#     str1 = Write("请输入兑换码", color=color_white, font=cfg.font_path3, size=25)
#     str2 = Write("", color=color_white, font=cfg.font_path3, size=25)
#     str3 = Write("", color=color_white, font=cfg.font_path3, size=25)
#     return_button = Button(screen, cfg.pos_return_button,
#                            text_in="返回", text_font=cfg.font_path2, text_size=cfg.title_font_size,
#                            fill_color=False, edge_color=True, size=(64, 34),
#                            call_function=func_return)
#
#     def is_event(event):
#         # 相关事件判定
#         return_button.update(event)
#         global str_gife
#         global write_mode
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_0:
#                 if len(str_gife) < 12:
#                     str_gife += "0"
#             if event.key == pygame.K_1:
#                 if len(str_gife) < 12:
#                     str_gife += "1"
#             if event.key == pygame.K_2:
#                 if len(str_gife) < 12:
#                     str_gife += "2"
#             if event.key == pygame.K_3:
#                 if len(str_gife) < 12:
#                     str_gife += "3"
#             if event.key == pygame.K_4:
#                 if len(str_gife) < 12:
#                     str_gife += "4"
#             if event.key == pygame.K_5:
#                 if len(str_gife) < 12:
#                     str_gife += "5"
#             if event.key == pygame.K_6:
#                 if len(str_gife) < 12:
#                     str_gife += "6"
#             if event.key == pygame.K_7:
#                 if len(str_gife) < 12:
#                     str_gife += "7"
#             if event.key == pygame.K_8:
#                 if len(str_gife) < 12:
#                     str_gife += "8"
#             if event.key == pygame.K_9:
#                 if len(str_gife) < 12:
#                     str_gife += "9"
#             if event.key == pygame.K_a:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "A"
#                     else:
#                         str_gife += "a"
#             if event.key == pygame.K_b:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "B"
#                     else:
#                         str_gife += "b"
#             if event.key == pygame.K_c:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "C"
#                     else:
#                         str_gife += "c"
#             if event.key == pygame.K_d:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "D"
#                     else:
#                         str_gife += "d"
#             if event.key == pygame.K_e:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "E"
#                     else:
#                         str_gife += "e"
#             if event.key == pygame.K_f:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "F"
#                     else:
#                         str_gife += "f"
#             if event.key == pygame.K_g:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "G"
#                     else:
#                         str_gife += "g"
#             if event.key == pygame.K_h:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "H"
#                     else:
#                         str_gife += "h"
#             if event.key == pygame.K_i:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "I"
#                     else:
#                         str_gife += "i"
#             if event.key == pygame.K_j:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "J"
#                     else:
#                         str_gife += "j"
#             if event.key == pygame.K_k:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "K"
#                     else:
#                         str_gife += "k"
#             if event.key == pygame.K_l:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "L"
#                     else:
#                         str_gife += "l"
#             if event.key == pygame.K_m:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "M"
#                     else:
#                         str_gife += "m"
#             if event.key == pygame.K_n:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "N"
#                     else:
#                         str_gife += "n"
#             if event.key == pygame.K_o:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "O"
#                     else:
#                         str_gife += "o"
#             if event.key == pygame.K_p:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "P"
#                     else:
#                         str_gife += "p"
#             if event.key == pygame.K_q:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "Q"
#                     else:
#                         str_gife += "q"
#             if event.key == pygame.K_r:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "R"
#                     else:
#                         str_gife += "r"
#             if event.key == pygame.K_s:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "S"
#                     else:
#                         str_gife += "s"
#             if event.key == pygame.K_t:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "T"
#                     else:
#                         str_gife += "t"
#             if event.key == pygame.K_u:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "U"
#                     else:
#                         str_gife += "u"
#             if event.key == pygame.K_v:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "V"
#                     else:
#                         str_gife += "v"
#             if event.key == pygame.K_w:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "W"
#                     else:
#                         str_gife += "w"
#             if event.key == pygame.K_x:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "X"
#                     else:
#                         str_gife += "x"
#             if event.key == pygame.K_y:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "Y"
#                     else:
#                         str_gife += "y"
#             if event.key == pygame.K_z:
#                 if len(str_gife) < 12:
#                     if write_mode:
#                         str_gife += "Z"
#                     else:
#                         str_gife += "z"
#             if event.key == pygame.K_CAPSLOCK:
#                 write_mode = not write_mode
#             if event.key == pygame.K_BACKSPACE:
#                 if len(str_gife) > 0:
#                     str_gife = str_gife[:-1]
#             if event.key == pygame.K_RETURN:
#                 global enter_time
#                 enter_time = 200
#                 if str_gife in cfg.gife1_name:
#                     cfg.gife1_game = True
#                     str3.setting("兑换成功！\n 门卡一张")
#                     print(cfg.gife1_game)
#                 else:
#                     str3.setting("兑换失败！")
#                 str_gife = ""
#
#
#     def show():
#         global str_gife
#         global enter_time
#         # 相关素材绘制
#         screen.fill((180, 180, 180))
#         str2.setting(str_gife, color=color_black, font=cfg.font_path3, size=50)
#         pygame.draw.rect(screen, cfg.color_white, [200, 300, 400, 70], 2)
#         str1.show((400, 200), screen, mode=4)
#         str2.show((220, 300), screen)
#         if enter_time > 0:
#             enter_time -= 1
#             str3.set_color((250 - enter_time, 250 - enter_time, 250 - enter_time))
#             str3.show((400, 250), screen, mode=4)
#
#
#         global show_key
#         show_key += 1
#         show_key %= 60
#         if show_key > 30:
#             pygame.draw.rect(screen, cfg.color_white, [220 + str2.get_y(), 310, 2, 50], 0)
#
#         # 返回按钮
#         return_button.show()
#
#     global running
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
#                 is_event(event)
#         show()
#         pygame.display.flip()
#         clock.tick(60)
#
# running = True
# show_key = 0
# enter_time = 200
# write_mode = False
# str_gife = ""
#
# if __name__ == '__main__':
#     main()
#
#
# """
# from cfg import *
# from cfg2 import *
# sys.path.append("..")
# import chapter.ch1.ch1_surface
# import chapter.ch2.ch2_surface
# import chapter.ch3.ch3_surface
# import chapter.ch4.ch4_surface
# import chapter.ch5.ch5_surface
# import chapter.ch6.ch6_surface
#
#
# def show():
#     global mean
#     global mean_time
#     # 相关素材绘制
#     screen.fill(cfg2.color_black)
#     background.show((400, 280), screen, mode=4)
#     choose_button1.show()
#     choose_button2.show()
#     choose_button3.show()
#     choose_button4.show()
#     choose_button5.show()
#     choose_button6.show()
#     choose_button7.show()
#     return_button.show()
#     if mean:
#         if mean_time > 0:
#             str1.show((400, 400 + mean_time), screen, mode=4)
#             mean_time -= 1
#         else:
#             mean = False
#
#
# def is_event(event):
#     # 相关事件判定
#     choose_button1.update(event)
#     choose_button2.update(event)
#     choose_button3.update(event)
#     choose_button4.update(event)
#     choose_button5.update(event)
#     choose_button6.update(event)
#     choose_button7.update(event)
#     return_button.update(event)
#
#
# def func_return():
#     global running
#     running = False
#
#
# def func1():
#     global vector
#     if chapter1_surface.main():
#         vector[1] = 1
#
#
# def func2():
#     global vector
#     global mean
#     global mean_time
#     if vector[1] == 0:
#         global str1
#         str1.setting("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)
#         mean = True
#         mean_time = 120
#     else:
#         if chapter2_surface.main():
#             vector[2] = 1
#
#
# def func3():
#     global vector
#     global mean
#     global mean_time
#     if vector[2] == 0:
#         global str1
#         str1.setting("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)
#         mean = True
#         mean_time = 120
#     else:
#         if chapter3_surface.main():
#             vector[3] = 1
#
#
# def func4():
#     global vector
#     global mean
#     global mean_time
#     if vector[3] == 0:
#         global str1
#         str1.setting("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)
#         mean = True
#         mean_time = 120
#     else:
#         if chapter4_surface.main():
#             vector[4] = 1
#
#
# def func5():
#     global vector
#     global mean
#     global mean_time
#     if vector[4] == 0:
#         global str1
#         str1.setting("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)
#         mean = True
#         mean_time = 120
#     else:
#         if chapter5_surface.main():
#             vector[5] = 1
#
#
# def func6():
#     global vector
#     global mean
#     global mean_time
#     if vector[5] == 0:
#         global str1
#         str1.setting("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)
#         mean = True
#         mean_time = 120
#     else:
#         if chapter6_surface.main():
#             vector[6] = 1
#
#
# def func7():
#     global vector
#     global mean
#     global mean_time
#     global str1
#     if vector[6] == 0:
#         str1.setting(text_in="通关全部关卡以解锁", color=color_white, font=cfg2.font_path3, size=15)
#         mean = True
#         mean_time = 120
#     else:
#         chapter_show.main()
#
#
# def main():
#     global running
#     global vector
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
#                 is_event(event)
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     vector = [1 for i in range(10)]
#         print(vector)
#
#         show()
#         pygame.display.flip()
#         clock.tick(60)
#
#
# # 相关背景素材设置
# pygame.init()
# screen = pygame.display.set_mode(cfg2.screen_size)
# pygame.display.set_caption(cfg2.title_name)
# clock = pygame.time.Clock()
# vector = [0 for i in range(10)]
# vector[0] = 1
# running = True
# mean = False
# mean_time = 0
#
# background = Image(path=cfg2.image_kg2)
# str1 = Write("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)
# return_button = Button(screen, cfg2.pos_return_button,
#                        text_in="返回", text_font=cfg2.font_path2,
#                        text_color=cfg2.color_white, text_size=cfg2.title_font_size,
#                        fill_color=False, edge_color=True, size=(64, 34),
#                        call_function=func_return)
# height = 370
# weight = 150
# choose_button1 = Button(screen, (height, weight),
#                         text_in="序章", text_font=cfg2.font_path2,
#                         text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
#                         fill_color=True, edge_color=True, size=(64, 34),
#                         call_function=func1)
# choose_button2 = Button(screen, (height, weight + 50),
#                         text_in="贰章", text_font=cfg2.font_path2,
#                         text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
#                         fill_color=True, edge_color=True, size=(64, 34),
#                         call_function=func2)
# choose_button3 = Button(screen, (height, weight + 100),
#                         text_in="叁章", text_font=cfg2.font_path2,
#                         text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
#                         fill_color=True, edge_color=True, size=(64, 34),
#                         call_function=func3)
# choose_button4 = Button(screen, (height, weight + 150),
#                         text_in="肆章", text_font=cfg2.font_path2,
#                         text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
#                         fill_color=True, edge_color=True, size=(64, 34),
#                         call_function=func4)
# choose_button5 = Button(screen, (height, weight + 200),
#                         text_in="伍章", text_font=cfg2.font_path2,
#                         text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
#                         fill_color=True, edge_color=True, size=(64, 34),
#                         call_function=func5)
# choose_button6 = Button(screen, (height, weight + 250),
#                         text_in="终章", text_font=cfg2.font_path2,
#                         text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
#                         fill_color=True, edge_color=True, size=(64, 34),
#                         call_function=func6)
# choose_button7 = Button(screen, (700, 50),
#                         text_in="剧情", text_font=cfg2.font_path2,
#                         text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
#                         fill_color=True, edge_color=True, size=(64, 34),
#                         call_function=func7)
#
#
# if __name__ == '__main__':
#     main()
import cfg
from cfg import *
import ch1_choose1_surface
import ch1_flight1
import ch1_flight2

# todo:考虑使用链表操纵剧情展示
def get_bg_image(num):
    if num == 1:
        return cfg.image_kg1
    if num == 2:
        return cfg.image_kg2
    if num == 3:
        return cfg.image_kg3
    if num == 4:
        return cfg.image_kg4
    if num == 5:
        return cfg.image_kg5
    if num == 6:
        return cfg.image_kg6
    if num == 7:
        return cfg.image_kg7
    if num == 8:
        return cfg.image_kg8
    if num == 9:
        return cfg.image_kg9
    if num == 10:
        return cfg.image_kg10
    if num == 11:
        return cfg.image_kg11
    if num == 101:
        return cfg.image_kg01
    if num == 102:
        return cfg.image_kg02
    if num == 103:
        return cfg.image_kg03
    if num == 104:
        return cfg.image_kg04
    if num == 105:
        return cfg.image_kg05
    if num == 106:
        return cfg.image_kg06
    if num == 107:
        return cfg.image_kg07
    if num == 108:
        return cfg.image_kg08
    if num == 109:
        return cfg.image_kg09
    if num == 110:
        return cfg.image_kg10


def get_pl_image(num):
    if num == 1:
        return cfg.image_pl1
    if num == 2:
        return cfg.image_pl2
    if num == 3:
        return cfg.image_pl3
    if num == 4:
        return cfg.image_pl4
    if num == 5:
        return cfg.image_pl5
    if num == 6:
        return cfg.image_pl6
    if num == 7:
        return cfg.image_pl7
    if num == 8:
        return cfg.image_pl8
    if num == 9:
        return cfg.image_pl9
    if num == 10:
        return cfg.image_pl10
    if num == 11:
        return cfg.image_pl11
    if num == 12:
        return cfg.image_pl12
    if num == 13:
        return cfg.image_pl13
    if num == 14:
        return cfg.image_pl14
    if num == 15:
        return cfg.image_pl15
    if num == 16:
        return cfg.image_pl16
    if num == 17:
        return cfg.image_pl17
    if num == 18:
        return cfg.image_pl18
    if num == 19:
        return cfg.image_pl19
    if num == 20:
        return cfg.image_pl20
    if num == 101:
        return cfg.image_pl01
    if num == 102:
        return cfg.image_pl02
    if num == 103:
        return cfg.image_pl03
    if num == 104:
        return cfg.image_pl04
    if num == 105:
        return cfg.image_pl05
    if num == 106:
        return cfg.image_pl06
    if num == 107:
        return cfg.image_pl07
    if num == 108:
        return cfg.image_pl08
    if num == 109:
        return cfg.image_pl09
    if num == 110:
        return cfg.image_pl10


def func_return():
    global running
    running = False


def main():
    # 重新加载游戏
    global plot_num_change
    global plot_num
    global running
    global vector
    plot_num = 0
    running = True

    # 相关背景素材设置
    pygame.init()
    screen = pygame.display.set_mode(cfg.screen_size)
    pygame.display.set_caption(cfg.title_name)
    clock = pygame.time.Clock()

    # 实例准备
    return_button = Button(screen, cfg.pos_return_button,
                           text_in="返回", text_font=cfg.font_path2, text_size=cfg.title_font_size,
                           text_color=cfg.color_white,
                           fill_color=False, edge_color=True, size=(64, 34),
                           call_function=func_return)
    plot = Plot()

    def show():
        # 相关素材绘制
        screen.fill(color_black)
        plot.show_bg(screen)
        plot.show(screen)
        return_button.show()

    def is_event(event):
        plot.is_event(event)
        return_button.update(event)

    def plot_change():
        plot.set_text(text_in=text1[plot_num][2], text_mode=int(text1[plot_num][1]))
        set_image()

    def set_image():
        inf = image1[plot_num].split(";")
        inf_bg = inf[0].split(",")
        bg = [get_bg_image(int(inf_bg[0][3:])), (int(inf_bg[1]), int(inf_bg[2]))]
        pl_ima = []
        pl_pos = []
        if len(inf) > 2:
            for pl_num in range(1, len(inf) - 1):
                pl_swap = inf[pl_num].split(",")
                pl_ima.append(get_pl_image(int(pl_swap[0][3:])))
                pl_pos.append((int(pl_swap[1]), int(pl_swap[2])))
            # print(pl_ima)
            # print(pl_pos)
        if len(pl_ima) > 0:
            plot.set_image(image_list=pl_ima, image_list_pos=pl_pos, image_bg=bg[0], image_bg_pos=bg[1])
        else:
            plot.set_image(image_list=None, image_list_pos=None, image_bg=bg[0], image_bg_pos=bg[1])

    def plot_num_change_func():
        # todo：
        global plot_num_change
        global plot_num
        global running

        key = 0
        if plot_num == 2:
            plot_num = ch1_choose_surface.main()
            key = 1
        if plot_num == 5:
            plot_num = 14
            key = 1
        if plot_num in [8, 11]:
            if ch1_flight1.main():
                plot_num = 12
            else:
                plot_num = 18
            key = 1
        if plot_num == 15:
            if ch1_flight2.main():
                plot_num = 16
            else:
                plot_num = 18

        if plot_num == 17:
            running = False
            global vector
            vector = True
            return
        if plot_num == 18:
            running = False
            return
        if key == 0:
            plot_num += 1

        print(f"plot_num {plot_num}")
        plot_change()
        plot_num_change = not plot_num_change

    # 预准备
    plot_num_change_func()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
                is_event(event)

        plot_num_change = plot.is_die()
        if plot_num_change:
            plot_num_change_func()
        show()
        pygame.display.flip()
        clock.tick(60)
    return vector


running = True
vector = False

# 剧情场景控制
plot_num = 1
plot_num_change = True

# 剧情文本读取
text0 = cfg.text_ch1("resource/font/text1.txt")
text1 = [[]]
for item in text0:
    for text in item:
        text1.append(text.split(" "))
print(text1)
# 剧情图像绘制
image0 = cfg.image_ch1("resource/font/image1.txt")
image1 = [[]]
for item in image0:
    if len(item) > 0:
        image1.append(item)
print(image1)
# 剧情音乐更新




if __name__ == '__main__':
    main()

