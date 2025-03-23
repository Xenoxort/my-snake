from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Score:
    def __init__(self, height):
        self.score = -1
        self.tim = Turtle()
        self.tim.hideturtle()
        self.tim.color("white")
        self.tim.penup()
        self.tim.goto(0, height/2 - 30)
        self.tim.pendown()
        self.increase_score()


    def increase_score(self):
        self.tim.clear()
        self.score += 1
        self.tim.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)






