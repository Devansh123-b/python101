# Python101 - Turtle Lesson 5 (HOMEWORK): Variables + User Input

# GOAL: Make your turtle program interactive using variables and input().
#
# New concepts in this file:
#   - Storing values in variables (size, color, sides)
#   - Using input() to ask the user a question
#   - int() to convert text input into a number
#   - Using a variable inside t.forward() and t.right()
#
# The 360° formula for any polygon:
#   angle = 360 / number_of_sides
#
# EXAMPLE: A shape-drawing program where the user picks the sides and size.

import turtle

# --- Ask the user for input ---
sides = int(input("How many sides? (3 = triangle, 4 = square, 5 = pentagon...): "))
size  = int(input("How long should each side be? (try 50 to 200): "))
color = input("What color? (red, blue, green, purple, orange...): ")

# --- Calculate the turning angle ---
angle = 360 / sides   # the 360° rule

# --- Draw the shape ---
t = turtle.Turtle()
t.speed(5)
t.color(color)
t.begin_fill()

for i in range(sides):
    t.forward(size)
    t.right(angle)

t.end_fill()
t.hideturtle()
turtle.done()

# --- CHALLENGE: extend this program ---
# Try adding these one at a time:
#
# Challenge A: Ask for a fill color separately (use t.fillcolor())
#
# Challenge B: Draw 3 copies of the shape side by side
#   Hint: use penup(), goto(x, 0), pendown() between each shape
#         and change x each time (e.g., 0, 200, 400)
#
# Challenge C: Draw the shape 6 times in a circle (like a flower)
#   Hint: after drawing each shape, turn the turtle by 60°
#         then draw again — repeat 6 times in an outer loop

# Teaching notes:
# - int() is needed because input() always returns a string
# - angle = 360 / sides is the key formula — emphasize this
# - Students who finish early should attempt Challenge B or C
