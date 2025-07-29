import random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

screen.setup(width=500, height=400)
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']
user_bet = screen.textinput(title="Bet on Turtle", prompt="Enter the color to bet on the turtle: ")

def get_turtle(turtle_color):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color)
    new_turtle.penup()
    return new_turtle

def print_end_message(winner_color):
    if winner_color == user_bet:
        print(f"You've won! the {winner_color} is the winner!")
    else:
        print(f"You've lost, the {winner_color} is the winner!")

turtles = []
for color in colors:
    turtles.append(get_turtle(color))

y_coordinate = -100
for turtle in turtles:
    turtle.goto(x=-230, y=y_coordinate)
    y_coordinate += 50

continue_race = True

while continue_race:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() > 230:
            continue_race = False
            print_end_message(turtle.pencolor())
            break

screen.exitonclick()