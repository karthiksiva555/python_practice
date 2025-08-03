from days_21_to_40.day_22.moving_ball import MovingBall
from days_21_to_40.day_22.paddle import Paddle
from days_21_to_40.day_22.pong_screen import PongScreen
from days_21_to_40.day_22.scoreboard import Scoreboard


class PongGame:

    LEFT_PADDLE = "left"
    RIGHT_PADDLE = "right"

    def __init__(self):
        self.is_game_on = False
        self.screen = PongScreen()
        self.scoreboard = Scoreboard()
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

            if self.is_ball_hitting_paddle():
                self.ball.bounce_horizontal()
                self.ball.increase_ball_speed()

            if self.ball.is_hitting_left_wall():
                self.ball.reset_position()
                self.scoreboard.increment_right_score()

            if self.ball.is_hitting_right_wall():
                self.ball.reset_position()
                self.scoreboard.increment_left_score()

    def is_ball_hitting_paddle(self):
        return self.is_ball_hitting_left_paddle() or self.is_ball_hitting_right_paddle()

    def is_ball_hitting_left_paddle(self):
        left_paddle_position = self.left_paddle.get_position()
        return self.ball.is_hitting_position(left_paddle_position)

    def is_ball_hitting_right_paddle(self):
        right_paddle_position = self.right_paddle.get_position()
        return self.ball.is_hitting_position(right_paddle_position)

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