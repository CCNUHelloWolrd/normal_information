from cfg import *
from cfg2 import *
import flight_meaning_surface

running = True
pl2_mode = None
pl2_time = 0
pl2_time_max = 50
pl2_key = False
vector = False


def func_return():
    global running
    running = False


def func1():
    flight_meaning_surface.main()


def main():
    # 初始化
    pygame.init()
    screen = pygame.display.set_mode(cfg2.screen_size)
    pygame.display.set_caption(cfg2.title_name)
    # 游戏要素准备
    pl1 = Player(pl_image=cfg2.image_pl2, pl_name="少年", pl_pos=(100, 500), attack=30)
    pl2 = Player(pl_image=cfg2.image_pl16, pl_name="黑木", pl_pos=(500, 500), show_mode=1)
    pl_group = pygame.sprite.Group(pl1, pl2)
    bu1_group = pygame.sprite.Group()
    bu2_group = pygame.sprite.Group()
    clock = pygame.time.Clock()
    return_button = Button(screen, cfg2.pos_return_button,
                           text_in="返回", text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                           text_color=cfg2.color_white,
                           fill_color=False, edge_color=True, size=(64, 34),
                           call_function=func_return)
    mean_button = Button(screen, (650, 50),
                         text_in="规则", text_color=cfg2.color_red,
                         text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                         fill_color=False, edge_color=True, size=(64, 34),
                         call_function=func1)

    # 关键函数
    def show():
        # 绘制元素
        screen.fill(cfg2.color_white60)
        pl1.draw(screen)
        pl2.draw1(screen)
        pl_group.draw(screen)
        bu1_group.draw(screen)
        bu2_group.draw(screen)
        return_button.show()
        mean_button.show()

    def game_move():
        # 进行当前实例的状态更新
        pl1.update()
        pl2.update()
        bu1_group.update()
        bu2_group.update()
        # 判断命中
        spri1 = pygame.sprite.spritecollide(pl1, bu2_group, dokill=False)
        spri2 = pygame.sprite.spritecollide(pl2, bu1_group, dokill=True)
        for item in spri1:
            pl1.attack_get(item)
            bu2_group.remove(item)
        for item in spri2:
            pl2.attack_get(item)
            bu1_group.remove(item)

    # 准备人机的攻击模式
    def pl2_attack():
        global pl2_mode
        global pl2_time
        global pl2_time_max
        global pl2_key
        global vector
        if pl2_time > 0:
            pl2_time -= 1
        else:
            if pl2.get_mode() == "attack":
                bu2_group.add(pl2.push_attack(15, 1))
            pl2_mode = random.randint(0, 2)
            pl2.mode_change(pl2_mode)
            pl2_time = random.randint(10, 30)

    # 判断游戏是否结束
    def is_gg():
        global vector
        global running
        if pl1.is_die():
            vector = False
            running = False
        if pl2.is_die():
            vector = True
            running = False

    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
                bu1_key = pl1.is_event(event)
                if bu1_key is not None:
                    bu1_group.add(bu1_key)
                return_button.update(event)
                mean_button.update(event)

        game_move()
        pl2_attack()
        is_gg()
        show()
        pygame.display.flip()
        clock.tick(60)
    return vector




if __name__ == '__main__':
    main()
