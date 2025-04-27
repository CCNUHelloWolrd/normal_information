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
    str1 = Write("请输入兑换码", color=color_white, font=cfg2.font_path3, size=25)
    str2 = Write("", color=color_white, font=cfg2.font_path3, size=25)
    str3 = Write("", color=color_white, font=cfg2.font_path3, size=25)
    str4 = Write("CCNU1024", color=color_white, font=cfg2.font_path3, size=25)
    return_button = Button(screen, cfg2.pos_return_button,
                           text_in="返回", text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                           fill_color=False, edge_color=True, size=(64, 34),
                           call_function=func_return)

    def is_event(event):
        # 相关事件判定
        return_button.update(event)
        global str_in
        global write_mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                if len(str_in) < 12:
                    str_in += "0"
            if event.key == pygame.K_1:
                if len(str_in) < 12:
                    str_in += "1"
            if event.key == pygame.K_2:
                if len(str_in) < 12:
                    str_in += "2"
            if event.key == pygame.K_3:
                if len(str_in) < 12:
                    str_in += "3"
            if event.key == pygame.K_4:
                if len(str_in) < 12:
                    str_in += "4"
            if event.key == pygame.K_5:
                if len(str_in) < 12:
                    str_in += "5"
            if event.key == pygame.K_6:
                if len(str_in) < 12:
                    str_in += "6"
            if event.key == pygame.K_7:
                if len(str_in) < 12:
                    str_in += "7"
            if event.key == pygame.K_8:
                if len(str_in) < 12:
                    str_in += "8"
            if event.key == pygame.K_9:
                if len(str_in) < 12:
                    str_in += "9"
            if event.key == pygame.K_a:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "A"
                    else:
                        str_in += "a"
            if event.key == pygame.K_b:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "B"
                    else:
                        str_in += "b"
            if event.key == pygame.K_c:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "C"
                    else:
                        str_in += "c"
            if event.key == pygame.K_d:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "D"
                    else:
                        str_in += "d"
            if event.key == pygame.K_e:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "E"
                    else:
                        str_in += "e"
            if event.key == pygame.K_f:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "F"
                    else:
                        str_in += "f"
            if event.key == pygame.K_g:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "G"
                    else:
                        str_in += "g"
            if event.key == pygame.K_h:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "H"
                    else:
                        str_in += "h"
            if event.key == pygame.K_i:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "I"
                    else:
                        str_in += "i"
            if event.key == pygame.K_j:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "J"
                    else:
                        str_in += "j"
            if event.key == pygame.K_k:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "K"
                    else:
                        str_in += "k"
            if event.key == pygame.K_l:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "L"
                    else:
                        str_in += "l"
            if event.key == pygame.K_m:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "M"
                    else:
                        str_in += "m"
            if event.key == pygame.K_n:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "N"
                    else:
                        str_in += "n"
            if event.key == pygame.K_o:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "O"
                    else:
                        str_in += "o"
            if event.key == pygame.K_p:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "P"
                    else:
                        str_in += "p"
            if event.key == pygame.K_q:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "Q"
                    else:
                        str_in += "q"
            if event.key == pygame.K_r:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "R"
                    else:
                        str_in += "r"
            if event.key == pygame.K_s:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "S"
                    else:
                        str_in += "s"
            if event.key == pygame.K_t:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "T"
                    else:
                        str_in += "t"
            if event.key == pygame.K_u:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "U"
                    else:
                        str_in += "u"
            if event.key == pygame.K_v:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "V"
                    else:
                        str_in += "v"
            if event.key == pygame.K_w:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "W"
                    else:
                        str_in += "w"
            if event.key == pygame.K_x:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "X"
                    else:
                        str_in += "x"
            if event.key == pygame.K_y:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "Y"
                    else:
                        str_in += "y"
            if event.key == pygame.K_z:
                if len(str_in) < 12:
                    if write_mode:
                        str_in += "Z"
                    else:
                        str_in += "z"
            if event.key == pygame.K_CAPSLOCK:
                write_mode = not write_mode
            if event.key == pygame.K_BACKSPACE:
                if len(str_in) > 0:
                    str_in = str_in[:-1]
            if event.key == pygame.K_RETURN:
                global enter_time
                enter_time = 250
                if str_in in cfg2.gift1_password:
                    cfg2.gift1_pass = True
                    str3.setting("兑换成功！ 门卡一张")
                    print("兑换成功！ 门卡一张")
                else:
                    str3.setting("兑换失败！")
                str_in = ""

    def show():
        global str_in
        global enter_time
        global show_key
        # 相关素材绘制
        screen.fill((180, 180, 180))
        str2.setting(str_in, color=color_black, font=cfg2.font_path3, size=50)
        pygame.draw.rect(screen, cfg2.color_white, [200, 300, 400, 70], 2)
        str1.show((400, 200), screen, mode=4)
        str2.show((220, 300), screen)
        str4.show((400, 500), screen, mode=4)

        if enter_time > 0:
            enter_time -= 1
            str3.set_color((250 - enter_time, 250 - enter_time, 250 - enter_time))
            str3.show((400, 250), screen, mode=4)

        show_key += 1
        show_key %= 60
        if show_key > 30:
            pygame.draw.rect(screen, cfg2.color_white, [220 + str2.get_y(), 310, 2, 50], 0)

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
show_key = 0
enter_time = 200
write_mode = False
str_in = ""

if __name__ == '__main__':
    main()
