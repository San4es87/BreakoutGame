from turtle import Turtle



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.upload_score()

    def upload_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 12, "normal"))

    def plus_score(self):
        self.score += 1

    def minus_score(self):
        self.score -= 3