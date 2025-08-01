from turtle import Turtle

TOP_RANGE = 340
BOTTOM_RANGE = -300
STEP = 20
LEFT_PADDLE_POSITION = (-380, 0)
RIGHT_PADDLE_POSITION = (370, 0)


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

    def move_up(self):
        if not self.can_paddle_move_up():
            return

        new_position = (self.xcor(), self.ycor() + STEP)
        self.setposition(new_position)

    def move_down(self):
        if not self.can_paddle_move_down():
            return

        new_position = (self.xcor(), self.ycor() - STEP)
        self.setposition(new_position)

    def can_paddle_move_up(self):
        if self.ycor() < TOP_RANGE:
            return True
        return False

    def can_paddle_move_down(self):
        if self.ycor() >= BOTTOM_RANGE:
            return True
        return False

