from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 12, 'bold'))

    # def display_game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align='center', font=('Arial', 12, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.display_score()

    def update_score(self):
        self.score += 1
        self.display_score()