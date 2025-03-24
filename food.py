import random
from turtle import Turtle

#Inherit the Turtle class and create food object
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        x_cor = random.randint(-250, 250)
        y_cor = random.randint(-250, 250)
        self.goto(x_cor, y_cor)







