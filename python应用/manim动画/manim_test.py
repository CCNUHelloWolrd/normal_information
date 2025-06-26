from manim import *


class Demo(Scene):
    def construct(self):
        square = Square(fill_color=BLUE, fill_opacity=1)
        circle = Circle()
        self.play(Create(square))
        self.wait(1)
        self.play(Transform(square, circle))
        self.wait()
        self.play(ScaleInPlace(circle, 2.5))
        self.wait()
        circle.set_fill(RED, opacity = 1)
        self.wait(2)

        t = Text('Hello world!')
        self.play(Write(t))
        self.wait(5)
