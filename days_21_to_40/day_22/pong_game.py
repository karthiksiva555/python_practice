from days_21_to_40.day_22.moving_ball import MovingBall
from days_21_to_40.day_22.paddle import Paddle
from days_21_to_40.day_22.pong_screen import PongScreen


class PongGame:

    LEFT_PADDLE = "left"
    RIGHT_PADDLE = "right"

    def __init__(self):
        self.is_game_on = False
        self.screen = PongScreen()
        self.left_paddle = Paddle(self.LEFT_PADDLE)
        self.right_paddle = Paddle(self.RIGHT_PADDLE)
        self.map_screen_events()
        self.ball = MovingBall()
        self.screen.update()

    def start_game(self):
        self.is_game_on = True

        while self.is_game_on:
            self.ball.move()
            self.screen.update()


    def stop_game(self):
        self.is_game_on = False
        self.screen.bye()

    def map_screen_events(self):
        self.screen.listen()
        self.screen.onkey(self.left_paddle.move_up, "q")
        self.screen.onkey(self.right_paddle.move_up, "p")
        self.screen.onkey(self.left_paddle.move_down, "a")
        self.screen.onkey(self.right_paddle.move_down, "l")
        self.screen.onkey(self.stop_game, "Escape")