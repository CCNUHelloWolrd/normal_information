from cfg import *
from cfg2 import *


def func_return():
    global running
    running = False


def main():
    # 初始化
    pygame.init()
    screen = pygame.display.set_mode(cfg2.screen_size)
    pygame.display.set_caption(cfg2.title_name)
    clock = pygame.time.Clock()

    # 相关背景素材设置
    str1 = Write("《健康游戏忠告》", color=color_white, font=cfg2.font_path3, size=15)
    str2 = Write("抵制不良游戏，拒绝盗版游戏。", color=color_white, font=cfg2.font_path3, size=15)
    str3 = Write("注意自我保护，谨防受骗上当。", color=color_white, font=cfg2.font_path3, size=15)
    str4 = Write("适度游戏益脑，沉迷游戏伤身。", color=color_white, font=cfg2.font_path3, size=15)
    str5 = Write("合理安排时间，享受健康生活。", color=color_white, font=cfg2.font_path3, size=15)
    str11 = Write("游戏策划：韩宇轩", color=color_white, font=cfg2.font_path3, size=20)
    str12 = Write("编程负责：张汝坤", color=color_white, font=cfg2.font_path3, size=20)
    str13 = Write("素材来源：b站乃贝上大分", color=color_white, font=cfg2.font_path3, size=20)
    str14 = Write("游戏结局：Bad,Good,Perfect", color=(200, 100, 100), font=cfg2.font_path3, size=20)
    return_button = Button(screen, cfg2.pos_return_button,
                           text_in="返回", text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                           fill_color=False, edge_color=True, size=(64, 34),
                           call_function=func_return)

    def is_event(event):
        # 相关事件判定
        return_button.update(event)

    def show():
        # 相关素材绘制
        screen.fill((180, 180, 180))
        # 公告
        height = 450
        str1.show((400, height), screen, mode=4)
        str2.show((400, height + 20), screen, mode=4)
        str3.show((400, height + 40), screen, mode=4)
        str4.show((400, height + 60), screen, mode=4)
        str5.show((400, height + 80), screen, mode=4)
        # 制作人员
        height = 200
        str11.show((400, height), screen, mode=4)
        str12.show((400, height + 30), screen, mode=4)
        str13.show((400, height + 60), screen, mode=4)
        str14.show((400, height + 150), screen, mode=4)
        # 返回按钮
        return_button.show()

    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
                is_event(event)
        show()
        pygame.display.flip()
        clock.tick(60)

    return


running = True


if __name__ == '__main__':
    main()
