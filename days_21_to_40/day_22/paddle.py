from turtle import Turtle

TOP_RANGE = 340
BOTTOM_RANGE = -300
STEP = 20
LEFT_PADDLE_POSITION = (-380, 0)
RIGHT_PADDLE_POSITION = (370, 0)

def get_paddle(position):
    paddle = Turtle("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(position)

    return paddle

class Paddle:

    def __init__(self, left_or_right):
        if left_or_right == "left":
            self.paddle = get_paddle(LEFT_PADDLE_POSITION)
        elif left_or_right == "right":
            self.paddle = get_paddle(RIGHT_PADDLE_POSITION)

    def move_up(self):
        if not self.can_paddle_move_up():
            return

        new_position = (self.paddle.xcor(), self.paddle.ycor() + STEP)
        self.paddle.setposition(new_position)

    def move_down(self):
        if not self.can_paddle_move_down():
            return

        new_position = (self.paddle.xcor(), self.paddle.ycor() - STEP)
        self.paddle.setposition(new_position)

    def can_paddle_move_up(self):
        if self.paddle.ycor() < TOP_RANGE:
            return True
        return False

    def can_paddle_move_down(self):
        if self.paddle.ycor() >= BOTTOM_RANGE:
            return True
        return False

