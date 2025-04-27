# 运行结果控制运行过程的方式实现


import pygame
import time
# 导入库

EMPTY = 0
BLACK = 1
WHITE = 2
# 定义三个状态

black_color = [0,0,0]
white_color = [255,255,255]
# 定义棋子颜色

# 定义棋盘（类）
class ChessBoard(object):

    def __init__(self):
        # self._board = board = [[EMPTY] * 15 for _ in range(15)]
        # 将棋盘每一个交叉点都看作列表的一个元素位，一共有15*15共225个元素
        self._board = [[]]*15       #私域变量？保护？
        self.reset()                #调用类中方法

    # 填充棋盘中的信息
    def reset(self):
        for row in range(len(self._board)):
            self._board[row] = [EMPTY] * 15
    # 定义下棋函数，，row表示行，col表示列，is_black表示判断当前点位该下黑棋，还是白棋
    def move(self,row,col,is_black):
        if self._board[row][col] == EMPTY:
            self._board[row][col] = BLACK if is_black else WHITE
            return True
        return False
    # 绘制棋盘，棋子
    def draw(self,screen):
        # 棋盘骨架与外框
        for h in range(1,16):
            pygame.draw.line(screen, black_color,
                             [40, h*40], [600, h*40], 1)
            pygame.draw.line(screen, black_color,
                             [h * 40, 40], [h * 40, 600], 1)
        pygame.draw.rect(screen, black_color, [36, 36, 568, 568], 3)

        # 标出五个特殊的点位
        pygame.draw.circle(screen, black_color, [320, 320], 5, 0)   #实心
        pygame.draw.circle(screen, black_color, [160, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [160, 480], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 480], 3, 0)

        #获取所有交叉点位,并显示所有棋子的状态
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] != EMPTY:
                    ccolor = black_color \
                        if self._board[row][col] == BLACK else white_color
                    pos = [40 * (col + 1), 40 * (row + 1)]
                    pygame.draw.circle(screen,ccolor,pos,18,0)

# 定义函数，传入当前棋盘上的棋子列表，输出结果，不管黑棋白棋胜，都是传回False，未出结果则为True
def is_win(board):
    for n in range(15):
        # 判断竖直方向上的情况(外循环读取纵向位置，外循环读取横向)
        flag = 0
        for b in board._board:
            if b[n] == 1:
                flag += 1
                if flag == 5:
                    print('黑方胜')
                    return False    #想在这里优化：加入方框显示，不会第一时间退出游戏
            else:
                flag = 0

        flag = 0
        for b in board._board:
            if b[n] == 2:
                flag += 1
                if flag == 5:
                    print('白棋胜')
                    return False
            else:
                flag = 0

        # 判断水平方向胜利（与上一个不同的是内外循环代表的坐标）
        flag = 0
        for b in board._board[n]:
            if b == 1:
                flag += 1
                if flag == 5:
                    print('黑棋胜')
                    return False
            else:
                flag = 0

        flag = 0
        for b in board._board[n]:
            if b == 2:
                flag += 1
                if flag == 5:
                    print('白棋胜')
                    return False
            else:
                flag = 0

        # 判断正斜方向胜利（从右上角到左下角）(思考如何实现遍历每一个可能的棋子？)

        for x in range(4, 25):
            # 从4，到25，仅仅是提高运行效率
            # 本质为将棋盘分成不同的正斜条，然后判断每个条上是否有连续的五个棋子
            flag = 0
            for i, b in enumerate(board._board):
                # 一种遍历的方法
                # 返回内容为地址与地址对应内容
                # 对于此处的二维列表，返回元素为一维列表，因此返回每个一维列表对应的地址和列表的内容
                if 14 >= x - i >= 0 and b[x - i] == 1:
                    # 每次从b中读取对应信息进行判断，此时每个一维列表仅使用一次，所以
                    # 斜对角方向涉及到不同行列，所以对每个一维列表进行一次判断，列表元素地址是有限制的
                    flag += 1
                    if flag == 5:
                        print('黑棋胜')
                        return False
                else:
                    flag = 0

        for x in range(4, 25):
            flag = 0
            for i, b in enumerate(board._board):
                if 14 >= x - i >= 0 and b[x - i] == 2:
                    flag += 1
                    if flag == 5:
                        print('白棋胜')
                        return False
                else:
                    flag = 0

        # 判断反斜方向胜利从左上角到右下角）(思考如何实现遍历每一个可能的棋子？)
        # 执行策略与上一个相同，但是数值进行修正
        for x in range(11, -11, -1):
            flag = 0
            for i, b in enumerate(board._board):
                if 0 <= x + i <= 14 and b[x + i] == 1:
                    flag += 1
                    if flag == 5:
                        print('黑棋胜')
                        return False
                else:
                    flag = 0

        for x in range(11, -11, -1):
            flag = 0
            for i, b in enumerate(board._board):
                if 0 <= x + i <= 14 and b[x + i] == 2:
                    flag += 1
                    if flag == 5:
                        print('白棋胜')
                        return False
                else:
                    flag = 0

    return True

def main():
    board = ChessBoard()
    is_black = True
    pygame.init()
    pygame.display.set_caption("五子棋")
    screen = pygame.display.set_mode((640,640))
    # screen.fill([125,95,24])
    # =[238, 154, 73]
    screen.fill("purple")
    board.draw(screen)
    pygame.display.flip()
    running = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                row = round((y - 40)/40)
                col = round((x - 40)/40)
                if board.move(row, col, is_black):
                    if not is_win(board):
                        break #退出循环不能终止游戏
                        # time.sleep(3600)
                    is_black = not is_black
                    # screen.fill([125, 95, 24])
                    screen.fill("pink")
                    board.draw(screen)
                    pygame.display.flip()






if __name__ =="__main__":
    main()


#todo: 疑问：
# 20,168
