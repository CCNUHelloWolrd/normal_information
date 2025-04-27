import sys, pygame, time, random,os
import numpy as np
from cfg import *

class BOARD_CLASS:
    def __init__(self):
        self._board = np.full((15, 15),0, dtype="i2")


    def update(self,row,col,colortype):
        if self._board[row,col] == 0:
            self._board[row,col] = colortype
            return True
        return False


    def draw(self, screen):
        # 绘制当前棋盘信息
        for i in range(1, 16):
            pygame.draw.line(screen, BLACK_COLOR,
                             [i * 40, 40], [i * 40, 600], 1)
            pygame.draw.line(screen, BLACK_COLOR,
                             [40, i * 40], [600, i * 40], 1)
        pygame.draw.rect(screen,BLACK_COLOR,
                         [36,36,569,569],4)     #起始点，边框大小，边框内宽度 (为什么会如此不整齐，别问我)
        pygame.draw.circle(screen, BLACK_COLOR, [320, 320], 5, 0)
        pygame.draw.circle(screen, BLACK_COLOR, [160, 160], 3, 0)
        pygame.draw.circle(screen, BLACK_COLOR, [160, 480], 3, 0)
        pygame.draw.circle(screen, BLACK_COLOR, [480, 160], 3, 0)
        pygame.draw.circle(screen, BLACK_COLOR, [480, 480], 3, 0)
        for row in range(15):
            for col in range(15):
                if self._board[row][col] != 0:
                    color1 =BLACK_COLOR if self._board[row][col] == 1 else WHITE_COLOR
                    pos = [40*(row+1),40*(col+1)]
                    pygame.draw.circle(screen, color1, pos,18,0)

def is_win(over_pos,boarddates):
    # 判断是否胜利为何要遍历整个棋盘？
    # 游戏结束不过判断四个方向罢了
    x , y =over_pos
    # (0,0)  -> (14,14)
    # print(x,y)
    color1=boarddates[x,y]
    flag = 0
    for i in range(1,15):
        if boarddates[i,y] == color1:
            flag += 1
            if flag == 5:
                return True
        else:
            flag = 0

    flag = 0
    for i in range(1, 15):
        if boarddates[x, i] == color1:
            flag += 1
            if flag == 5:
                return True
        else:
            flag = 0
    flag = 0
    for i in range(-14, 14):
        # 左上到右下
        # 一定有相当多的冗余，但是后期再改
        if 0 <= x + i <15 and 0 <= y + i < 15:
            if boarddates[x + i, y + i] == color1:
                flag += 1
                if flag == 5:
                    return True
            else:
                flag = 0
    for i in range(-14, 14):
        # 右上到左下
        if 0 <= x - i <15 and 0 <= y + i < 15:
            if boarddates[x - i, y + i] == color1:
                flag += 1
                if flag == 5:
                    return True
            else:
                flag = 0
    # if x >= 4:        #没有考虑到最后一个子可以落到中间，初步设想米字检测
    #     flag = 1
    #     for i in range(x,x-5,-1):
    #         if boarddates[i,y] != color1:
    #             flag = 0
    #     if flag == 1:
    #         return True
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_size)
    pygame.display.set_caption("五子棋3 1.0")
    board = BOARD_CLASS()

    file = open(os.path.join(os.getcwd(), '五子棋记录\\第1次记录.txt'), mode="w", encoding="utf-8")

    colorsize = 1
    over = False
    clock = pygame.time.Clock()
    colorkind = SCREEN_COLOR.get(random.randint(0, 138))[:-1]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # pygame.quit()
                # sys.exit()
                pass
                # todo: 按1查看规则
            if event.type == pygame.MOUSEBUTTONDOWN:
                if over:
                    continue
                colorkind = SCREEN_COLOR.get(random.randint(0, 138))[:-1]
                x, y = event.pos
                # row = (x - 40) // 40
                # col = (y - 40) // 40
                row = round((x - 40) / 40)
                col = round((y - 40) / 40)
                file.write(f"{row}\t,{col}"+"\n")
                if board.update(row,col,colorsize):
                    colorsize = 2 if colorsize == 1 else 1
                    if is_win((row,col),board._board):
                        print(f"{'黑' if board._board[row][col] == 1 else '白'}胜利！")
                        file.write(f"{'黑' if board._board[row][col] == 1 else '白'}胜利！")
                        file.close()
                        over = True


        screen.fill(colorkind)
        x, y = pygame.mouse.get_pos()
        x = round((x - 40) / 40)*40
        y = round((y - 40) / 40)*40
        pygame.draw.rect(screen, [0, 229, 238], [x + 20, y + 20, 40, 40], 2, 0)
        board.draw(screen)
        pygame.display.flip()
        clock.tick(10)
if __name__ == "__main__":
    main()
