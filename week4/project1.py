# EX06 - Mini Project: Mystery Island Escape
# Logic: Find the hidden exit before your energy (score) runs out!

# import random

# ------------------------------------------------------------
# 1. SETUP
# ------------------------------------------------------------
# - Ask for the player's name
# - Set score = 100 (This is your 'Survival Energy')
# - Pick the escape_dir (north, south, east, or west) randomly ONCE.
# - Create a boolean variable 'escaped' and set it to False.

# ------------------------------------------------------------
# 2. MAIN GAME LOOP
# ------------------------------------------------------------
# Use: while True:
#
#   A) Display Status:
#      - Print the player's current Energy (score).
#
#   B) Get Action:
#      - Ask: "Where to? (jungle / beach / camp / quit): "
#      - TIP: Use .lower() on the input so "Jungle" and "jungle" both work!
#
#   C) Validate Action:
#      - If the action isn't one of the 4 options:
#        print "You wander in circles... try a real location."
#        continue (This skips the rest of the loop)

# ------------------------------------------------------------
# 3. ACTION: JUNGLE (The Only Way Out)
# ------------------------------------------------------------
# If action == "jungle":
#   - Ask for a direction: north, south, east, or west.
#   - If direction == escape_dir:
#       - print "You found a hidden boat! You're free!"
#       - escaped = True
#       - break
#   - Else:
#       - print "The thick vines block your path. You lose 25 energy."
#       - score -= 25

# ------------------------------------------------------------
# 4. ACTION: BEACH (The Number Lock Chest)
# ------------------------------------------------------------
# If action == "beach":
#   - "You find a locked supply crate! It needs a code (1-5)."
#   - code = random.randint(1, 5)
#   - guess_str = input("Enter the 1-digit code: ")
#
#   - Check if guess_str.isdigit():
#       - guess = int(guess_str)
#   - Else:
#       - print "That's not even a number!"
#       - continue
#
#   - Logic: 
#       - If guess == code:
#           - print "Success! You found protein bars (+25 energy)."
#           - score += 25
#       - Else:
#           - print "The chest hissed! It was a trap! (-10 energy)."
#           - score -= 10

# ------------------------------------------------------------
# 5. ACTION: CAMP (The Strategy Spot)
# ------------------------------------------------------------
# If action == "camp":
#   - This is where we use Boolean Logic (and/or).
#   - If score < 50 and random.choice([True, False]):
#       - print "A local guide finds you and shares a meal! (+50 energy)"
#       - score += 50
#   - Elif score >= 50:
#       - print "The camp is peaceful, but you're wasting time. (-5 energy)"
#       - score -= 5
#   - Else:
#       - print "Monkeys stole your backpack! (-15 energy)"
#       - score -= 15

# ------------------------------------------------------------
# 6. ACTION: QUIT
# ------------------------------------------------------------
# If action == "quit":
#   - print "You decide to live on the island forever..."
#   - break

# ------------------------------------------------------------
# 7. FINAL CHECKS & ENDING
# ------------------------------------------------------------
# Inside the loop (at the bottom):
#   - If score <= 0:
#       - score = 0
#       - print "You fainted from exhaustion... Game Over."
#       - break
#
# Outside the loop (The Summary):
#   - Print a final summary: "Player: [Name] | Final Score: [Score]"
#   - If escaped == True, print "RESULT: SURVIVED"
#   - Else, print "RESULT: LOST AT SEA"
