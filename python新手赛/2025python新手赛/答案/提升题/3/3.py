import pygame as pg
import sys


class Dialogue:
    def __init__(self, dialogues, font_path=None, font_size=30, text_color=(255, 255, 255)):
        """初始化对话系统"""
        self.dialogues = dialogues  # 对话内容列表
        self.current_index = 0  # 当前对话索引
        self.text_color = text_color

        self.font = pg.font.SysFont(None, font_size)

    def next(self):
        """切换到下一段对话"""
        if self.current_index < len(self.dialogues) - 1:
            self.current_index += 1
            return True  # 有下一段对话
        return False  # 已到最后一段

    def render(self, surface, x, y, max_width):
        """渲染当前对话到指定表面"""
        text = self.dialogues[self.current_index]
        # 处理文本换行
        words = text.split(' ')
        space_width = self.font.size(' ')[0]
        current_line = ''
        current_y = y

        for word in words:
            test_line = current_line + word + ' '
            test_width = self.font.size(test_line)[0]

            if test_width > max_width:
                # 绘制当前行
                line_surface = self.font.render(current_line, True, self.text_color)
                surface.blit(line_surface, (x, current_y))
                current_y += self.font.size(current_line)[1] + 5  # 行间距
                current_line = word + ' '
            else:
                current_line = test_line

        # 绘制最后一行
        if current_line:
            line_surface = self.font.render(current_line, True, self.text_color)
            surface.blit(line_surface, (x, current_y))


def main():
    # 初始化pygame
    pg.init()
    pg.mixer.init()  # 初始化音频

    # 窗口设置
    width, height = 800, 600
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("The Little Prince and the Fox")


    pg.mixer.music.load("background_music.wav")
    pg.mixer.music.set_volume(0.5)  # 设置音量
    pg.mixer.music.play(-1)  # -1表示循环播放

    # 对话内容 - 已改为英文
    dialogues = [
        "Fox: Good morning.",
        "Little Prince: Good morning.",
        "(The little prince responded politely. He turned around, but saw no one.)",
        "Fox: I am right here, under the apple tree.",
        "Little Prince: Who are you? You are very pretty to look at.",
        "Fox: I am a fox.",
        "Little Prince: Come and play with me. I am so unhappy.",
        "Fox: I cannot play with you. I am not tamed."
    ]

    # 创建对话实例
    dialogue_system = Dialogue(dialogues, font_size=28)

    # 主循环
    running = True
    while running:
        # 填充背景色
        screen.fill((40, 40, 60))  # 深蓝色背景

        # 绘制对话框
        dialog_box_rect = pg.Rect(50, height - 200, width - 100, 150)
        pg.draw.rect(screen, (80, 80, 100), dialog_box_rect)  # 对话框背景
        pg.draw.rect(screen, (200, 200, 200), dialog_box_rect, 3)  # 对话框边框

        # 渲染当前对话
        dialogue_system.render(screen, 70, height - 180, width - 140)

        # 事件处理
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                # 点击鼠标切换到下一段对话
                if not dialogue_system.next():
                    # 如果已经是最后一段对话，退出程序
                    running = False

        # 更新显示
        pg.display.flip()

    # 退出程序
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()