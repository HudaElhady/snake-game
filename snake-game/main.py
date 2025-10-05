from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

turtles_list = []

for index in range(3):
    turtle = Turtle(shape="square")
    turtle.color("white")
    if index > 0:
        previous_turtle = turtles_list[-1]
        turtle.setx(previous_turtle.xcor() - 20)

    turtles_list.append(turtle)




screen.exitonclick()