from turtle import Turtle
from models import Position

TOP_RANGE = 340
BOTTOM_RANGE = -300
STEP = 20
LEFT_PADDLE_POSITION = (-380, 0)
RIGHT_PADDLE_POSITION = (370, 0)
UP = "up"
DOWN = "down"


class Paddle(Turtle):

    def __init__(self, left_or_right):
        super().__init__()
        if left_or_right == "left":
            position = LEFT_PADDLE_POSITION
        else:
            position = RIGHT_PADDLE_POSITION

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.last_move = None

    def move_up(self):
        if not self.can_paddle_move_up():
            return

        new_position = (self.xcor(), self.ycor() + STEP)
        x = new_position[0]
        y = new_position[1]

        z = x + y
        self.setposition(new_position)
        self.last_move = UP

    def move_down(self):
        if not self.can_paddle_move_down():
            return

        new_position = (self.xcor(), self.ycor() - STEP)
        self.setposition(new_position)
        self.last_move = DOWN

    def can_paddle_move_up(self):
        if self.ycor() < TOP_RANGE:
            return True
        return False

    def can_paddle_move_down(self):
        if self.ycor() >= BOTTOM_RANGE:
            return True
        return False

    def get_position(self):
        return Position(x=self.xcor(), y=self.ycor())

