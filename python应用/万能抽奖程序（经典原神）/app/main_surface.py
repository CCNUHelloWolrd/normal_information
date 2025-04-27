from app.cfg import *
from app.text_surface import *
from app.second_surface import *


def main_function(x, y):
    inf0 = [[490, 710], [490, 530]]
    inf1 = [[290, 510], [590, 630]]
    inf2 = [[690, 910], [590, 630]]
    if is_tick(x, y, inf0):
        second_main()
        print("进入抽奖")
    if is_tick(x, y, inf1):
        text_main("./data/协会简介.txt")
        print("协会简介")
    if is_tick(x, y, inf2):
        text_main("./data/软件简介.txt")
        print("软件简介")


def main():
    # 初始化
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("1024程序设计协会\\百团大战\\抽卡小程序")
    try:
        img1 = Image("./data/背景图片.jpg")
    except OSError:
        img1 = Image("../data/背景图片.jpg")

    text1 = Write("1024程序设计协会", size=120, color=(200, 150, 100))
    text2 = Write("百团大战", size=80, color=(200, 150, 100))
    text3 = Write("抽奖小程序", size=60, color=(100, 200, 100))
    text4 = Write("进入抽奖", size=60, color=(200, 150, 100))
    text5 = Write("协会简介", size=60, color=(100, 200, 100))
    text6 = Write("软件简介", size=60, color=(100, 200, 100))

    # 准备游戏资源
    # 游戏主循环
    clock = pygame.time.Clock()
    while True:
        # 键盘操作反应
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # print(x, y)
                main_function(x, y)

        img1.show((0, 0), screen)
        text1.show((600, 80), screen, mode=4)
        text2.show((600, 200), screen, mode=4)
        text3.show((600, 300), screen, mode=4)
        text4.show((600, 500), screen, mode=4)
        text5.show((400, 600), screen, mode=4)
        text6.show((800, 600), screen, mode=4)
        pygame.display.flip()
        clock.tick(20)


if __name__ == '__main__':
    main()
