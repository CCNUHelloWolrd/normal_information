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
    str1 = Write("非常抱歉，设置功能不想做了>^<", color=color_white, font=cfg2.font_path3, size=25)
    return_button = Button(screen, cfg2.pos_return_button,
                           text_in="返回", text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                           fill_color=False, edge_color=True, size=(64, 34),
                           call_function=func_return)

    def is_event(event):
        # 相关事件判定
        return_button.update(event)

    def show():
        global str_in
        global enter_time
        global show_key
        # 相关素材绘制
        screen.fill((180, 180, 180))
        str1.show((400, 200), screen, mode=4)
        # 返回按钮
        return_button.show()

    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                is_event(event)
        show()
        pygame.display.flip()
        clock.tick(60)


running = True

if __name__ == '__main__':
    main()
