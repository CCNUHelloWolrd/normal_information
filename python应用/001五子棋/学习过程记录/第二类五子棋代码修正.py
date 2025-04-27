# 传统的嵌套函数的方式实现,通过直接运行的方式实现
# 感觉出来博主的水平也高不到那里去，不过通过一堆问题的学习，成长了好多


import pygame,sys
import numpy as np

pygame.init()
pygame.display.set_caption("五子棋2")  #非常想吐槽这个版本的游戏
screen = pygame.display.set_mode((670,670))
screen_color = [238,154,73]
line_color = [0,0,0]

def check_win(over_pos):
    mp=np.zeros([15,15],dtype=int)
    # 提高运行速度？

    # 这一步太好奇了，于是直接看代码然后复制了
    for val in over_pos:
        x = int((val[0][0] - 27) / 44)
        y = int((val[0][1] - 27) / 44)
        if val[1]==white_color:
            # 判断依据是？        形成地图记录已有的信息
            mp[x][y]=2#表示白子
        else:
            mp[x][y]=1#表示黑子

    # 通过入列表的形式来判断是否获胜，可以有一个标志量啊，
    # 胜在可以一次读完黑白双方信息，使用numpy库可以提高很多效率？
    # todo:改用标志量，使用numpy库
    # 好奇返回的列表的信息是什么，应该是胜方信息，绘制胜利标志的地址，还是可以改进
    # 不得不说逻辑很容易搞懂
    for i in range(15):
        pos1=[]
        pos2=[]
        for j in range(15):
            if mp[i][j]==1:
                pos1.append([i,j])
            else:
                pos1=[]
            if mp[i][j]==2:
                pos2.append([i,j])
            else:
                pos2=[]
            if len(pos1)>=5:#五子连心
                return [1,pos1]
            if len(pos2)>=5:
                return [2,pos2]
    for j in range(15):
        pos1=[]
        pos2=[]
        for i in range(15):
            if mp[i][j]==1:
                pos1.append([i,j])
            else:
                pos1=[]
            if mp[i][j]==2:
                pos2.append([i,j])
            else:
                pos2=[]
            if len(pos1)>=5:
                return [1,pos1]
            if len(pos2)>=5:
                return [2,pos2]
    for i in range(15):
        for j in range(15):
            pos1=[]
            pos2=[]
            for k in range(15):
                # 判断是否超出界限
                if i+k>=15 or j+k>=15:
                    break
                # 左上到右下
                if mp[i+k][j+k]==1:
                    pos1.append([i+k,j+k])
                else:
                    pos1=[]
                if mp[i+k][j+k]==2:
                    pos2.append([i+k,j+k])
                else:
                    pos2=[]
                if len(pos1)>=5:
                    return [1,pos1]
                if len(pos2)>=5:
                    return [2,pos2]
    for i in range(15):
        for j in range(15):
            pos1=[]
            pos2=[]
            for k in range(15):
                if i+k>=15 or j-k<0:
                    break
                if mp[i+k][j-k]==1:
                    pos1.append([i+k,j-k])
                else:
                    pos1=[]
                if mp[i+k][j-k]==2:
                    pos2.append([i+k,j-k])
                else:
                    pos2=[]
                if len(pos1)>=5:
                    return [1,pos1]
                if len(pos2)>=5:
                    return [2,pos2]
    # 返回空储存某种信息？
    return [0,[]]

def find_pos(x,y):
    # 用于将鼠标反馈的坐标信息转换成棋子的坐标信息
    # 效率太低，最后返回的数据也是有问题，数据溢出边界后会报错
    for i in range(27,670,44):
        for j in range(27,670,44):
            l1=1-22
            l2=i+22
            r1=j-22
            r2=j+22
            if x>=l1 and x<=l2 and y>=r1 and y<=r2:
                return i,j
    # return x,y
    # todo:边界溢出为返回信息不正确，修改后的边界条件数据需要修改
    return 27 if x<27 else 643,27 if y<27 else 643

def check_over_pos(x,y,over_pos):
    # 没有看懂原来的人在写什么，真假代表是否落子
    for val in over_pos:
        if val[0][0]==x and val[0][1]==y:
            return False
    return True

flag = False
tim = 0

# 储存信息的地方，好奇效率，相对于五子棋应该是前期越少越好，
# 所以这种遍历方式应该反而更好一点
over_pos=[]
white_color=[255,255,255]
black_color=[0,0,0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 原来按任意键退出时这个意思，不过这个退出是不是太过于粗糙了？
        # if event.type == pygame.KEYDOWN :
        #     sys.exit()
    screen.fill(screen_color)

    #todo: 绘制棋盘，可以单独开个函数
    for i in range(27,670,44):
        # 先画竖线
        # 人是懵逼的，原来就没有好好的规划棋盘空间，怪不得边界条件不对，而且右侧边界有问题原来是这回事
        if i == 27 or i == 670 - 27:  # 边缘线稍微粗一些
            pygame.draw.line(screen, line_color, [i, 27], [i, 670 - 27], 4)
        else:
            pygame.draw.line(screen, line_color, [i, 27], [i, 670 - 27], 2)
        # 再画横线
        if i == 27 or i == 670 - 27:  # 边缘线稍微粗一些
            pygame.draw.line(screen, line_color, [27, i], [670 - 27, i], 4)
        else:
            pygame.draw.line(screen, line_color, [27, i], [670 - 27, i], 2)

    # 在棋盘中心画个小圆表示正中心位置
    # 吐槽：就一个点
    pygame.draw.circle(screen, line_color, [27 + 44 * 7, 27 + 44 * 7], 8, 0)

    for val in over_pos:  # 显示所有落下的棋子
        pygame.draw.circle(screen, val[1], val[0], 20, 0)

    # 判断是否存在五子连心
    # todo:利用bug制作绘图软件？
    res = check_win(over_pos)
    if res[0] != 0:
        for pos in res[1]:
            pygame.draw.rect(screen, [238, 48, 167], [pos[0] * 44 + 27 - 22, pos[1] * 44 + 27 - 22, 44, 44], 2, 1)
        pygame.display.update()  # 刷新显示
        # 学到了，昨天还在头疼，结果多看一个就好多了
        continue  # 游戏结束，停止下面的操作

    # 获取鼠标坐标信息
    x, y = pygame.mouse.get_pos()

    # 实时反馈的方块，差点误导我以为逻辑不对
    x, y = find_pos(x, y)
    if check_over_pos(x, y, over_pos):  # 判断是否可以落子，再显示
        pygame.draw.rect(screen, [0, 229, 238], [x - 22, y - 22, 44, 44], 2, 1)

    #很新颖的想法
    keys_pressed = pygame.mouse.get_pressed()  # 获取鼠标按键信息
    # 鼠标左键表示落子,tim用来延时的，因为每次循环时间间隔很断，容易导致明明只按了一次左键，却被多次获取，认为我按了多次
    # 后面是否就是想解决这个问题，但实际上没有解决
    # todo:所以要加入帧频
    if keys_pressed[0] and tim == 0:
        flag = True
        if check_over_pos(x, y, over_pos):  # 判断是否可以落子，再落子
            if len(over_pos) % 2 == 0:  # 黑子
                over_pos.append([[x, y], black_color])
            else:
                over_pos.append([[x, y], white_color])
        # 看不惯下面的代码于是就注释掉后加了这一句，果然出现了作者说的情况
        # 但关键是有下面的代码问题也没有解决啊，应该从源头获取单击位置或者篡改鼠标点击信息
        flag = False
        # 留着证明自己的傻~~~~~~~~~~~~~~~~(元组好麻烦！)，
        # todo:然鹅事情没有解决于是尝试另一种方式
        # keys_pressed[0] = tuple([0].append([x for x in list(keys_pressed)]))
        list1=list(keys_pressed)
        list1[0] = False
        keys_pressed=tuple(list1)


    # # 鼠标左键延时作用
    # # 原注释看的有点懵，此处没有任何作用
    # if flag:
    #     tim += 1
    # # 延时200ms？难道是一次运行有4ms？没有看出来任何意义
    # # 但是注释掉后居然不能运行了？
    # #
    # if tim % 50 == 0:  # 延时200ms
    #     flag = False
    #     tim = 0
    pygame.display.update()
