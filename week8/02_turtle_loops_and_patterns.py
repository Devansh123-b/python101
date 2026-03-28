# Python101 - Turtle Lesson 2: Loops + Patterns (Star & Spiral)

import turtle

t = turtle.Turtle()
t.speed(0)  # fastest — spiral has many steps

# --- Part A: Filled 5-pointed star ---
# A star turns 144° each point: 720° total ÷ 5 = 144°
t.color("black", "gold")  # pen color, fill color
t.begin_fill()
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

# --- Part B: Rainbow spiral ---
t.penup()
t.goto(-200, -150)
t.pendown()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(150):
    t.color(colors[i % 6])  # i % 6 cycles through 0,1,2,3,4,5,0,1,2...
    t.forward(i * 2)        # gets longer each step → creates the spiral
    t.left(59)              # 59° gives a nice open spiral shape

t.hideturtle()
turtle.done()

# Teaching notes:
# - begin_fill() / end_fill() fills the shape with fillcolor
# - colors[i % 6] is the "modulo trick" to cycle through a list
# - Changing the angle in the spiral (try 61°, 90°, 120°) gives very different shapes
# - hideturtle() removes the arrow at the end for a cleaner look
