import time
from turtle import Screen, Turtle
from snake import Snake

# Create screen
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create snake
snake = Snake()

# Event Listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start game
game_on = True

while game_on:
    screen.update()  # Update screen after each segment is moved
    time.sleep(0.1)

    snake.move()


screen.exitonclick()