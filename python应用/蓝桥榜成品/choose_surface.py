from cfg import *
from cfg2 import *
sys.path.append("..")
import ch1_surface
import ch2_surface
import ch3_surface
import ch4_surface
import ch5_surface
import ch6_surface
import show_surface



def func_return():
    global running
    running = False


def func1():
    global vector
    print(vector)
    if ch1_surface.main():
        vector[1] = 1


def func2():
    global vector
    global mean
    global mean_time
    print(vector)
    if vector[1] == 0:
        global str1
        str1.setting("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)
        mean = True
        mean_time = 120
    else:
        if ch2_surface.main():
            vector[2] = 1


def func3():
    global vector
    global mean
    global mean_time
    print(vector)
    if vector[2] == 0:
        global str1
        str1.setting("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)
        mean = True
        mean_time = 120
    else:
        if ch3_surface.main():
            vector[3] = 1


def func4():
    global vector
    global mean
    global mean_time
    print(vector)
    if vector[3] == 0:
        global str1
        str1.setting("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)
        mean = True
        mean_time = 120
    else:
        if ch4_surface.main():
            vector[4] = 1


def func5():
    global vector
    global mean
    global mean_time
    print(vector)
    if vector[4] == 0:
        global str1
        str1.setting("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)
        mean = True
        mean_time = 120
    else:
        if ch5_surface.main():
            vector[5] = 1


def func6():
    global vector
    global mean
    global mean_time
    print(vector)
    if vector[5] == 0:
        global str1
        str1.setting("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)
        mean = True
        mean_time = 120
    else:
        if ch6_surface.main():
            vector[6] = 1


def func7():
    global vector
    global mean
    global mean_time
    print(vector)
    if vector[6] == 0:
        global str1
        str1.setting(text_in="通关全部关卡以解锁", color=color_white, font=cfg2.font_path3, size=15)
        mean = True
        mean_time = 120
    else:
        show_surface.main()


def main():
    global running
    global vector

    # 相关背景素材设置
    pygame.init()
    screen = pygame.display.set_mode(cfg2.screen_size)
    pygame.display.set_caption(cfg2.title_name)
    clock = pygame.time.Clock()

    background = Image(path=cfg2.image_kg2)
    return_button = Button(screen, cfg2.pos_return_button,
                           text_in="返回", text_font=cfg2.font_path2,
                           text_color=cfg2.color_white, text_size=cfg2.title_font_size,
                           fill_color=False, edge_color=True, size=(64, 34),
                           call_function=func_return)
    height = 370
    weight = 150
    choose_button1 = Button(screen, (height, weight),
                            text_in="序章", text_font=cfg2.font_path2,
                            text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
                            fill_color=True, edge_color=True, size=(64, 34),
                            call_function=func1)
    choose_button2 = Button(screen, (height, weight + 50),
                            text_in="贰章", text_font=cfg2.font_path2,
                            text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
                            fill_color=True, edge_color=True, size=(64, 34),
                            call_function=func2)
    choose_button3 = Button(screen, (height, weight + 100),
                            text_in="叁章", text_font=cfg2.font_path2,
                            text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
                            fill_color=True, edge_color=True, size=(64, 34),
                            call_function=func3)
    choose_button4 = Button(screen, (height, weight + 150),
                            text_in="肆章", text_font=cfg2.font_path2,
                            text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
                            fill_color=True, edge_color=True, size=(64, 34),
                            call_function=func4)
    choose_button5 = Button(screen, (height, weight + 200),
                            text_in="伍章", text_font=cfg2.font_path2,
                            text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
                            fill_color=True, edge_color=True, size=(64, 34),
                            call_function=func5)
    choose_button6 = Button(screen, (height, weight + 250),
                            text_in="终章", text_font=cfg2.font_path2,
                            text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
                            fill_color=True, edge_color=True, size=(64, 34),
                            call_function=func6)
    choose_button7 = Button(screen, (700, 50),
                            text_in="剧情", text_font=cfg2.font_path2,
                            text_color=cfg2.color_choose, text_size=cfg2.title_font_size,
                            fill_color=True, edge_color=True, size=(64, 34),
                            call_function=func7)

    def show():
        global mean
        global mean_time
        # 相关素材绘制
        screen.fill(cfg2.color_black)
        background.show((400, 280), screen, mode=4)
        choose_button1.show()
        choose_button2.show()
        choose_button3.show()
        choose_button4.show()
        choose_button5.show()
        choose_button6.show()
        choose_button7.show()
        return_button.show()
        if mean:
            if mean_time > 0:
                str1.show((400, 400 + mean_time), screen, mode=4)
                mean_time -= 1
            else:
                mean = False

    def is_event(event):
        # 相关事件判定
        choose_button1.update(event)
        choose_button2.update(event)
        choose_button3.update(event)
        choose_button4.update(event)
        choose_button5.update(event)
        choose_button6.update(event)
        choose_button7.update(event)
        return_button.update(event)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
                is_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    vector = [1 for i in range(10)]
        show()
        pygame.display.flip()
        clock.tick(60)


running = True
vector = [0 for i in range(10)]
vector[0] = 1
mean = False
mean_time = 0
str1 = Write("请先通过前面的关卡", color=color_white, font=cfg2.font_path3, size=15)

if __name__ == '__main__':
    main()
