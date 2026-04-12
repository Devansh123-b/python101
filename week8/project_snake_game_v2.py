import turtle
import time

# --- SCREEN SETUP ---
screen = turtle.Screen()
screen.title("Snake Game - Version 2")
screen.bgcolor("lightgreen")
screen.setup(width=600, height=600)
screen.tracer(0)

# --- SNAKE ---
snake = turtle.Turtle()
snake.shape("square")
snake.color("blue")
snake.penup()
snake.goto(0, 0)

# We store the current direction as a custom attribute on the snake object.
# "stop" means the snake hasn't started moving yet.
snake.direction = "stop"

# --- FOOD (still fixed) ---
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)

# --- SCORE DISPLAY ---
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# --- DIRECTION FUNCTIONS ---
# Each function updates the snake's direction when a key is pressed.
# We don't move here — movement happens in the game loop.
def go_up():
    snake.direction = "up"

def go_down():
    snake.direction = "down"

def go_left():
    snake.direction = "left"

def go_right():
    snake.direction = "right"

# --- KEYBOARD CONTROLS ---
# Tell the screen to listen for key presses, then link keys to functions
screen.listen()
screen.onkey(go_up,    "Up")
screen.onkey(go_down,  "Down")
screen.onkey(go_left,  "Left")
screen.onkey(go_right, "Right")

# --- MOVE FUNCTION ---
# Called every game loop tick to shift the snake one step in its direction.
# Each step is 20 pixels — same as the snake's square size.
def move():
    x = snake.xcor()   # Current x position
    y = snake.ycor()   # Current y position

    if snake.direction == "up":
        snake.sety(y + 20)   # Move up (larger y = up in turtle)
    if snake.direction == "down":
        snake.sety(y - 20)
    if snake.direction == "left":
        snake.setx(x - 20)
    if snake.direction == "right":
        snake.setx(x + 20)

# --- GAME LOOP ---
while True:
    screen.update()
    time.sleep(0.1)

    move()   # Move snake every tick

    # --- WALL COLLISION ---
    # The play area goes from -290 to 290 (leaving 10px border).
    # If the snake goes past any wall, reset it to the centre.
    if (snake.xcor() > 290 or snake.xcor() < -290 or
        snake.ycor() > 290 or snake.ycor() < -290):
        
        snake.goto(0, 0)          # Return to centre
        snake.direction = "stop"  # Stop moving until player presses a key

turtle.done()
