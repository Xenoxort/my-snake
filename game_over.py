import turtle as t
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

# Freeze game and write out Game Over, when snake dies
class GameOver:
    def __init__(self):
        self.tim = Turtle()
        self.tim.hideturtle()
        self.tim.color("white")
        self.tim.write("Game Over.", align=ALIGNMENT, font=FONT)
        t.done()






