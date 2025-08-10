from turtle import Turtle
import random
from models import Position

class CrossingTurtle(Turtle):

    BOTTOM_ROW = -350
    STEP = 10
    LEFT_LIMIT = -380
    RIGHT_LIMIT = 380
    UPPER_LIMIT = 380
    LOWER_LIMIT = -380

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.left(90)
        self.penup()
        self.goto_random_start_position()

    def goto_random_start_position(self):
        random_x = random.randint(-350, 350)
        self.goto(random_x, self.BOTTOM_ROW)

    def move_up(self):
        if self.ycor() + self.STEP <= self.UPPER_LIMIT:
            self.goto(self.xcor(), self.ycor() + self.STEP)

    def move_down(self):
        if self.ycor() - self.STEP >= self.LOWER_LIMIT:
            self.goto(self.xcor(), self.ycor() - self.STEP)

    def move_left(self):
        if self.xcor() - self.STEP >= self.LEFT_LIMIT:
            self.goto(self.xcor() - self.STEP, self.ycor())

    def move_right(self):
        if self.xcor() + self.STEP <= self.RIGHT_LIMIT:
            self.goto(self.xcor() + self.STEP, self.ycor())

    def is_at_finish_line(self):
        return self.ycor() >= self.UPPER_LIMIT

    def get_current_position(self):
        return Position(x=self.xcor(), y=self.ycor())