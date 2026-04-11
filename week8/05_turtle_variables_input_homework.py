import turtle
#Challenge A&B
sides = int(input("How many sides? (3 = triangle, 4 = square, 5 = pentagon...): "))
size  = int(input("How long should each side be? (try 50 to 200): "))
color = input("What color? (red, blue, green, purple, orange...): ")
fill = input("what color to fill the shape with? (red, blue, green, purple, orange...): ")
# --- Calculate the turning angle ---
angle = 360 / sides   # the 360° rule
t = turtle.Turtle()
t.speed(5)
t.penup()
t.goto(-200,0)
t.pendown()
for i in range(3):
 t.penup()
 t.forward(60)
 t.pendown()
 t.color(color)
 t.begin_fill()
 t.fillcolor(fill)
 t.begin_fill()
 for i in range(sides):
    t.forward(size)
    t.right(angle)
 t.end_fill()
t.hideturtle()
turtle.done()


#Challenge C
# name: devansh
# --- Ask the user for input ---
sides = int(input("How many sides? (3 = triangle, 4 = square, 5 = pentagon...): "))
size  = int(input("How long should each side be? (try 50 to 200): "))
color = input("What color? (red, blue, green, purple, orange...): ")
fill = input("what color to fill the shape with? (red, blue, green, purple, orange...): ")
# --- Calculate the turning angle ---
angle = 360 / sides   # the 360° rule

# --- Draw the shape ---
t = turtle.Turtle()
t.speed(5)
t.penup()
t.goto(-200,0)
t.pendown()
for i in range(6):
 t.penup()
 t.forward(1)
 t.pendown()
 t.color(color)
 t.begin_fill()
 t.fillcolor(fill)
 t.begin_fill()
 for r in range(sides):
    t.forward(size)
    t.right(angle)
 t.end_fill()
 t.left(angle/2)
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
