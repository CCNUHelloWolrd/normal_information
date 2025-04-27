# 本榜单为打印榜单，且无法排除重复参与作业的情况

# todo: 每次公布前先更新一遍榜单信息
# todo:将所有题单的得分信息复制到“榜单信息.txt”中（不需要考虑顺序，但要做到不重不漏），
#  不同题单的信息不需要做任何区分，但要注意每一行都应是下一行的格式（防止数据结构不正确或添加错误信息）
#  # 8	张汝坤只想躺着保命	330	100			100		100	30

# todo: 2025.1.13（补）：此代码已弃用
def is_chinese(uchar):
    # 判断当前字符是否为中文字符
    return uchar >= u'\u4e00' and uchar <= u'\u9fa5'


def func(ustring, length=20):
    # 将输入字符串调节为输出宽度为20个全角字符的宽度
    # 记录输入字符串的宽度，遇到中文字符加3，遇到其他字符加2
    num = 0
    for uchar in ustring:
        if is_chinese(uchar):
            num += 3
        else:
            num += 2
    # 计算需要补充的宽度，进行补充并返回补充后的字符串
    add = length * 3 - num
    if add % 2 == 0:
        return ustring + ' ' * int(add / 2)
    else:
        return ustring + '\u3000' + ' ' * int((add - 3) / 2)


# todo: 第一行的num_eg用于记录总题数（已发布的所有榜单中的所有题目的数量），每次需手动修改，避免得分率超过100%
num_eg = 12
##
# 代码段功能：读取“榜单信息.txt”信息，统计所有同学的累计得分，
#           得到字典inf,每一个昵称对应一个总分
file = open("./榜单信息.txt", mode="r", encoding="utf")
inf = {}
lines = file.readlines()
for line in lines:
    use = [i for i in line.split("	")]
    try:
        if use[1] in inf:
            inf[use[1]] += int(use[2])
        else:
            inf[use[1]] = int(use[2])
    except:
        pass
file.close()
##
# 代码段功能：根据每位同学的得分进行排名(注意排名后的数据为二维列表，每个子列表包含昵称与总分两个数据)
# 计算出前十名总分与所有人总分
new_inf = sorted(inf.items(), key=lambda cmp: cmp[1], reverse=True)
score_top10 = 0
score_all = 0
for i in range(0, 10):
    score_top10 += new_inf[i][1]
for i in new_inf:
    score_all += i[1]
##
# 代码段功能：将榜单结果打印出来
# 先打印表头，再打印每位同学的信息
print("=====================================2024 榜单=====================================")
print("\tTotal：{:\u3000<20}Ave of top10：{:<20}".format(score_all, int(score_top10/10)))
for i in range(len(new_inf)):
    name = func(new_inf[i][0], length=28)
    score = int(new_inf[i][1])
    print("#{:<5} name：{} ".format(i + 1, name), end="")
    print("\tscores:{:<8} complete:{:.0%}".format(score, (score/(num_eg * 100))))
