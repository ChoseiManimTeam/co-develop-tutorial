from manim import *

class CreateSquare(Scene):
    def construct(self):
        square = Square()
        createAnim1 = Create(square)
        self.play(createAnim1)
        
        circle = Circle()
        createAnim2 = Create(circle)
        self.play(createAnim2)

        self.wait(2)