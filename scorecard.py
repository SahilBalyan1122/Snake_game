from turtle import Turtle
from variables import HIGH_SCORE_FILE

class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.show_text("Score = "+str(self.score),(0,280))
        self.high_score = self.load_high_score()

    def show_text(self,string,pos=(0,0)):
        self.goto(pos)
        self.write(string, False, "center", ('Arial', 12, 'bold'))

    def load_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        if self.score > self.high_score:
            with open(HIGH_SCORE_FILE, "w") as file:
                file.write(str(self.score))
            self.show_text(f"Congratulations! You beat the previous High Score of {self.high_score}", (0, -40))

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_text("Score = "+str(self.score),(0,280))

    def game_over(self):
        self.show_text("GAME OVER")
        self.save_high_score()
