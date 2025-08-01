from turtle import Turtle
import time

class MovingBall:

    STEP = 5

    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.penup()

    def move(self):
        time.sleep(0.1)
        new_position = (self.ball.xcor() + self.STEP, self.ball.ycor() + self.STEP)
        self.ball.setposition(new_position)
