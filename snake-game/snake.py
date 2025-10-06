from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_segments()

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

        self.segments[0].forward(MOVE_DISTANCE)