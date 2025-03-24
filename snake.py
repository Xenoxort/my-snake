import time
from turtle import Turtle, Screen
from score import Score

Y_COR = 0
X_COR = 20

screen = Screen()


class Snake(Score):
    def __init__(self):
        super().__init__()
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    # Create initial snake
    def create_snake(self):
        screen.tracer(0)
        for index in range(3):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(X_COR - index * 20, Y_COR)
            self.snake_list.append(tim)
        screen.update()

    # Handle snake movement
    def move_snake(self):
        screen.tracer(0)
        time.sleep(0.1)
        for index in range(len(self.snake_list) - 1, 0, -1):
            self.snake_list[index].goto(self.snake_list[index - 1].pos())
        self.head.forward(20)
        
        screen.update()
    
    # Increase snake when eating food
    def increase_snake(self):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()

        tim.goto(self.snake_list[-1].pos())
        self.snake_list.append(tim)

    # Handling eating food
    def eat_food(self, my_food):
        if self.head.distance(my_food) < 15:
            # Delete previous food, create new one
            my_food.new_food()

            # Increase snake - one more tail
            self.increase_snake()

            # Increase score
            self.increase_score()

            # Overwrite best score even during game
            self.overwrite_bestscore()

        return my_food

    #Keyboard functions
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    # Game ends when snake hits the wall
    def hit_wall(self, width, height):
        x_limit = (width / 2) - 20
        y_limit = (height / 2) - 20
        if ((self.head.xcor() > x_limit or self.head.xcor() < -x_limit) or
            (self.head.ycor() > y_limit or self.head.ycor() < -y_limit)):
            self.game_over()

    # Game ends when snake hits the tail
    def hit_tail(self):
        for tail in self.snake_list[2:]:
            if ((abs(self.head.xcor() - tail.xcor()) < 10) and
                (abs(self.head.ycor() - tail.ycor()) < 10)):
                self.game_over()

            
    # Control snake
    def control_snake(self):
        screen.listen()
        screen.onkey(fun=self.up, key="Up")
        screen.onkey(fun=self.down, key="Down")
        screen.onkey(fun=self.right, key="Right")
        screen.onkey(fun=self.left, key="Left")