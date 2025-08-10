from turtle import Turtle
from message import Message

class LevelTracker(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.message = Message()
        self.show_level()

    def increase_level(self):
        self.level += 1

    def show_level(self):
        self.message.show_message_left_top(f"Level {self.level}")

    def level_up(self):
        self.increase_level()
        self.show_level()