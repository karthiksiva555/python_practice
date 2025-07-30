from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
# to turn off the animation where each box seems to move a bit lagging
screen.tracer(0)

snake = Snake()
screen.listen()

food = Food()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move_forward()

    # Detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment_score()
        snake.add_tail()

    # Detect collision with a wall
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > 280 or x < -280 or y > 280 or y < -280:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
