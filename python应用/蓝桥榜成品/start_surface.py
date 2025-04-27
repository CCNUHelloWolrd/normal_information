from cfg import *
from cfg2 import *
import meaning_surface
import choose_surface
import gift_surface
import setting_surface


def func_start():
    choose_surface.main()


def func_meaning():
    meaning_surface.main()


def func_gift():
    gift_surface.main()


def func_setting():
    setting_surface.main()




def main():
    pygame.init()
    screen = pygame.display.set_mode(cfg2.screen_size)
    pygame.display.set_caption(cfg2.title_name)
    clock = pygame.time.Clock()
    title_button = Button(screen, cfg2.pos_title_button,
                          text_in=cfg2.game_name, text_color=cfg2.color_red,
                          text_font=cfg2.font_path2, text_size=cfg2.game_font_size,
                          fill_color=False, edge_color=True, size=(154, 54))
    start_button = Button(screen, cfg2.pos_start_button,
                          text_in="游戏开始", text_color=cfg2.color_red,
                          text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                          fill_color=False, edge_color=True, size=(124, 34),
                          call_function=func_start)
    meaning_button = Button(screen, cfg2.pos_mean_button,
                            text_in="游戏说明", text_color=cfg2.color_red,
                            text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                            fill_color=False, edge_color=True, size=(124, 34),
                            call_function=func_meaning)
    gift_button = Button(screen, cfg2.pos_gift_button,
                         text_in="兑", text_color=cfg2.color_red,
                         text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                         fill_color=True, edge_color=True, size=(34, 34),
                         call_function=func_gift)
    setting_button = Button(screen, cfg2.pos_set_button,
                            text_in="设置", text_color=cfg2.color_red,
                            text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                            fill_color=True, edge_color=True, size=(64, 34),
                            call_function=func_setting)
    out_button = Button(screen, cfg2.pos_out_button,
                         text_in="接", text_color=cfg2.color_red,
                         text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                         fill_color=True, edge_color=True, size=(34, 34),
                         call_function=func_setting)
    background = Image(path=cfg2.image_kg9)
    background.setting(path=cfg2.image_kg8)


    def is_event(event):
        start_button.update(event)
        meaning_button.update(event)
        gift_button.update(event)
        setting_button.update(event)
        out_button.update(event)

    def show():
        screen.fill(cfg2.color_black)
        background.show((400, 280), screen, mode=4)
        title_button.show()
        start_button.show()
        meaning_button.show()
        gift_button.show()
        setting_button.show()
        out_button.show()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
                is_event(event)
        show()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
