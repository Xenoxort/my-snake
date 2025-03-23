# Imports
import time
import turtle as t
from turtle import Turtle, Screen
from food import Food
from score import Score
from game_over import GameOver

# Setup
width = 600
height = 600

screen = Screen()
screen.setup(width=width, height=height)
screen.title("My Snake Game")
screen.bgcolor("black")

# Initializing the snake
screen.tracer(0)

snake_list = []
y_cor = 0
x_cor = 20
for index in range(3):
    tim = Turtle(shape="square")
    tim.color("white")
    tim.penup()
    tim.goto(x_cor - index * 20, y_cor)

    snake_list.append(tim)

#creating the first food
my_food = Food()

screen.update()


# Keyboard functions
def up():
    if snake_list[0].heading() != 270:
        snake_list[0].setheading(90)

def down():
    if snake_list[0].heading() != 90:
        snake_list[0].setheading(270)

def right():
    if snake_list[0].heading() != 180:
        snake_list[0].setheading(0)

def left():
    if snake_list[0].heading() != 0:
        snake_list[0].setheading(180)

#Initializing Score
my_score = Score(height)


# Snake Movement
screen.listen()



game_on = True
while game_on:
    screen.tracer(0)
    time.sleep(0.1)
    for index in range(len(snake_list)-1, 0, -1):
        snake_list[index].goto(snake_list[index - 1].pos())
    snake_list[0].forward(20)

    if abs(snake_list[0].xcor() - my_food.food_object.xcor()) < 15  and abs(snake_list[0].ycor() - my_food.food_object.ycor()) < 15:
        #delete previous food, create new one
        my_food.food_object.clear()
        del my_food
        my_food = Food()

        #one more tail
        tom = Turtle(shape="square")
        tom.color("white")
        tom.penup()

        tom.goto(snake_list[-1].pos())
        snake_list.append(tom)

        #increase score
        my_score.increase_score()

    # Death - Game over
    # Collision with wall
    if (snake_list[0].xcor() > (width/2 - 5) or snake_list[0].xcor() < -(width/2 - 5)) or (snake_list[0].ycor() > (height/2 - 5) or snake_list[0].ycor() < -(height/2 - 5)):
        game = GameOver()
        game_on = False

    # Collision with tail
    for tail in snake_list[2:]:
        if (abs(snake_list[0].xcor() - tail.xcor()) < 10) and (abs(snake_list[0].ycor() - tail.ycor()) < 10):
            game = GameOver()
            game_on = False

    screen.update()

    # Controlling the Snake with keyboard
    screen.onkey(fun=up, key="Up")
    screen.onkey(fun=down, key="Down")
    screen.onkey(fun=right, key="Right")
    screen.onkey(fun=left, key="Left")





screen.exitonclick()