from turtle import Screen
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
# to turn off the animation where each box seems to move a bit lagging
screen.tracer(0)

snake = Snake()
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move_forward()


screen.exitonclick()
