from tkinter.constants import RIGHT
from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_segments()
        self.head = self.segments[0]

    def create_segments(self):
        for position in STARTING_POSITIONS:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            current_seg = self.segments[index]
            next_seg = self.segments[index - 1]
            current_seg.goto(next_seg.xcor(), next_seg.ycor())

        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)