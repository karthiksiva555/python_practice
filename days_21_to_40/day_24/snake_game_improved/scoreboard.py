from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    HIGH_SCORE_FILE_NAME = "data.txt"

    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        self.high_score = self.get_high_score_from_file()
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score}, High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score_to_file()
        self.score = 0
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align=ALIGNMENT, font=FONT)

    def get_high_score_from_file(self):
        with open(self.HIGH_SCORE_FILE_NAME) as file:
            high_score = file.read()
            return int(high_score)

    def write_high_score_to_file(self):
        with open(self.HIGH_SCORE_FILE_NAME, mode="w") as file:
            file.write(f"{self.high_score}")
