from turtle import Turtle

MOVE_POSITIONS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

def get_3_segment_snake():
    segments = []
    x_cor = 0
    for _ in range(3):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.setposition(x=x_cor, y=0)
        x_cor -= 20
        segments.append(segment)
    return segments


class Snake:
    def __init__(self):
        self.segments = get_3_segment_snake()
        self.head = self.segments[0]

    def move_forward(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            prev_segment = self.segments[segment_index - 1]
            new_position = (prev_segment.xcor(), prev_segment.ycor())
            self.segments[segment_index].goto(new_position)
        self.head.forward(MOVE_POSITIONS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_tail(self):
        last_segment = self.segments[-1]
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(segment)
