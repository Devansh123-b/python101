# Filename: 03_for_loop_pattern_printer.py
# Python101 - Week 3: for loops + patterns + iterating over a string

print("=== Pattern Printer + String Loop ===")

rows = int(input("How many rows? "))

print()
print("Triangle pattern:")
for r in range(1, rows + 1):
    print("*" * r)

print()
print("Square pattern (using repetition):")
for r in range(1, rows + 1):
    print("#" * rows)

print()
print("Square pattern (nested loop version):")
# Nested loops: one loop for rows, one loop for columns
for r in range(1, rows + 1):
    line = ""
    for c in range(1, rows + 1):
        line = line + "@"
    print(line)

print()
print("Iterating over a string (characters):")
word = input("Type a word: ").strip()

vowels = 0
for ch in word.lower():
    if ch in "aeiou":
        vowels = vowels + 1

print("Vowel count =", vowels)

print()
print("Done.")
