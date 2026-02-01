# Python101 - Lesson 5: Calculator + Debugging demos + ASCII sprite

# --- Simple calculator (math feels real fast) ---
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

print()  # blank line

# --- Debugging demo (read errors like clues) ---
print("Python (high-level)")
print("  -> Interpreter (translator)")
print("  -> Assembly (low-level)")
print("  -> Machine code (1s and 0s)")
print("  -> CPU runs instructions")

print()  # blank line

# --- Bonus fun: ASCII “sprite” (Scratch vibe) ---
print("  ^_^  ")
print(" (o o) ")
print("  \\_/  ")

# Debugging challenges (DON'T run these unless you're demoing errors):
#
# 1) SyntaxError (quotes must match)
# print("This will break)
#
# Fix:
# print("This will work")
#
# 2) NameError (names must match exactly)
# score = 10
# print(scor)
#
# Fix:
# score = 10
# print(score)
