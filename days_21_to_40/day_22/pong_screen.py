from turtle import Screen

class PongScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=800)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)

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