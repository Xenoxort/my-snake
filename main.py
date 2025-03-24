# Imports
from turtle import Turtle, Screen
from food import Food
from score import Score
from game_over import GameOver
from snake import Snake

# Setup
width = 600
height = 600

screen = Screen()
screen.setup(width=width, height=height)
screen.title("My Snake Game")
screen.bgcolor("black")

# Initializing snake and first food
my_snake = Snake()
my_food = Food()

# Initializing Score
my_score = Score(height, width)

game_on = True #For now this never turns to False because game ends with turtle.done()
while game_on:
    # Move snake
    my_snake.move_snake()

    # Eating food
    my_food = my_snake.eat_food(my_food, my_score)

    # Collision with wall
    my_snake.hit_wall(width, height)

    # Collision with tail
    my_snake.hit_tail()

    # Controlling the Snake with keyboard
    my_snake.control_snake()

screen.exitonclick()