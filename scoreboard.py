from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(-150, 270)
        self.ht()
        self.new_high_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.storing_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def storing_high_score(self):
        with open("high-score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def new_high_score(self):
        with open("high-score.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()





