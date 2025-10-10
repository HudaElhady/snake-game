from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.write(f"Score: {self.score}", align='center', font=('Arial', 12, 'bold'))

    def display_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 12, 'bold'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.display_score()