# Python101 - Turtle Lesson 4 (HOMEWORK): Draw a Scene

# GOAL: Use turtle to draw a scene with at least 5 things in it.
#
# Requirements (you must include ALL of these):
#   1. A background color using turtle.bgcolor("color")
#   2. At least ONE filled shape
#   3. At least ONE circle (use t.circle())
#   4. At least ONE use of penup() + goto() + pendown() to move positions
#   5. At least ONE for loop
#   6. Your name in a comment at the top
#
# Ideas for your scene (pick one or make your own!):
#   - Underwater ocean (fish, bubbles, seaweed, rocks)
#   - Outer space (planets, stars, a rocket)
#   - City skyline (buildings, moon, windows)
#   - Emoji faces (happy, sad, surprised)
#
# EXAMPLE STARTER (a very simple house — replace this with YOUR scene):

import turtle

# ── YOUR NAME HERE ──
# Name: _______________

turtle.bgcolor("skyblue")   # set the background color

t = turtle.Turtle()
t.speed(5)

# -- Ground --
t.penup()
t.goto(-300, -100)
t.pendown()
t.color("black", "green")
t.begin_fill()
for i in range(2):
    t.forward(600)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()

# -- House body --
t.penup()
t.goto(-60, -100)
t.pendown()
t.color("black", "white")
t.begin_fill()
for i in range(4):
    t.forward(120)
    t.right(90)
t.end_fill()

# -- Roof --
t.penup()
t.goto(-80, -100)
t.pendown()
t.color("black", "red")
t.begin_fill()
for i in range(3):
    t.forward(160)
    t.left(120)
t.end_fill()

# -- Sun (circle) --
t.penup()
t.goto(180, 80)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.circle(40)
t.end_fill()

t.hideturtle()
turtle.done()

# Teaching notes:
# - turtle.bgcolor() sets the whole background color
# - Students should DELETE the example and write their own scene
# - Encourage creativity — there are no wrong answers here
# - Remind: penup before every goto so they don't draw unwanted lines
