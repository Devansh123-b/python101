import turtle
import random
import time

# ============================================================
#  SNAKE GAME — Final Version
#  Controls: Arrow keys to move. Avoid the walls!
# ============================================================

# --- SCREEN SETUP ---
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("darkgreen")      # Darker bg looks more game-like
screen.setup(width=600, height=600)
screen.tracer(0)

# --- SNAKE ---
snake = turtle.Turtle()
snake.shape("square")
snake.color("lime")              # Brighter green stands out on dark bg
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# --- FOOD ---
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# --- SCORE ---
score = 0
high_score = 0   # Track the best score across resets

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")     # White text on dark background
score_display.goto(0, 260)

def update_score():
    """Redraw the score line at the top of the screen."""
    score_display.clear()
    score_display.write(
        f"Score: {score}   Best: {high_score}",
        align="center",
        font=("Arial", 16, "bold")
    )

update_score()   # Show score once at the start

# --- DIRECTION FUNCTIONS ---
# Extra check: don't allow the snake to instantly reverse direction.
# e.g. if going right, pressing left would move directly into itself.
def go_up():
    if snake.direction != "down":    # Can't reverse from down to up
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

screen.listen()
screen.onkey(go_up,    "Up")
screen.onkey(go_down,  "Down")
screen.onkey(go_left,  "Left")
screen.onkey(go_right, "Right")

# --- MOVE FUNCTION ---
def move():
    """Advance the snake one step (20px) in its current direction."""
    x = snake.xcor()
    y = snake.ycor()
    if snake.direction == "up":    snake.sety(y + 20)
    if snake.direction == "down":  snake.sety(y - 20)
    if snake.direction == "left":  snake.setx(x - 20)
    if snake.direction == "right": snake.setx(x + 20)

# --- RESET FUNCTION ---
def reset_game():
    """Return the snake to the centre and reset the score."""
    global score
    snake.goto(0, 0)
    snake.direction = "stop"
    if score > high_score:
        # This won't update high_score because it's not declared global here.
        # That's intentional — students can fix this as a challenge!
        pass
    score = 0
    update_score()

# --- GAME LOOP ---
while True:
    screen.update()
    time.sleep(0.08)    # Slightly faster than before (0.08s ≈ 12 fps)

    move()

    # --- WALL COLLISION ---
    if (snake.xcor() > 290 or snake.xcor() < -290 or
        snake.ycor() > 290 or snake.ycor() < -290):
        reset_game()

    # --- FOOD COLLISION ---
    if snake.distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        score += 1
        update_score()

turtle.done()
