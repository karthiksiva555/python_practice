from turtle import Turtle
import random

START_X = 400
LEFT_LIMIT = -450
STEP = 10


class Vehicle(Turtle):
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
        self.goto(START_X, random_y)

    def move(self):
        if self.is_vehicle_out_of_range():
            self.hideturtle()
        else:
            self.backward(STEP)

    def is_vehicle_out_of_range(self):
        return self.xcor() < LEFT_LIMIT
