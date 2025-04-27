from app.cfg import *


def text_function(x, y):
    inf3 = [[950, 1050], [590, 630]]
    if is_tick(x, y, inf3):
        print("返回")
        return False
    return True


def text_main(file_path_in, size_in=30):
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
    text4 = Write("返回", size=60, color=(200, 200, 100))
    str1 = ""
    try:
        with open(file_path_in, mode="r", encoding='utf-8') as f:
            for line in f.readlines():
                str1 += line
    except OSError:
        with open("."+file_path_in, mode="r", encoding='utf-8') as f:
            for line in f.readlines():
                str1 += line
    except:
        print("文件不存在或文件路径错误")
    paragraph1 = Paragraph(str1, size=size_in)
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
                print(x, y)
                running = text_function(x, y)

        img1.show((0, 0), screen)
        text1.show((600, 80), screen, mode=4)
        text2.show((600, 200), screen, mode=4)
        text3.show((600, 300), screen, mode=4)
        text4.show((1000, 600), screen, mode=4)
        paragraph1.show((300, 400), screen)
        pygame.display.flip()
        clock.tick(20)


if __name__ == '__main__':
    text_main("../data/奖品数目.txt")
