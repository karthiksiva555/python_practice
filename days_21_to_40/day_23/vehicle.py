from turtle import Turtle
import random
import time

class Vehicle(Turtle):

    START_X = 360
    LEFT_LIMIT = -380
    STEP = 10

    def __init__(self, size, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=size, stretch_wid=1)
        self.color(color)
        self.penup()
        self.goto_start()

    def goto_start(self):
        random_row = random.randint(-15, 15)
        random_y = random_row * 20
        self.goto(self.START_X, random_y)

    def move(self):
        time.sleep(0.1)
        if self.xcor() - self.STEP >= self.LEFT_LIMIT:
            self.goto(self.xcor() - self.STEP, self.ycor())
        else:
            self.hideturtle()