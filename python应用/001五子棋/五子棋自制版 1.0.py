import sys, pygame
import numpy as np
from cfg import *

#todo：说明
# 1.0版本删除了所有的多余内容，
# 仅包含基础游戏画面，反馈游戏结果
# 会出现bug，但在不恶意寻找的情况下可以正常进行游戏
# 自我说明：
# 不断添加的时候发现很多地方的代码执行过剩了，
# 但是想要优化性能的话需要细致思考，
# 往往再次回顾代码时会认为原来的棒点子是bug
# 所以目的就是结构清晰，思路明了

class BOARD_CLASS:
    # 棋盘类，游戏过程围绕此类进行
    # 初始化开辟数组，数组储存棋盘状态信息
    def __init__(self):
        self._board = np.full((15, 15),0, dtype="i2")
    # 更新棋盘状态，进行判断，如果状态为空添加新状态
    def update(self,row,col,colortype):
        if self._board[row,col] == 0:
            self._board[row,col] = colortype
            return True
        return False
    # 绘制当前棋盘信息（可视化）-->绘制棋盘框架，显示棋盘状态
    def draw(self, screen):
        # 绘制基本棋盘
        for i in range(1, 16):
            pygame.draw.line(screen, BLACK_COLOR,
                             [i * 40, 40], [i * 40, 600], 1)
            pygame.draw.line(screen, BLACK_COLOR,
                             [40, i * 40], [600, i * 40], 1)
        pygame.draw.rect(screen,BLACK_COLOR,
                         [36,36,569,569],4)
        pygame.draw.circle(screen, BLACK_COLOR, [320, 320], 5, 0)
        pygame.draw.circle(screen, BLACK_COLOR, [160, 160], 3, 0)
        pygame.draw.circle(screen, BLACK_COLOR, [160, 480], 3, 0)
        pygame.draw.circle(screen, BLACK_COLOR, [480, 160], 3, 0)
        pygame.draw.circle(screen, BLACK_COLOR, [480, 480], 3, 0)
        # 更新棋盘状态信息
        for row in range(15):
            for col in range(15):
                if self._board[row][col] != 0:
                    color1 =BLACK_COLOR if self._board[row][col] == 1 else WHITE_COLOR
                    pos = [40*(row+1),40*(col+1)]
                    pygame.draw.circle(screen, color1, pos,18,0)

def is_win(over_pos,boarddates):
    # 判断最后一次落子后是否达到胜利要求
    x , y =over_pos
    color1=boarddates[x,y]
    # 竖直方向
    flag = 0
    for i in range(1,15):
        if boarddates[i,y] == color1:
            flag += 1
            if flag == 5:
                return True
        else:
            flag = 0
    # 水平方向
    flag = 0
    for i in range(1, 15):
        if boarddates[x, i] == color1:
            flag += 1
            if flag == 5:
                return True
        else:
            flag = 0
    # 左上到右下
    flag = 0
    for i in range(-14, 14):
        if 0 <= x + i < 15 and 0 <= y + i < 15:
            if boarddates[x + i, y + i] == color1:
                flag += 1
                if flag == 5:
                    return True
            else:
                flag = 0
    # 右上到左下
    flag = 0
    for i in range(-14, 14):
        if 0 <= x - i < 15 and 0 <= y + i < 15:
            if boarddates[x - i, y + i] == color1:
                flag += 1
                if flag == 5:
                    return True
            else:
                flag = 0
    # 所有条件均不满足
    return False

def main():
    # 界面初始化
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_size)
    pygame.display.set_caption("五子棋自制版 1.0")
    # 游戏参数准备
    board = BOARD_CLASS()
    colorsize = 1
    over = False
    # 开始主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if over:
                    continue
                x, y = event.pos
                row = round((x - 40) / 40)
                col = round((y - 40) / 40)
                if board.update(row,col,colorsize):
                    colorsize = 2 if colorsize == 1 else 1
                    if is_win((row, col), board._board):
                        print(f"{'黑' if board._board[row][col] == 1 else '白'}胜利！")
                        over = True
        # 刷新游戏画面
        screen.fill(BOARD_COLOR)
        board.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()
