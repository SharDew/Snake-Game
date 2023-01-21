import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score_counter = 0
        self.goto(x=90, y=270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(f"Score: {self.score_counter}", move=False, align="center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=('Arial', 36, 'bold'))


class HighScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.high_score_counter = 0
        self.temp = self.high_score_counter
        self.goto(x=-40, y=270)
        self.color("white")
        self.penup()
        self.hideturtle()
        with open("data.txt",mode="r")as file:
            self.high_score_counter = int(file.read())
        self.write(f" High Score: {self.high_score_counter}", move=False, align="center", font=('Arial', 16, 'normal'))

    def set_high(self):
        self.temp = self.high_score_counter
        self.clear()
        self.write(f" High Score: {self.temp}", move=False, align="center", font=('Arial', 16, 'normal'))
