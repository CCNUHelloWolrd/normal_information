import pygame
import sys

# todo:运行结果为一个显示榜单的界面，自行截图

##
TITLE_NAME = "2025 榜单"
SCREEN_SIZE = (1200, 800)
BACKGROUND_PICTURE = "2025 榜单/星空1.png"
num_eg = 9+6+8+6+10+7  # 题单总题数，需人工给出
##
# 自定义类
class Write:
    """绘制字体"""
    def __init__(self, str1, x, y, screen, size, color):
        font = pygame.font.Font("C:/Windows/Fonts/STXINWEI.TTF", size)
        text1 = font.render(str1, True, color)
        textRect1 = text1.get_rect()
        textRect1.topleft = (x, y)  # 90,120
        screen.blit(text1, textRect1)


class Img:
    """绘制图像"""
    def __init__(self, path, pos, screen):
        img = pygame.image.load(path)
        rect = img.get_rect()
        rect.topleft = pos
        screen.blit(img, rect)


##
# 信息处理函数
def get_inf_1():
    # todo: 每次公布前先更新一遍榜单信息
    # todo: 更新方式：
    #  将所有题单的得分信息复制到“榜单信息.txt”中（不需要考虑顺序，但要做到不重不漏），
    #  不同题单的信息需要做任何区分，区分方式为在题单信息的前一行添加一个只有数字的空行，（见示例）

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

def get_inf_2():
    # todo: 每次公布前先更新一遍榜单信息
    # todo: 更新方式：
    #  将所有比赛的得分信息复制到“比赛信息.txt”中（不需要考虑顺序，但要做到不重不漏）

    # 代码段功能：读取“榜单信息.txt”信息，统计所有同学的累计得分，
    #           得到字典inf,每一个昵称对应一个总分
    file = open("./比赛信息.txt", mode="r", encoding="utf")
    name = ""
    inf = {}
    lines = file.readlines()
    for line in lines:
        use = [i.replace("\n", "") for i in line.split("\t") if i != ""]
        # 人员信息
        if len(use) == 3:
            name = use[1]
            if use[1] in inf:
                inf[use[1]] = [inf[use[1]][0] + int(use[2]), inf[use[1]][1]]
            else:
                inf[use[1]] = [int(use[2]), 0]
        elif len(use) == 2:
            if use[1] == "100":
                inf[name] = [inf[name][0], inf[name][1] + 1]
    file.close()
    # 返回排序后的信息
    new_inf = sorted(inf.items(), key=lambda cmp: cmp[1][0], reverse=True)
    new_inf = [[enum[0], enum[1][0], enum[1][1]] for enum in new_inf]
    print(new_inf)
    return new_inf


##
# 界面绘制函数
def print_sheet1(screen, inf, start_index=0):
    # todo:本函数用于将信息显示在屏幕上，每次注意更新特效，一个界面默认显示30人

    # 计算榜单前十和总分
    score_top10 = 0
    score_all = 0
    for i in range(0, 10):
        score_top10 += inf[i][1]
    for i in inf:
        score_all += i[1]

    # 文字绘制位置
    x_swap = 50
    x_width = 710

    # todo: 表头信息
    # 两次打印实现赛博风
    # Write("=" * 19 + "2024 榜单" + "=" * 19, 12 + x_swap, 30, screen, 30, "blue")
    # Write("\t\tTotal：{:\u3000<35}Ave of top10：{:<20}".format(score_all, int(score_top10 / 10)), 12 + x_swap, 60, screen, 20,
    #       "blue")
    Write("=" * 19 + "2025 榜单" + "=" * 19, 10 + x_swap, 30, screen, 30, "firebrick")
    Write("\t\tTotal：{:\u3000<35}Ave of top10：{:<20}".format(score_all, int(score_top10 / 10)), 10 + x_swap, 60, screen, 20,
          "red")

    # todo:显示每个人的信息
    for i in range(start_index, min(start_index + 30, len(inf))):
        name = inf[i][0]
        score = int(inf[i][1])

        # todo: 特效
        # todo:特判，如果该同学的分数达到要求，绘制金色特效，（其中95可以改成任意的要求，即达到总分的95%）
        if score >= num_eg * 95:
            Write("#{:<5} name：{} ".format(i + 1, name), 10 + x_swap, 80 + (i - start_index) * 20, screen, 20, "gold")
            Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + x_swap,
                  80 + (i - start_index) * 20,
                  screen,
                  20, "gold")
        else:
            Write("#{:<5} name：{} ".format(i + 1, name), 10 + x_swap, 80 + (i - start_index) * 20, screen, 20, "lightcyan")
            Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + x_swap, 80 + (i - start_index) * 20,
                  screen, 20,
                  "darkorange")

        # todo:个人特效，特判，可继续添加
        #  依据下述两条，判断分数或同学，显示格式为两个屎山模组，其中特效为颜色，可以更改为其他颜色
        # # todo:特判，该同学的特殊要求，冷酷杀手黑
        # if "陈冶邦" in name:
        #     Write("#{:<5} name：{} ".format(i + 1, name), 12 + x_swap, 80 + i * 20, screen, 20, "blue")
        #     Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + 2 + x_swap, 80 + i * 20,
        #           screen, 20,
        #           "blue")
        #     Write("#{:<5} name：{} ".format(i + 1, name), 10 + x_swap, 80 + i * 20, screen, 20, "black")
        #     Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + x_swap, 80 + i * 20, screen,
        #           20, "black")
        #     continue
        # # todo：特判，该同学要求添加个性图标
        # if "潘浩" in name:
        #     Img("2024 榜单/潘浩专属1(已去底).png", (260 + 8 + x_swap, 80 + i * 20 - 1.5), screen)
        #     Write("#{:<5} name：{} ".format(i + 1, name), 10 + x_swap, 80 + i * 20, screen, 20, "black")
        #     Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + x_swap, 80 + i * 20, screen,
        #           20, "black")
        #     Write("#{:<5} name：{} ".format(i + 1, name), 11 + x_swap, 80 + i * 20, screen, 20, "black")
        #     Write("\tscores:{:<8} complete:{:.0%}".format(score, (score / (num_eg * 100))), x_width + 1 + x_swap, 80 + i * 20,
        #           screen, 20,
        #           "black")
        #     continue

def print_sheet2(screen, inf, start_index=0):
    # todo:本函数用于将信息显示在屏幕上，每次注意更新特效，一个界面默认显示30人

    # 文字绘制位置
    x_swap = 50
    x_width = 680

    # 计算榜单前十和总分
    score_top10 = 0
    score_all = 0
    for i in range(0, min(10, len(inf))):
        score_top10 += inf[i][1]
    for i in inf:
        score_all += i[1]

    # todo: 表头信息
    Write("=" * 18 + "2025 榜单 比赛" + "=" * 18,  x_swap, 30, screen, 30, "firebrick")
    Write("\t\tTotal：{:\u3000<35}Ave of top10：{:<20}".format(score_all, int(score_top10 / 10)), 10 + x_swap, 60, screen, 20,
          "red")

    # todo:显示每个人的信息
    for i in range(start_index, min(start_index + 30, len(inf))):
        name = inf[i][0]
        score = int(inf[i][1])
        ac_num = int(inf[i][2])
        print(name)

        # todo: 特效 (特判)
        Write("#{:<5} name：{} ".format(i + 1, name), 10 + x_swap, 80 + (i - start_index) * 20, screen, 20, "lightcyan")
        Write("scores:{:<8}".format(score), x_width + x_swap, 80 + (i - start_index) * 20,
              screen, 20,"darkorange")
        Write("complete:{:.0%}".format(score / (num_eg * 100)), x_width + x_swap + 150, 80 + (i - start_index) * 20,
              screen, 20,"darkorange")
        Write("ac_num:{}".format(ac_num), x_width + x_swap + 310, 80 + (i - start_index) * 20,
              screen, 20 ,"darkorange")

def show_screen_enum(screen):
    # todo: 两个模式只能选一个使用，另一个必须注释
    # 一个界面只能显示30个人，30名以后的人员请在start_index中修改起始排名
    # 背景图片
    Img(BACKGROUND_PICTURE, (0, 0), screen)

    # todo:题单模式
    # # 信息处理
    # # inf: [[str, int] ...]
    # inf = get_inf_1()
    # # 界面信息
    # print_sheet1(screen, inf, start_index=0)

    # todo: 比赛模式
    # 信息处理
    # inf: [[str, int, ac_num] ...]
    inf = get_inf_2()
    # 界面信息
    print_sheet2(screen, inf, start_index=0)


def main():
    # 界面初始化
    pygame.init()
    pygame.display.set_caption(TITLE_NAME)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    show_screen_enum(screen)
    pygame.display.flip()

    while True:
        # 仅支持退出，无其他功能
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
