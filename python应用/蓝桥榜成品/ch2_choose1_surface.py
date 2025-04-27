from cfg import *
from cfg2 import *


def func_return():
    global running
    running = False


def func_choose1():
    # 返回选择一所代表的节点数
    global running
    running = False
    global ans
    ans = return_num[0]


def func_choose2():
    # 返回选择二所代表的节点数
    global running
    running = False
    global ans
    ans = return_num[1]



def main():
    # 相关背景素材设置
    pygame.init()
    screen = pygame.display.set_mode(cfg2.screen_size)
    pygame.display.set_caption(cfg2.title_name)
    clock = pygame.time.Clock()

    return_button = Button(screen, cfg2.pos_return_button,
                           text_in="返回", text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                           text_color=cfg2.color_white,
                           fill_color=False, edge_color=True, size=(64, 34),
                           call_function=func_return)

    choose1_button = Button(screen, (200, 400),
                            text_in="·溜过去·", text_font=cfg2.font_path3, text_size=choose_font_size,
                            text_color=cfg2.color_white,
                            fill_color=True, edge_color=True, size=(104, 34),
                            call_function=func_choose1)

    choose2_button = Button(screen, (500, 400),
                            text_in="·冲过去·", text_font=cfg2.font_path3, text_size=choose_font_size,
                            text_color=cfg2.color_white,
                            fill_color=True, edge_color=True, size=(104, 34),
                            call_function=func_choose2)
    plot_choose = Plot(button_list=[choose1_button, choose2_button])
    background = Image(path=cfg2.image_kg5)

    def show():
        # 相关素材绘制
        global choose_time
        screen.fill(color_black)
        background.show((0, 100), screen)
        return_button.show()
        plot_choose.show(screen)
        pygame.draw.rect(screen, color_white80, [200, 200, 400, 10], 2)
        pygame.draw.rect(screen, color_red, [200, 200, choose_time * 2, 10], 0)
        pygame.draw.rect(screen, color_black, [200, 200, 400, 10], 2)

    def is_event(event):
        return_button.update(event)
        plot_choose.is_event(event)

    # 重新加载游戏
    global running
    running = True
    global ans
    ans = 4
    global choose_time
    choose_time = 200

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

        choose_time -= 1
        if choose_time <= 0:
            # 返回无选择一所代表的节点数
            running = False
            return return_num[2]

    print(f"ans{ans}")
    return ans



running = True
ans = 0

return_num = [4, 5, 3]



choose_time = 200

if __name__ == '__main__':
    main()
