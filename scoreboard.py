from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("grey")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.life = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 330)
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(200, 330)
        self.write(f"LIFES: {self.life}", align=ALIGNMENT, font=FONT)

    def score_up(self, color):
        if color == "yellow":
            self.score += 1
        if color == "green":
            self.score += 3
        if color == "orange":
            self.score += 5
        if color == "red":
            self.score += 7
        self.update_scoreboard()

    def lose_life(self):
        self.life += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
