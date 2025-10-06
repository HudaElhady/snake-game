from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []

for index in range(3):
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    if index > 0:
        previous_segment = segments[-1]
        segment.setx(previous_segment.xcor() - 20)

    segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for index in range(len(segments)-1, 0, -1):
        current_seg = segments[index]
        next_seg = segments[index-1]
        current_seg.goto(next_seg.xcor(), next_seg.ycor())

    segments[0].forward(20)


screen.exitonclick()