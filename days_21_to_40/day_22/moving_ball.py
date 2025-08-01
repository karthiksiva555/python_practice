from turtle import Turtle
import time
from collections import namedtuple

Position = namedtuple('Position', ['x', 'y'])

class MovingBall(Turtle):

    STEP = 5
    UPPER_LIMIT = 380
    LOWER_LIMIT = -380

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(-200, 200)
        self.x_step = self.STEP
        self.y_step = self.STEP

    def move(self):
        time.sleep(0.1)
        current_position = Position(x=self.xcor(), y=self.ycor())
        new_position = self.get_new_position(current_position)
        self.setposition(new_position)

    def get_new_position(self, current_position):

        # if ball hits up or bottom wall, bounce
        if self.is_ball_hitting_wall(current_position):
            self.y_step = self.y_step * -1

        return current_position.x + self.x_step, current_position.y + self.y_step

    def is_ball_hitting_wall(self, current_position):
        return current_position.y + self.y_step >= self.UPPER_LIMIT or current_position.y + self.y_step <= self.LOWER_LIMIT
