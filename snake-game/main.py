from turtle import Screen
from snake import Snake
import time

# sets up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

game_on = True
while game_on:
    # makes the parts of the snake move together
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
