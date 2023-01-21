import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        new_x = random.randint(-260, 260)
        new_y = random.randint(-260, 260)
        self.goto(x=new_x, y=new_y)
