from turtle import Turtle
import time
from models import Position

class MovingBall(Turtle):

    STEP = 10
    UPPER_LIMIT = 380
    LOWER_LIMIT = -380
    LEFT_LIMIT = -380
    RIGHT_LIMIT = 380

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(-200, 200)
        self.x_step = self.STEP
        self.y_step = self.STEP

    def move(self):
        time.sleep(0.1)
        current_position = Position(x=self.xcor(), y=self.ycor())
        new_position = self.get_new_position(current_position)
        self.setposition(new_position)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_horizontal()

    def is_hitting_position(self, position):
        return self.distance(position) <= 50 and (self.xcor() <= -360 or self.xcor() >= 360)

    def bounce_horizontal(self):
        self.x_step *= -1

    def bounce_vertical(self):
        self.y_step *= -1

    def get_new_position(self, current_position):
        if self.is_hitting_top_wall(current_position) or self.is_hitting_bottom_wall(current_position):
            self.bounce_vertical()

        return current_position.x + self.x_step, current_position.y + self.y_step

    def is_hitting_top_wall(self, current_position):
        return current_position.y >= self.UPPER_LIMIT

    def is_hitting_bottom_wall(self, current_position):
        return current_position.y <= self.LOWER_LIMIT

    def is_hitting_left_wall(self):
        return self.xcor() <= self.LEFT_LIMIT

    def is_hitting_right_wall(self):
        return self.xcor() >= self.RIGHT_LIMIT
