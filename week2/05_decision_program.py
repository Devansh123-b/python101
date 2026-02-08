# Filename: 05_decision_program.py
# Python101 - Week 2: Decision-making program (Movie Picker)

print("=== Movie Picker ===")

funny = input("Do you want a funny movie? (yes/no): ").strip().lower() == "yes"
action = input("Do you want an action movie? (yes/no): ").strip().lower() == "yes"

print()  # blank line

# Rules:
# funny AND action         -> "Superhero Comedy"
# funny AND NOT action     -> "Cartoon"
# NOT funny AND action     -> "Action Adventure"
# NOT funny AND NOT action -> "Mystery"

if funny and action:
    print("You should watch: Superhero Comedy 🦸😂")
elif funny and (not action):
    print("You should watch: Cartoon 🐭")
elif (not funny) and action:
    print("You should watch: Action Adventure 🏃💥")
else:
    print("You should watch: Mystery 🕵️")

print()
print("Done.")

# Teaching notes:
# - We turned answers into booleans (True/False)
# - Then we used if/elif/else to match the correct rule
# - This is how real apps make decisions
