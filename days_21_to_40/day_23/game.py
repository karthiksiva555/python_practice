from days_21_to_40.day_23.crossing_turtle import CrossingTurtle
from days_21_to_40.day_23.vehicle import Vehicle
from game_screen import GameScreen
from message import Message


class Game:
    def __init__(self):
        self.screen = GameScreen()
        self.crossing_turtle = CrossingTurtle()
        self.vehicle = Vehicle(2, "red")
        self.message = Message()
        self.map_key_events()
        self.screen.update()
        self.is_game_on = False

    def start(self):
        self.is_game_on = True

        while self.is_game_on:
            self.vehicle.move()

            self.screen.update()

            # sample message
            self.message.show_message("Game started!")

            if self.crossing_turtle.did_cross_traffic():
                self.message.show_message("You Won!")

    def stop(self):
        self.is_game_on = False
        self.screen.bye()

    def map_key_events(self):
        self.screen.listen()
        self.screen.onkey(key="Up", func=self.crossing_turtle.move_up)
        self.screen.onkey(key="Down", func=self.crossing_turtle.move_down)
        self.screen.onkey(key="Left", func=self.crossing_turtle.move_left)
        self.screen.onkey(key="Right", func=self.crossing_turtle.move_right)
        self.screen.onkey(key="Escape", func=self.stop)
