# Filename: week4_jungle.py
# Week4 - Mystery Island (Action 1 Only: Jungle Escape + Score)

import random

name = input("Enter your name: ").strip()
print(f"\nWelcome, {name}! Find the escape direction to leave the island.\n")

# Escape direction is chosen ONCE and stays fixed
escape_dir = random.choice(["north", "south", "east", "west"])

score = 100

while True:
    action = input("Choose: jungle / quit: ").strip().lower()

    if action not in ("jungle", "quit"):
        print("Invalid choice\n")
        continue

    if action == "quit":
        print("You quit the game.")
        break

    direction = input("Pick a direction (north/south/east/west): ").strip().lower()

    if direction not in ("north", "south", "east", "west"):
        print("Invalid direction\n")
        continue

    if direction == escape_dir:
        print("You found the escape route! You escaped the island!")
        break
    else:
        print("Dead end! Try again.")
        score = score - 25

        if score <= 0:
            score = 0
            print("Your score hit 0. Game Over.")
            break

    print()

print("\n=== Final Summary ===")
print(f"Player: {name}")
print(f"Final score: {score}")
