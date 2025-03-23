import turtle as t
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class GameOver:
    def __init__(self):
        self.tim = Turtle()
        self.tim.hideturtle()
        self.tim.color("white")
        self.tim.write("Game Over.", align=ALIGNMENT, font=FONT)
        t.done()






