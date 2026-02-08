# Filename: 04_boolean_logic.py
# Python101 - Week 2: Boolean logic (and / or / not)

print("=== Boolean Logic ===")

age = int(input("Age: ").strip())
has_ticket = input("Do you have a ticket? (yes/no): ").strip().lower()

print()  # blank line

# AND: both must be true
if age >= 13 and has_ticket == "yes":
    print("You may enter.")
else:
    print("You may NOT enter.")

print()  # blank line

day = input("Day (sat/sun/mon/tue/wed/thu/fri): ").strip().lower()

# OR: at least one must be true
if day == "sat" or day == "sun":
    print("It's the weekend.")
else:
    print("It's a weekday.")

print()  # blank line

homework_done = input("Homework done? (yes/no): ").strip().lower() == "yes"

# NOT: flips True/False
if not homework_done:
    print("Do homework first.")
else:
    print("Free time!")

print()
print("Done.")

# Teaching notes:
# - and = both conditions must be True
# - or  = at least one condition must be True
# - not = flips a boolean value
