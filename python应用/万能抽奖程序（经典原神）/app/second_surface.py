from app.cfg import *
from app.text_surface import *


def lucky(file_path_in):
    card_inf = []
    try:
        with open(file_path_in, mode="r", encoding='utf-8') as f:
            # 读取现存多少奖品
            for i in range(4):
                line = f.readline()
                card_inf.append(int(line[4:]))
    except OSError:
        with open("."+file_path_in, mode="r", encoding='utf-8') as f:
            # 读取现存多少奖品
            for i in range(4):
                line = f.readline()
                card_inf.append(int(line[4:]))
    except:
        print("文件不存在或文件路径错误")
    print(card_inf)
    if len(card_inf) == 4:
        print("正在抽奖中")
        # 界定抽奖范围
        sum1 = card_inf[0]
        sum2 = sum1 + card_inf[1]
        sum3 = sum2 + card_inf[2]
        sum4 = sum3 + card_inf[3]
        # 开始抽奖
        key = random.randint(1, sum4)
        print(key)
        if key <= sum1:
            # print("1")
            return 1
        if key <= sum2:
            # print("2")
            return 2
        if key <= sum3:
            # print("3")
            return 3
        if key <= sum4:
            # print("4")
            return 4
    else:
        print("抽奖失败")
        return 0


def show(key):
    if key == 1:
        VIDEOSHOW.show_1()
        try:
            text_main("./data/一等奖说明.txt", size_in=40)
        except OSError:
            text_main("../data/一等奖说明.txt", size_in=40)
    if key == 2:
        VIDEOSHOW.show_2()
        try:
            text_main("./data/二等奖说明.txt", size_in=40)
        except OSError:
            text_main("../data/二等奖说明.txt", size_in=40)
    if key == 3:
        VIDEOSHOW.show_3()
        try:
            text_main("./data/三等奖说明.txt", size_in=40)
        except OSError:
            text_main("../data/三等奖说明.txt", size_in=40)
    if key == 4:
        VIDEOSHOW.show_4()
        try:
            text_main("./data/参与奖说明.txt", size_in=40)
        except OSError:
            text_main("../data/参与奖说明.txt", size_in=40)
    print("抽奖结束")


def second_function(x, y):
    inf1 = [[290, 510], [590, 630]]
    inf2 = [[690, 910], [590, 630]]
    inf3 = [[950, 1050], [590, 630]]
    if is_tick(x, y, inf1):
        try:
            keys = lucky("./data/奖品数目.txt")
        except OSError:
            keys = lucky("../data/奖品数目.txt")
        show(keys)
        print("开始抽奖")
    if is_tick(x, y, inf2):
        try:
            text_main("./data/奖品数目.txt")
        except OSError:
            text_main("../data/奖品数目.txt")
        print("奖池明细")
    if is_tick(x, y, inf3):
        print("返回")
        return False
    return True


def second_main():
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
    text4 = Write("开始抽奖", size=60, color=(200, 150, 100))
    text5 = Write("奖池信息", size=60, color=(100, 200, 100))
    text6 = Write("返回", size=60, color=(200, 200, 100))
    # 准备游戏资源
    # 游戏主循环
    clock = pygame.time.Clock()
    running = True
    while running:
        # 键盘操作反应
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # print(x, y)
                running = second_function(x, y)

        img1.show((0, 0), screen)
        text1.show((600, 80), screen, mode=4)
        text2.show((600, 200), screen, mode=4)
        text3.show((600, 300), screen, mode=4)
        text4.show((400, 600), screen, mode=4)
        text5.show((800, 600), screen, mode=4)
        text6.show((1000, 600), screen, mode=4)
        pygame.display.flip()
        clock.tick(20)


if __name__ == '__main__':
    second_main()
