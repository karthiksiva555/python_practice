from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def increment_left_score(self):
        self.left_score += 1
        self.update_score()

    def increment_right_score(self):
        self.right_score += 1
        self.update_score()