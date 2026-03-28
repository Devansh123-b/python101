# 🐍 PROJECT: Snake Game in Python Turtle
# ─────────────────────────────────────────────────────────────────

# PROJECT OVERVIEW
# ─────────────────
# Build a fully working Snake game using Python's turtle module.
# The snake moves around the screen, eats food to grow longer,
# and the game ends when the snake hits a wall or its own body.
# This project brings together functions, lists, keyboard events,
# collision detection, and a real-time game loop.

# LEARNING OBJECTIVES
# ────────────────────
# By the end of this project, you will be able to:
#   - Use turtle.onkey() to handle keyboard input
#   - Use turtle.ontimer() to create a game loop
#   - Store snake body segments in a list and update them each frame
#   - Detect collisions with walls and with the snake itself
#   - Use functions to organize a larger program cleanly
#   - Track and display a score using a separate turtle object

# NEW CONCEPTS (things you haven't seen yet)
# ───────────────────────────────────────────
#   - turtle.tracer(0) + turtle.update()  → manual screen refresh (smooth animation)
#   - turtle.onkey(func, "key")           → call a function when a key is pressed
#   - turtle.listen()                     → activate keyboard listening
#   - turtle.ontimer(func, ms)            → call a function every X milliseconds
#   - Lists as a queue: append to front, pop from back = snake movement

# HOW THE GAME WORKS
# ───────────────────
#   1. The snake starts with 3 segments in the center of the screen.
#   2. It moves automatically in the current direction every 150ms.
#   3. Arrow keys change the direction (no reversing into yourself).
#   4. When the head touches the food, the snake grows by 1 segment.
#   5. Food respawns at a random position after being eaten.
#   6. The game ends (and shows GAME OVER) if:
#        a) The head hits any wall boundary, OR
#        b) The head overlaps any body segment

# PROJECT STRUCTURE
# ──────────────────
#   snake_game.py   ← the one file you need to write and run

# MILESTONES (build it step by step)
# ────────────────────────────────────
#   Milestone 1 — Setup (5 min)
#     Draw the game window, black background, set tracer(0)
#
#   Milestone 2 — Snake segments (10 min)
#     Create a list of square turtle objects as body segments
#     Draw them on screen at starting positions
#
#   Milestone 3 — Movement (10 min)
#     Write a move() function that shifts segments forward
#     Use ontimer() to call move() repeatedly
#
#   Milestone 4 — Keyboard controls (5 min)
#     Use onkey() to change direction
#     Block reverse direction (can't go right if currently going left)
#
#   Milestone 5 — Food (10 min)
#     Place a food dot at a random position
#     Detect when the head reaches the food → grow snake → new food
#
#   Milestone 6 — Collision detection (10 min)
#     Check if head hits a wall → game over
#     Check if head overlaps any body segment → game over
#
#   Milestone 7 — Score display (5 min)
#     Use a separate turtle to write the score on screen
#     Update it every time the snake eats food

# CONTROLS
# ─────────
#   Arrow Up    → move up
#   Arrow Down  → move down
#   Arrow Left  → move left
#   Arrow Right → move right

# GRADING RUBRIC
# ───────────────
#   Snake moves smoothly                          10 pts
#   Arrow keys change direction correctly         10 pts
#   Snake grows when eating food                  15 pts
#   Food respawns at random position              10 pts
#   Wall collision ends game                      15 pts
#   Self collision ends game                      15 pts
#   Score displayed and updates correctly         10 pts
#   Code is organized into functions with comments 15 pts
#   TOTAL                                        100 pts

# BONUS CHALLENGES
# ─────────────────
#   +5  Speed increases every 5 foods eaten
#   +5  High score is saved and displayed
#   +10 Wrap-around walls (snake exits right → enters left)
#   +10 Two-player mode (WASD vs arrow keys)
