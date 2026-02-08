# Filename: 02_if_else.py
# Python101 - Week 2: if / else (Two choices)

print("=== if / else ===")

answer = input("Do you like pizza? (yes/no): ").strip().lower()

if answer == "yes":
    print("Nice! Pizza is popular.")
else:
    print("All good. Everyone likes different food.")

print()
print("Done.")

# Teaching notes:
# - if runs when the condition is True
# - else runs when the condition is False
# - .strip() removes extra spaces
# - .lower() makes the answer lowercase
