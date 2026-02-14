# Filename: 04_while_guessing_game.py
# Python101 - Week 3: while loops + counter + input validation + continue

print("=== Guessing Game (with attempts) ===")
print("Secret number is between 1 and 10.")
print("Type -1 to quit.")
print()

secret = 7
attempts = 0

guess = int(input("Your guess: "))

while guess != secret and guess != -1:
    # Input validation
    if guess < 1 or guess > 10:
        print("Invalid. Enter a number from 1 to 10 (or -1 to quit).")
        guess = int(input("Your guess: "))
        continue  # skip the rest and restart the loop

    attempts = attempts + 1

    if guess < secret:
        print("Too low.")
    else:
        print("Too high.")

    guess = int(input("Try again: "))

if guess == secret:
    attempts = attempts + 1  # count the final correct guess
    print()
    print("Correct! The secret was", secret)
    print("Attempts:", attempts)
else:
    print()
    print("You quit. The secret was", secret)

print("Done.")

# Teaching notes:
# - attempts is a counter (counts how many tries)
# - continue skips the rest of the loop body and restarts the loop
# - Always update guess inside the loop to avoid infinite loops
