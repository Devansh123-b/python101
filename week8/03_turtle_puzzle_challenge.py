# by devansh
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
t.goto(-60, 120)
t.pendown()
t.color("black", "orange")
t.begin_fill()
t.circle(40)   # circle with radius 40 pixels
t.end_fill()

# --- Shape 3: Small square (a "window" on the wall) ---
t.penup()
t.goto(40, -40)
t.pendown()
t.color("blue", "lightblue")
t.begin_fill()
for i in range(4):
    t.forward(70)
    t.right(90)
t.end_fill()

# --- Shape 4: Triangle (a "roof" — but wait, where is it?) ---
t.penup()
t.goto(0, 0)
t.pendown()
t.color("brown", "peru")
t.begin_fill()
for i in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()

t.hideturtle()
turtle.done()
