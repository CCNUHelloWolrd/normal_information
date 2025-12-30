import datetime
import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(5)
t.hideturtle()

# 基础函数：移动（提笔不绘图）
def move(x, y):
    t.penup()
    t.goto(x, y)

# 基础函数：点（用于冒号）
def dot(x, y):
    move(x, y)
    t.pendown()
    t.dot(10)
    t.penup()

# 基础函数：横线（从左到右，长度50，基于当前位置）
def draw_horizontal(x, y):
    move(x, y)
    t.setheading(0)  # 朝右
    t.pendown()
    t.forward(50)
    t.penup()

# 基础函数：竖线（从上到下，长度50，基于当前位置）
def draw_vertical(x, y):
    move(x, y)
    t.setheading(270)  # 朝下
    t.pendown()
    t.forward(50)
    t.penup()

# 0-9数字函数（均以左上角(x,y)为起点，用基础函数拼接）
def draw_0(x, y):
    draw_horizontal(x, y)          # 上横
    draw_vertical(x + 50, y)       # 右竖上半
    draw_vertical(x + 50, y - 50)  # 右竖下半
    draw_horizontal(x, y - 100)    # 下横
    draw_vertical(x, y)            # 左竖上半
    draw_vertical(x, y - 50)       # 左竖下半

def draw_1(x, y):
    draw_vertical(x + 50, y)       # 右竖上半
    draw_vertical(x + 50, y - 50)  # 右竖下半

def draw_2(x, y):
    draw_horizontal(x, y)          # 上横
    draw_vertical(x + 50, y)       # 右上竖
    draw_horizontal(x, y - 50)     # 中横
    draw_vertical(x, y - 50)       # 左下竖
    draw_horizontal(x, y - 100)    # 下横

def draw_3(x, y):
    draw_horizontal(x, y)          # 上横
    draw_vertical(x + 50, y)       # 右上竖
    draw_horizontal(x, y - 50)     # 中横
    draw_vertical(x + 50, y - 50)  # 右下竖
    draw_horizontal(x, y - 100)    # 下横

def draw_4(x, y):
    draw_vertical(x, y)            # 左上竖
    draw_horizontal(x, y - 50)     # 中横
    draw_vertical(x + 50, y)       # 右上竖
    draw_vertical(x + 50, y - 50)  # 右下竖

def draw_5(x, y):
    draw_horizontal(x, y)          # 上横
    draw_vertical(x, y)            # 左上竖
    draw_horizontal(x, y - 50)     # 中横
    draw_vertical(x + 50, y - 50)  # 右下竖
    draw_horizontal(x, y - 100)    # 下横

def draw_6(x, y):
    draw_horizontal(x, y)          # 上横
    draw_vertical(x, y)            # 左上竖
    draw_vertical(x, y - 50)       # 左下竖
    draw_horizontal(x, y - 50)     # 中横
    draw_vertical(x + 50, y - 50)  # 右下竖
    draw_horizontal(x, y - 100)    # 下横

def draw_7(x, y):
    draw_horizontal(x, y)          # 上横
    draw_vertical(x + 50, y)       # 右上竖
    draw_vertical(x + 50, y - 50)  # 右下竖

def draw_8(x, y):
    draw_horizontal(x, y)          # 上横
    draw_vertical(x, y)            # 左上竖
    draw_vertical(x + 50, y)       # 右上竖
    draw_horizontal(x, y - 50)     # 中横
    draw_vertical(x, y - 50)       # 左下竖
    draw_vertical(x + 50, y - 50)  # 右下竖
    draw_horizontal(x, y - 100)    # 下横

def draw_9(x, y):
    draw_horizontal(x, y)          # 上横
    draw_vertical(x, y)            # 左上竖
    draw_vertical(x + 50, y)       # 右上竖
    draw_horizontal(x, y - 50)     # 中横
    draw_vertical(x + 50, y - 50)  # 右下竖
    draw_horizontal(x, y - 100)    # 下横

# 冒号函数（两点，基于左上角对齐）
def draw_colon(x, y):
    dot(x + 20, y - 20)    # 上点（居中）
    dot(x + 20, y - 70)    # 下点（居中）
# 数字映射表，把函数储存在字典里便于调用，不需要多次if判断
num_drawers = {
    '0': draw_0, '1': draw_1, '2': draw_2, '3': draw_3, '4': draw_4,
    '5': draw_5, '6': draw_6, '7': draw_7, '8': draw_8, '9': draw_9
}

# 核心逻辑：获取时间并绘制
now = datetime.datetime.now()
time_str = now.strftime("%H:%M:%S")
print(f"当前时间：{time_str}")

# 绘制参数：起始位置、数字宽度50+间隔20=70
start_x = -300
start_y = 0
digit_step = 70  # 固定间隔20，自动累加

# 遍历绘制
for i, char in enumerate(time_str):
    current_x = start_x + i * digit_step
    if char == ':':
        draw_colon(current_x - 20, start_y)
    else:
        num_drawers[char](current_x, start_y)

turtle.done()