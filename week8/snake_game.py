# snake_game.py
# ─────────────────────────────────────────

import turtle
import random

# ══════════════════════════════════════════
# CONSTANTS  (tweak these to change the game)
# ══════════════════════════════════════════
WIDTH        = 600      # window width  in pixels
HEIGHT       = 600      # window height in pixels
GRID         = 20       # size of each snake segment (pixels)
START_SPEED  = 150      # milliseconds between each move (lower = faster)
SPEED_UP     = 5        # ms faster for every food eaten
MIN_SPEED    = 50       # fastest the game can get

# ══════════════════════════════════════════
# WINDOW SETUP
# ══════════════════════════════════════════
screen = turtle.Screen()
screen.title("🐍 Snake Game")
screen.bgcolor("black")
screen.setup(width=WIDTH + 40, height=HEIGHT + 40)
screen.tracer(0)        # turn off auto-refresh so WE control when to draw

# ══════════════════════════════════════════
# HELPER: create a square turtle
# ══════════════════════════════════════════
def make_square(x, y, color):
    """Create a filled square turtle at position (x, y)."""
    s = turtle.Turtle()
    s.shape("square")
    s.shapesize(GRID / 20)   # turtle "square" default is 20px; scale to GRID
    s.color(color)
    s.penup()
    s.goto(x, y)
    s.speed(0)
    return s

# ══════════════════════════════════════════
# DRAW BORDER
# ══════════════════════════════════════════
def draw_border():
    """Draw the white boundary box."""
    b = turtle.Turtle()
    b.color("white")
    b.penup()
    b.goto(-WIDTH // 2, -HEIGHT // 2)
    b.pendown()
    b.pensize(3)
    for _ in range(4):
        b.forward(WIDTH if b.heading() in (0, 180) else HEIGHT)
        # simpler: just draw a rectangle manually
    b.hideturtle()
    # redo cleanly:
    b.penup()
    b.goto(-WIDTH // 2, -HEIGHT // 2)
    b.pendown()
    b.goto( WIDTH // 2, -HEIGHT // 2)
    b.goto( WIDTH // 2,  HEIGHT // 2)
    b.goto(-WIDTH // 2,  HEIGHT // 2)
    b.goto(-WIDTH // 2, -HEIGHT // 2)
    b.hideturtle()

draw_border()

# ══════════════════════════════════════════
# SCORE DISPLAY
# ══════════════════════════════════════════
score_turtle = turtle.Turtle()
score_turtle.color("white")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, HEIGHT // 2 + 8)

score      = 0
high_score = 0
speed      = START_SPEED   # current delay in ms

def update_score():
    """Redraw the score line at the top."""
    score_turtle.clear()
    score_turtle.write(
        "Score: {}   High Score: {}".format(score, high_score),
        align="center",
        font=("Arial", 14, "bold")
    )

update_score()

# ══════════════════════════════════════════
# SNAKE STATE
# ══════════════════════════════════════════
# segments is a list of turtle objects.
# segments[0] = head.  Last element = tail tip.
segments   = []
direction  = "Right"   # current direction
next_dir   = "Right"   # direction queued by key press (applied at next move)

def create_snake():
    """Build the starting snake (3 segments)."""
    global segments
    for seg in segments:
        seg.hideturtle()   # clean up old segments if restarting
    segments = []
    for i in range(3):
        # start in center; each segment is one GRID step to the left of the previous
        seg = make_square(-i * GRID, 0, "lime green" if i == 0 else "green")
        segments.append(seg)

create_snake()

# ══════════════════════════════════════════
# FOOD
# ══════════════════════════════════════════
food = make_square(0, 0, "red")
food.shape("circle")
food.shapesize(GRID / 20)

def place_food():
    """Move food to a random grid-aligned position inside the boundary."""
    half_w = (WIDTH  // 2 // GRID) * GRID - GRID
    half_h = (HEIGHT // 2 // GRID) * GRID - GRID
    while True:
        fx = random.randrange(-half_w, half_w, GRID)
        fy = random.randrange(-half_h, half_h, GRID)
        # make sure food doesn't spawn ON the snake
        occupied = [(s.xcor(), s.ycor()) for s in segments]
        if (fx, fy) not in occupied:
            food.goto(fx, fy)
            break

place_food()

# ══════════════════════════════════════════
# KEYBOARD CONTROLS
# ══════════════════════════════════════════
# We queue the direction change in next_dir.
# It's applied at the START of move() to prevent
# changing direction twice in one frame.

def go_up():
    global next_dir
    if direction != "Down":    # can't reverse
        next_dir = "Up"

def go_down():
    global next_dir
    if direction != "Up":
        next_dir = "Down"

def go_left():
    global next_dir
    if direction != "Right":
        next_dir = "Left"

def go_right():
    global next_dir
    if direction != "Left":
        next_dir = "Right"

screen.listen()
screen.onkey(go_up,    "Up")
screen.onkey(go_down,  "Down")
screen.onkey(go_left,  "Left")
screen.onkey(go_right, "Right")
# also support WASD
screen.onkey(go_up,    "w")
screen.onkey(go_down,  "s")
screen.onkey(go_left,  "a")
screen.onkey(go_right, "d")

# ══════════════════════════════════════════
# GAME OVER SCREEN
# ══════════════════════════════════════════
game_over_turtle = turtle.Turtle()
game_over_turtle.color("white")
game_over_turtle.penup()
game_over_turtle.hideturtle()

game_running = True

def show_game_over():
    """Display the game over message."""
    game_over_turtle.goto(0, 40)
    game_over_turtle.write(
        "GAME OVER",
        align="center",
        font=("Arial", 36, "bold")
    )
    game_over_turtle.goto(0, -10)
    game_over_turtle.write(
        "Final Score: {}".format(score),
        align="center",
        font=("Arial", 20, "normal")
    )
    game_over_turtle.goto(0, -50)
    game_over_turtle.write(
        "Press R to restart",
        align="center",
        font=("Arial", 14, "normal")
    )

def restart():
    """Reset everything and start a new game."""
    global score, speed, direction, next_dir, game_running
    if game_running:
        return   # ignore R press during active game
    score     = 0
    speed     = START_SPEED
    direction = "Right"
    next_dir  = "Right"
    game_over_turtle.clear()
    create_snake()
    place_food()
    update_score()
    game_running = True
    move()   # restart the game loop

screen.onkey(restart, "r")
screen.onkey(restart, "R")

# ══════════════════════════════════════════
# COLLISION DETECTION
# ══════════════════════════════════════════
def hit_wall(x, y):
    """Return True if (x, y) is outside the boundary."""
    return (abs(x) >= WIDTH  // 2 or
            abs(y) >= HEIGHT // 2)

def hit_self(x, y):
    """Return True if (x, y) overlaps any body segment (skip head)."""
    for seg in segments[1:]:
        if abs(seg.xcor() - x) < GRID // 2 and abs(seg.ycor() - y) < GRID // 2:
            return True
    return False

# ══════════════════════════════════════════
# MAIN GAME LOOP
# ══════════════════════════════════════════
def move():
    """Move the snake one step. Called repeatedly via ontimer()."""
    global direction, score, high_score, speed, game_running

    if not game_running:
        return

    # Apply the queued direction
    direction = next_dir

    # Calculate where the new head should be
    head_x = segments[0].xcor()
    head_y = segments[0].ycor()

    if direction == "Up":
        head_y += GRID
    elif direction == "Down":
        head_y -= GRID
    elif direction == "Left":
        head_x -= GRID
    elif direction == "Right":
        head_x += GRID

    # ── Check collisions BEFORE moving ──────────
    if hit_wall(head_x, head_y) or hit_self(head_x, head_y):
        game_running = False
        if score > high_score:
            high_score = score
        update_score()
        show_game_over()
        screen.update()
        return

    # ── Check if food is eaten ───────────────────
    ate_food = (abs(head_x - food.xcor()) < GRID // 2 and
                abs(head_y - food.ycor()) < GRID // 2)

    if ate_food:
        # Grow: add a new head segment at the new position
        new_seg = make_square(head_x, head_y, "lime green")
        segments.insert(0, new_seg)
        # Recolor old head to body color
        segments[1].color("green")
        # Update score and speed
        score += 1
        if score > high_score:
            high_score = score
        speed = max(MIN_SPEED, speed - SPEED_UP)
        update_score()
        place_food()
    else:
        # Move: shift each segment to the position of the one ahead of it
        # Work from tail to head so no segment overwrites a position we still need
        for i in range(len(segments) - 1, 0, -1):
            prev_x = segments[i - 1].xcor()
            prev_y = segments[i - 1].ycor()
            segments[i].goto(prev_x, prev_y)
        # Move head to new position
        segments[0].goto(head_x, head_y)

    screen.update()                        # refresh screen once per frame
    screen.ontimer(move, speed)            # schedule next frame

# ══════════════════════════════════════════
# START
# ══════════════════════════════════════════
move()
turtle.done()
