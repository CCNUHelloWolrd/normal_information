import pygame
import sys

# todo:运行结果为一个显示榜单的界面，自行截图

# todo: num_eg用于记录总题数（已发布的所有榜单中的所有题目的数量），每次需手动修改，避免得分率超过100%
num_eg = 67


class Write:
    # 屎山模组，文字类
    def __init__(self, str1, x, y, screen, size, color):
        font = pygame.font.Font("C:/Windows/Fonts/STXINWEI.TTF", size)
        # font = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", size)
        text1 = font.render(str1, True, color)
        textRect1 = text1.get_rect()
        textRect1.topleft = (x, y)  # 90,120
        screen.blit(text1, textRect1)


class Img:
    # 屎山模组，图像类
    def __init__(self, path, pos, screen):
        img = pygame.image.load(path)
        rect = img.get_rect()
        rect.topleft = pos
        screen.blit(img, rect)


def is_chinese(uchar):
    # 判断当前字符是否为中文字符
    return uchar >= u'\u4e00' and uchar <= u'\u9fa5'


def func(ustring):
    # 将输入字符串调节为输出宽度为20个全角字符的宽度
    # 记录输入字符串的宽度，遇到中文字符加3，遇到其他字符加2
    num = 0
    for uchar in ustring:
        if is_chinese(uchar):
            num += 3
        else:
            num += 2
    # 计算需要补充的宽度，进行补充并返回补充后的字符串
    add = 60 - num
    if add % 2 == 0:
        return ustring + ' ' * int(add / 2)
    else:
        return ustring + '\u3000' + ' ' * int((add - 3) / 2)


def get_inf():
    # todo: 每次公布前先更新一遍榜单信息
    # todo: 更新方式：
    #  将所有题单的得分信息复制到“榜单信息.txt”中（不需要考虑顺序，但要做到不重不漏），
    #  不同题单的信息需要做任何区分，区分方式为在题单信息的前一行添加一个只有数字的空行，（见示例）
    #  但要注意每一行都应是下一行的格式(直接在洛谷中将信息复制过来就没有格式问题)
    #  # 8	张汝坤只想躺着保命	330	100			100		100	30

    # 代码段功能：读取“榜单信息.txt”信息，统计所有同学的累计得分，
    #           得到字典inf,每一个昵称对应一个总分
    file = open("./榜单信息.txt", mode="r", encoding="utf")
    inf = {}
    new_inf = {}
    lines = file.readlines()
    # todo: (已解决)解决题目重复参与问题
    for line in lines:
        if len(line) > 3:
            use = [i for i in line.split("	")]
            print(use)
            if use[1] in new_inf:
                pass
            else:
                new_inf[use[1]] = 1
                if use[1] in inf:
                    inf[use[1]] += int(use[2])
                else:
                    inf[use[1]] = int(use[2])
        else:
            # print(inf)
            new_inf = {}
    print(inf)
    file.close()
    # 根据每位同学的得分进行排名(注意排名后的数据为二维列表，每个子列表包含昵称与总分两个数据)
    # 返回排序后的信息
    new_inf = sorted(inf.items(), key=lambda cmp: cmp[1], reverse=True)
    return new_inf


def printf(screen):
    # todo:本函数用于将信息显示在屏幕上，每次注意更新特效

    # 计算榜单前十和总分
    inf = get_inf()
    score_top10 = 0
    score_all = 0
    for i in range(0, 10):
        score_top10 += inf[i][1]
    for i in inf:
        score_all += i[1]

    x_swap = 100
    x_width = 710
    ##
    # 此代码段为显示，可在此修改榜单图片效果
    # 表头信息（两次打印为赛博风）
    Write("=" * 19 + "2024 榜单" + "=" * 19, 12 + x_swap, 30, screen, 30, "blue")
    Write("\t\tTotal：{:\u3000<35}Ave of top10：{:<20}".format(score_all, int(score_top10 / 10)), 12 + x_swap, 60, screen, 20,
          "blue")
    Write("=" * 19 + "2024 榜单" + "=" * 19, 10 + x_swap, 30, screen, 30, "firebrick")
    Write("\t\tTotal：{:\u3000<35}Ave of top10：{:<20}".format(score_all, int(score_top10 / 10)), 10 + x_swap, 60, screen, 20,
          "red")
    # todo:显示每个人的信息，可在此更改特效
    for i in range(len(inf)):
        name = func(inf[i][0])
        score = int(inf[i][1])

        # todo:特判，该同学的特殊要求，冷酷杀手黑
        if "陈冶邦" in name:
            Write("#{:<5} name：{} ".format(i + 1, name), 12 + x_swap, 80 + i * 20, screen, 20, "blue")
            Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + 2 + x_swap, 80 + i * 20,
                  screen, 20,
                  "blue")
            Write("#{:<5} name：{} ".format(i + 1, name), 10 + x_swap, 80 + i * 20, screen, 20, "black")
            Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + x_swap, 80 + i * 20, screen,
                  20, "black")
            continue
        if "潘浩" in name:
            Img("2024 榜单/潘浩专属1(已去底).png", (260 + 8 + x_swap, 80 + i * 20 - 1.5), screen)
            Write("#{:<5} name：{} ".format(i + 1, name), 10 + x_swap, 80 + i * 20, screen, 20, "black")
            Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + x_swap, 80 + i * 20, screen,
                  20, "black")
            Write("#{:<5} name：{} ".format(i + 1, name), 11 + x_swap, 80 + i * 20, screen, 20, "black")
            Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + 1 + x_swap, 80 + i * 20,
                  screen, 20,
                  "black")
            continue

        Write("#{:<5} name：{} ".format(i + 1, name), 12 + x_swap, 80 + i * 20, screen, 20, "blue")
        Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + 2 + x_swap, 80 + i * 20,
              screen, 20,
              "blue")
        Write("#{:<5} name：{} ".format(i + 1, name), 10 + x_swap, 80 + i * 20, screen, 20, "lightcyan")
        Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + x_swap, 80 + i * 20,
              screen, 20,
              "darkorange")
        # todo:特判，如果该同学的分数达到要求，绘制金色特效，（其中95可以改成任意的要求，即达到总分的95%）
        if score >= num_eg * 95:
            Write("#{:<5} name：{} ".format(i + 1, name), 10 + x_swap, 80 + i * 20, screen, 20, "gold")
            Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + x_swap, 80 + i * 20,
                  screen,
                  20, "gold")
        # todo:特判，可继续添加
        #  依据上述两条，判断分数或同学，显示格式为两个屎山模组，其中特效为颜色，可以更改为其他颜色


def main():
    # 标准pygame模组

    # 界面初始化
    pygame.init()
    pygame.display.set_caption("2024 榜单")
    screen = pygame.display.set_mode((1200, 800))
    # todo:"./赛博.png"可更改为本文件夹下任意图片，达成换背景的效果，当然可以更改成绘制背景的函数
    Img("2024 榜单/大吉(1).jpg", (0, 0), screen)
    printf(screen)
    pygame.display.flip()

    while True:
        # 事件反应
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()

