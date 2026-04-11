import turtle
import random
import time

# --- SCREEN SETUP ---
screen = turtle.Screen()
screen.title("Snake Game - Version 3")
screen.bgcolor("lightgreen")
screen.setup(width=600, height=600)
screen.tracer(0)

# --- SNAKE ---
snake = turtle.Turtle()
snake.shape("square")
snake.color("blue")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# --- FOOD ---
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

# --- SCORE ---
# We track score as a plain integer variable
score = 0

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

# --- DIRECTION FUNCTIONS ---
def go_up():    snake.direction = "up"
def go_down():  snake.direction = "down"
def go_left():  snake.direction = "left"
def go_right(): snake.direction = "right"

screen.listen()
screen.onkey(go_up,    "Up")
screen.onkey(go_down,  "Down")
screen.onkey(go_left,  "Left")
screen.onkey(go_right, "Right")

# --- MOVE FUNCTION ---
def move():
    x = snake.xcor()
    y = snake.ycor()
    if snake.direction == "up":    snake.sety(y + 20)
    if snake.direction == "down":  snake.sety(y - 20)
    if snake.direction == "left":  snake.setx(x - 20)
    if snake.direction == "right": snake.setx(x + 20)

# --- HELPER: update the score text on screen ---
# We separate this into its own function to avoid repeating three lines everywhere
def update_score():
    score_display.clear()   # Erase the old text
    score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

# --- GAME LOOP ---
while True:
    screen.update()
    time.sleep(0.1)

    move()

    # --- WALL COLLISION ---
    if (snake.xcor() > 290 or snake.xcor() < -290 or
        snake.ycor() > 290 or snake.ycor() < -290):
        snake.goto(0, 0)
        snake.direction = "stop"
        score = 0           # Reset score on wall hit
        update_score()

    # --- FOOD COLLISION ---
    # distance() measures how far apart two turtles are.
    # If the snake is within 20 pixels of the food, it "eats" it.
    if snake.distance(food) < 20:
        # Move food to a new random position inside the walls
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        food.goto(new_x, new_y)

        score += 1      # Increase score by 1
        update_score()

turtle.done()
