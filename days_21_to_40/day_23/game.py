import time
from days_21_to_40.day_23.crossing_turtle import CrossingTurtle
from game_screen import GameScreen
from message import Message
from vehicle_manager import VehicleManager


class Game:

    def __init__(self):
        self.screen = GameScreen()
        self.crossing_turtle = CrossingTurtle()
        self.vehicle_manager = VehicleManager()
        self.message = Message()
        self.map_key_events()
        self.screen.update()
        self.is_game_on = False

    def start(self):
        self.is_game_on = True

        while self.is_game_on:
            time.sleep(0.1)
            self.vehicle_manager.add_vehicle_random()
            self.vehicle_manager.move_vehicles()
            self.screen.update()

            if self.vehicle_manager.any_vehicle_colliding(self.crossing_turtle.get_current_position()):
                self.message.show_message("Game Over")
                self.is_game_on = False

            if self.crossing_turtle.is_at_finish_line():
                self.crossing_turtle.goto_random_start_position()
                self.message.show_message_left_top("Level 2")
                self.vehicle_manager.level_up()
        else:
            self.screen.exit_on_click()

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
