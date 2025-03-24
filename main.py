# Imports
from turtle import Turtle, Screen
from food import Food
from score import Score
from snake import Snake

# Setup
width = 600
height = 600

screen = Screen()
screen.setup(width=width, height=height)
screen.title("My Snake Game")
screen.bgcolor("black")

screen.tracer(0)
# Initializing snake and first food
my_snake = Snake()
my_food = Food()

# Initializing Score
my_score = Score()

screen.update()

game_on = True #For now this never turns to False because game ends with turtle.done()
while game_on:
    # Move snake
    my_snake.move_snake()

    # Eating food
    if my_snake.head.distance(my_food) < 15:
        # Delete previous food, create new one
        my_food.new_food()
        screen.update()

        # Increase snake - one more tail
        my_snake.increase_snake()

        # Increase score
        my_score.increase_score()

        # Overwrite best score even during game
        my_score.overwrite_bestscore()

    # Collision with wall
    x_limit = (width / 2) - 20
    y_limit = (height / 2) - 20
    if ((my_snake.head.xcor() > x_limit or my_snake.head.xcor() < -x_limit) or
            (my_snake.head.ycor() > y_limit or my_snake.head.ycor() < -y_limit)):
        my_score.game_over()

    # Collision with tail
    for tail in my_snake.snake_list[2:]:
        if my_snake.head.distance(tail) < 10:
            my_score.game_over()

    # Controlling the Snake with keyboard
    my_snake.control_snake()

screen.exitonclick()