from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "bold"))
        self.goto(0, 190)
        self.write(":", align="center", font=("Courier", 80, "bold"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "bold"))

    def point(self, winner):
        if winner == "l":
            self.l_score += 1
        elif winner == "r":
            self.r_score += 1
