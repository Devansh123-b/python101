import turtle
import time

# --- SCREEN SETUP ---
# Create the game window and configure it
screen = turtle.Screen()
screen.title("Snake Game - Version 1")
screen.bgcolor("lightgreen")       # Background color of the play area
screen.setup(width=600, height=600)  # Window size in pixels
screen.tracer(0)                   # Disable auto-refresh (we'll do it manually)

# --- SNAKE ---
# The snake is just a single blue square for now
snake = turtle.Turtle()
snake.shape("square")   # Built-in turtle shape
snake.color("blue")
snake.penup()           # Lift the pen so moving doesn't draw a line
snake.goto(0, 0)        # Place snake at the centre of the screen

# --- FOOD ---
# The food is a red circle sitting at a fixed spot
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100, 100)     # Fixed position for now (will be random later)

# --- SCORE DISPLAY ---
# A hidden turtle used only to write text on screen
score_display = turtle.Turtle()
score_display.hideturtle()   # Don't show the turtle arrow itself
score_display.penup()
score_display.goto(0, 260)   # Top-centre of the window
score_display.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# --- GAME LOOP ---
# This loop keeps the window alive and refreshes the screen
# Right now it does nothing except redraw 10 times per second
while True:
    screen.update()   # Manually push the latest frame to the screen
    time.sleep(0.1)   # Wait 0.1 seconds → ~10 frames per second

# Required to keep the window open (unreachable here, but good habit)
turtle.done()
