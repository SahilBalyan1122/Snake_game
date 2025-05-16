from turtle import Turtle

class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.score = 0
        self.show_text("Score = "+str(self.score))

    def show_text(self,string):
        self.write(string, False, "center", ('Arial', 12, 'bold'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_text("Score = "+str(self.score))

    def game_over(self):
        self.goto(0,0)
        self.show_text("GAME OVER")
