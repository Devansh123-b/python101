# Python101 - Turtle Lesson 3: Puzzle Challenge (Read the Clues!)

# PUZZLE: Follow the clues below to draw a mystery picture.
# Do NOT look ahead — figure out each step before running it.
#
# Clue 1: The picture uses 4 shapes.
# Clue 2: Two shapes are the same type but different sizes and colors.
# Clue 3: One shape has 360 equal steps (think: what is almost a polygon with 360 sides?)
# Clue 4: The last shape is hidden inside another.
#
# Can you guess what the final picture looks like before running it?

import turtle

t = turtle.Turtle()
t.speed(3)

# --- Shape 1: Large filled square (the "room") ---
t.color("black", "lightyellow")
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.right(90)
t.end_fill()

# --- Shape 2: Circle (the "sun" in the top-right corner) ---
t.penup()
t.goto(60, 20)
t.pendown()
t.color("black", "orange")
t.begin_fill()
t.circle(40)   # circle with radius 40 pixels
t.end_fill()

# --- Shape 3: Small square (a "window" on the wall) ---
t.penup()
t.goto(-80, 80)
t.pendown()
t.color("blue", "lightblue")
t.begin_fill()
for i in range(4):
    t.forward(60)
    t.right(90)
t.end_fill()

# --- Shape 4: Triangle (a "roof" — but wait, where is it?) ---
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("brown", "peru")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.hideturtle()
turtle.done()

# Discussion questions for class:
# 1. What was the mystery picture?
# 2. What does t.circle(40) actually draw? (hint: try circle(80) or circle(-40))
# 3. How would you add a door? (rectangle = 2 sides of 40, 2 sides of 80)
# 4. Challenge: rewrite Shape 1 WITHOUT a loop using 4 separate forward/right lines.
