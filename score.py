from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Score:
    def __init__(self, height, width):
        # current score
        self.score = -1
        self.tim = Turtle()
        self.tim.hideturtle()
        self.tim.color("white")
        self.tim.penup()
        self.tim.goto(0, height/2 - 30)
        self.tim.pendown()
        self.increase_score()

        # best score
        self.best = self.best_score()
        self.tom = Turtle()
        self.tom.hideturtle()
        self.tom.color("white")
        self.tom.penup()
        self.tom.goto(-(width / 2 - 70), height / 2 - 30)
        self.tom.pendown()
        self.tom.write(f"Best Score: {self.best}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.tim.clear()
        self.score += 1
        self.tim.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def best_score(self):
        with open("best_score.txt", mode="r") as b_file:
            best_score = b_file.read()

        return int(best_score)

    def overwrite_bestscore(self):
        try:
            if self.score > self.best_score():
                with open("best_score.txt", mode="w") as file:
                    file.write(f"{self.score}")
        except FileNotFoundError:
            with open("best_score.txt", mode="w") as file:
                file.write(f"{self.score}")



