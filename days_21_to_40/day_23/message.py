from turtle import Turtle

class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")

    def show_message(self, message):
        self.clear()
        self.goto(0, 0)
        self.write(message, align="center", font=("Courier", 80, "normal"))
