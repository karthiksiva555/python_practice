from turtle import Screen
from models import Position

class GameScreen:

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800

    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Turtle Crossing")
        self.screen.tracer(0)

    def is_hitting_top_wall(self, position: Position):
        return position.y >= (self.SCREEN_WIDTH / 2)

    def update(self):
        self.screen.update()

    def listen(self):
        self.screen.listen()

    def onkey(self, func, key):
        self.screen.onkey(func, key)

    def mainloop(self):
        self.screen.mainloop()

    def bye(self):
        self.screen.bye()
