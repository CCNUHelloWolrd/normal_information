import turtle

# 使用Kruskal算法构建最小生成树
def file_read(path):    #数据清洗
    clear_list = ['(', ')', ',', ';','、']
    dot = [[0.0, 0.0]] * 26
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            numbers = line
            for i in clear_list:
                numbers = numbers.replace(i, ' ')
        num_list = numbers.split()
        for i in range(26):
            x = float(num_list[2 * i])
            y = float(num_list[2 * i + 1])
            dot[i] = [x, y]
    return dot


def draw_dot(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(10, "red")


def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor("green")
    turtle.pensize(2)
    turtle.goto(x2, y2)


def visualize(dot, mst_edges):
    # 计算坐标范围
    min_x = min(point[0] for point in dot)
    max_x = max(point[0] for point in dot)
    min_y = min(point[1] for point in dot)
    max_y = max(point[1] for point in dot)

    # 计算画布尺寸（留适当边距）
    width = (max_x - min_x) * 1.5
    height = (max_y - min_y) * 1.5

    # 计算中心点
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    # 设置画布大小和位置（使图形居中）
    screen = turtle.Screen()
    screen.setup(width=width, height=height)
    screen.screensize(width, height)

    # 设置坐标系，使图形居中
    screen.setworldcoordinates(
        center_x - width / 2,
        center_y - height / 2,
        center_x + width / 2,
        center_y + height / 2
    )

    turtle.speed(0)
    turtle.pensize(2)

    # 绘制点
    for x, y in dot:
        draw_dot(x, y)

    # 绘制MST边
    for i, j in mst_edges:
        x1, y1 = dot[i]
        x2, y2 = dot[j]
        draw_line(x1, y1, x2, y2)

    # 添加标签
    for i, (x, y) in enumerate(dot):
        turtle.penup()
        turtle.goto(x + 5, y + 5)
        turtle.pendown()
        turtle.write(str(i), font=('Arial', 12, 'normal'))

    turtle.hideturtle()
    turtle.done()

def find(u):    #检查是否以及与其他点相连（避免成环）
    while parent[u] != u:
        u = parent[u]
    return u

dot = file_read('appendix.txt')
n = len(dot)

distance = [[0.0 for _ in range(26)] for _ in range(26)]    #列表出所有点两两间距离
edges = []
for j in range(n):
    for i in range(n):
        dist = ((dot[i][0] - dot[j][0]) ** 2 + (dot[i][1] - dot[j][1]) ** 2) ** 0.5
        distance[i][j] = dist
        edges.append((dist, i, j))

parent = list(range(n))


mst_edges, total = [], 0.0  #mst_edege为最小路径的边列表，total为总长
edges.sort()    #排序，从最短开始取
for d, i, j in edges:
    if find(i) != find(j):
        parent[find(j)] = find(i)
        mst_edges.append((i, j))
        total += d
        if len(mst_edges) == n - 1:
            break

print(f"路线图总长度: {total:.2f}")
visualize(dot, mst_edges)