from cfg import *
from cfg2 import *
import ch4_choose1_surface
import ch4_choose2_surface
import ch4_flight1_surface
import ch4_flight2_surface
import ch4_flight3_surface



def func_return():
    global running
    running = False


def main():
    # 重新加载游戏
    global plot_num_change
    global plot_num
    global running
    global vector
    plot_num = 0
    running = True

    # 相关背景素材设置
    pygame.init()
    screen = pygame.display.set_mode(cfg2.screen_size)
    pygame.display.set_caption(cfg2.title_name)
    clock = pygame.time.Clock()

    # 实例准备
    return_button = Button(screen, cfg2.pos_return_button,
                           text_in="返回", text_font=cfg2.font_path2, text_size=cfg2.title_font_size,
                           text_color=cfg2.color_white,
                           fill_color=False, edge_color=True, size=(64, 34),
                           call_function=func_return)
    plot = Plot()

    def show():
        # 相关素材绘制
        screen.fill(color_black)
        plot.show_bg(screen)
        plot.show(screen)
        return_button.show()

    def is_event(event):
        plot.is_event(event)
        return_button.update(event)

    def plot_change():
        plot.set_text(text_in=text1[plot_num][2], text_mode=int(text1[plot_num][1]))
        set_image()

    def set_image():
        inf = image1[plot_num].split(";")
        inf_bg = inf[0].split(",")
        bg = [get_bg_image(int(inf_bg[0][3:])), (int(inf_bg[1]), int(inf_bg[2]))]
        pl_ima = []
        pl_pos = []
        if len(inf) > 2:
            for pl_num in range(1, len(inf) - 1):
                pl_swap = inf[pl_num].split(",")
                pl_ima.append(get_pl_image(int(pl_swap[0][3:])))
                pl_pos.append((int(pl_swap[1]), int(pl_swap[2])))
        if len(pl_ima) > 0:
            plot.set_image(image_list=pl_ima, image_list_pos=pl_pos, image_bg=bg[0], image_bg_pos=bg[1])
        else:
            plot.set_image(image_list=None, image_list_pos=None, image_bg=bg[0], image_bg_pos=bg[1])

    def plot_num_change_func():
        # todo：
        global plot_num_change
        global plot_root
        global plot_num
        global running

        # plot_num += 1
        if len(root_com[plot_root]) == 0:
            plot_root = 1
        if plot_num != root_com[plot_root][-1]:
            plot_num += 1
        else:
            if plot_root == 2:
                if ch4_flight1_surface.main():
                    plot_root = 3
                    plot_num = root_com[plot_root][0]
                else:
                    plot_root = 12
                    plot_num = root_com[plot_root][0]
            elif plot_root == 3:
                key = ch4_choose1_surface.main()
                if key == 1:
                    plot_root = 4
                    plot_num = root_com[plot_root][0]
                else:
                    plot_root = 5
                    plot_num = root_com[plot_root][0]
            elif plot_root == 5:
                plot_root = 6
                for i in range(3):
                    if ch4_flight2_surface.main():
                        continue
                    plot_root = 12
                    break
                plot_num = root_com[plot_root][0]
            elif plot_root == 7:
                if ch4_flight3_surface.main():
                    plot_root = 8
                    plot_num = root_com[plot_root][0]

                    key = ch4_choose2_surface.main()
                    if key == 1:
                        cfg2.choose_ch4.append(10)
                        plot_root = 10
                        plot_num = root_com[plot_root][0]
                    else:
                        plot_root = 9
                        plot_num = root_com[plot_root][0]
                else:
                    plot_root = 12
                    plot_num = root_com[plot_root][0]
            # elif plot_num == 8:
            #     key = ch4_choose2_surface.main()
            #     if key == 1:
            #         cfg2.choose_ch4.append(10)
            #         plot_root = 10
            #         plot_num = root_com[plot_root][0]
            #     else:
            #         plot_root = 9
            #         plot_num = root_com[plot_root][0]
            else:
                plot_root = control[plot_root][0]
                if len(root_com[plot_root]) == 0:
                    running = False
                else:
                    plot_num = root_com[plot_root][0]
        if plot_root in [9, 10]:
            global vector
            vector = True
        print(f"plot_root{plot_root}")
        print(f"plot_num {plot_num}")
        plot_change()
        plot_num_change = not plot_num_change

    # 预准备
    plot_num_change_func()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
                is_event(event)

        plot_num_change = plot.is_die()
        if plot_num_change:
            plot_num_change_func()
        show()
        pygame.display.flip()
        clock.tick(60)
    print(vector)
    return vector


running = True
vector = False

# 剧情场景控制
plot_root = 0
plot_num = 1
plot_num_change = True

# 剧情文本读取
text0 = cfg2.text_get("resource/font/text4.txt")
# print(text0)
text1 = [[]]
for item in text0:
    for text in item:
        text1.append(text.split(" "))
# print(text1)
# 剧情图像绘制
image0 = cfg2.image_get("resource/font/image4.txt")
image1 = [[]]
for item in image0:
    if len(item) > 0:
        image1.append(item)
# print(image1)
# todo:剧情音乐更新
# todo:考虑使用链表操纵剧情展示
#  利用迭代器统计节点数
root_kis = iter([i + 1 for i in range(len(text1))])
root_com = []
for items in text0:
    swap = []
    for item in items:
        swap.append(next(root_kis))
    root_com.append(swap)
print(root_com)
print(len(root_com))
control = [[0], [2], [3], [4, 5], [7], [6], [7], [8], [9, 10], [11], [11], [0], [0], [0]]
if __name__ == '__main__':
    main()

