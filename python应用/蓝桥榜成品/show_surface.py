from cfg import *
from cfg2 import *


def func_return():
    global running
    running = False


def func1(event):
    global move_vkis
    if event.type == pygame.KEYDOWN:
        print(type(event))
        if event.key == pygame.K_SPACE:
            move_vkis = 2.5
            print("asdasd")
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            move_vkis = 0.5
            print("adsa")

def main():
    # 重新加载游戏
    global running
    global show_now
    running = True

    # 相关背景素材设置
    pygame.init()
    screen = pygame.display.set_mode(cfg2.screen_size)
    pygame.display.set_caption(cfg2.title_name)
    clock = pygame.time.Clock()

    # 实例准备
    return_button = Button(screen, cfg2.pos_return_button,
                           text_in="返回", text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                           text_color=cfg2.color_white,
                           fill_color=False, edge_color=True, size=(64, 34),
                           call_function=func_return)
    f1 = open("resource/font/text_show.txt", mode="r", encoding="utf8")
    text_plot = ""
    for line in f1.readlines():
        text_plot += line
    show_plot = Paragraph(text_in=text_plot, color="yellow", size=30)
    tip_show = Write(text_in="按住空格键进行加速", color="white", size=20)

    def show():
        global show_now
        # 相关素材绘制
        screen.fill(color_white160)
        return_button.show()
        show_plot.show_all((100, 200 - int(show_now)), screen, length=20)
        kisss = int((show_now * 100) % 250)
        tip_show.set_color((kisss, kisss, kisss))
        tip_show.show((400, 50), screen, mode=4)

    def is_event(event):
        func1(event)
        return_button.update(event)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
                is_event(event)
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                is_event(event)
        show_now += move_vkis
        show()
        pygame.display.flip()
        clock.tick(60)


running = True
move_vkis = 0.5
show_now = 0




if __name__ == '__main__':
    main()

