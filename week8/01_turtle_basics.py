# Python101 - Turtle Lesson 1: Basics (Movement + Shapes)

import turtle

t = turtle.Turtle()
t.speed(5)  # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

# --- Draw a square ---
# A square has 4 sides and 4 corners (90° each)
t.color("blue")
for i in range(4):
    t.forward(100)
    t.right(90)

# --- Move without drawing ---
t.penup()       # lift the pen so we don't draw while moving
t.goto(150, 0)  # jump to a new position (0,0 is the center)
t.pendown()     # put the pen back down

# --- Draw a triangle ---
# A triangle has 3 corners: 360 ÷ 3 = 120° per turn
t.color("red")
for i in range(3):
    t.forward(100)
    t.left(120)

turtle.done()   # keeps the window open

# Teaching notes:
# - import turtle loads the drawing library
# - t = turtle.Turtle() creates your turtle (like a pen on screen)
# - forward/backward move in pixels; left/right rotate in degrees
# - The 360° rule: total turning for any shape = 360°
# - penup/pendown let you move without drawing
# - goto(x, y) jumps to exact coordinates
