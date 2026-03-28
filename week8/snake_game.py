import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Simple Snake Game")
screen.bgcolor("lightgreen")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off screen updates

# Create snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("blue")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Create food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

# Score
score = 0

# Display score
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# Movement functions
def go_up():
    snake.direction = "up"

def go_down():
    snake.direction = "down"

def go_left():
    snake.direction = "left"

def go_right():
    snake.direction = "right"

# Keyboard controls
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Move snake
def move():
    x = snake.xcor()
    y = snake.ycor()

    if snake.direction == "up":
        snake.sety(y + 20)
    if snake.direction == "down":
        snake.sety(y - 20)
    if snake.direction == "left":
        snake.setx(x - 20)
    if snake.direction == "right":
        snake.setx(x + 20)

# Game loop
while True:
    screen.update()
    time.sleep(0.1)

    move()

    # Check collision with wall
    if (snake.xcor() > 290 or snake.xcor() < -290 or
        snake.ycor() > 290 or snake.ycor() < -290):
        snake.goto(0, 0)
        snake.direction = "stop"
        score = 0
        score_display.clear()
        score_display.write("Score: 0", align="center", font=("Arial", 16, "bold"))

    # Check collision with food
    if snake.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

# Keep window open
turtle.done()
