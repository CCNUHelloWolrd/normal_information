from cfg import *
from cfg2 import *


def func_return():
    global running
    running = False


def main():
    pygame.init()
    screen = pygame.display.set_mode(cfg2.screen_size)
    pygame.display.set_caption(cfg2.title_name)
    clock = pygame.time.Clock()
    return_button = Button(screen, cfg2.pos_return_button,
                           text_in="返回", text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                           text_color=cfg2.color_black,
                           fill_color=False, edge_color=True, size=(64, 34),
                           call_function=func_return)
    meaning = Paragraph(text_in="""
1.按住鼠标右键进行格挡，格挡期间无法进行蓄力攻击，连击状态无法进行格挡\n
2.按住鼠标左键进行蓄力，松开鼠标左键发起攻击\n
3.当发动攻击时蓄力到黄色区间，角色进入连击状态\n
4.蓄力攻击的攻击值为蓄力条的长度，连击攻击的攻击值为角色的攻击力上限\n
5.连击攻击存在上限，且两次连击间不得中断超过三分之一秒\n
6.所有角色都有隐藏数值，本游戏不支持刮痧\n
""", color="yellow")
    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
                return_button.update(event)
        screen.fill(cfg2.color_white180)
        meaning.show_all((200, 100), screen, length=40)
        return_button.show()
        pygame.display.flip()
        clock.tick(60)


running = True

if __name__ == '__main__':
    main()
