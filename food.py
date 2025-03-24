import random
from turtle import Turtle

class Food:
    def __init__(self):
        self.food_object = Turtle()
        self.food_object.hideturtle()
        self.food_object.penup()
        self.food_object.color("blue")
        self.new_food()

    def new_food(self):
        x_cor = random.randint(-250, 250)
        y_cor = random.randint(-250, 250)
        self.food_object.goto(x_cor, y_cor)
        self.food_object.dot(15)






