# Filename: 03_if_elif_else.py
# Python101 - Week 2: if / elif / else (More than two choices)

print("=== if / elif / else ===")

# In Python, the input() function always returns a string (text), even if you type a number. You cannot compare a string to an integer using >=.
score_str = input("Enter your score (0 to 100): ")
# Add int() to convert the text input into a number
score = int(score_str)

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

print()
print("Done.")

# Teaching notes:
# - elif means “else if”
# - Only ONE block runs in a ladder
# - Put the biggest ranges first (90+, then 80+, etc.)
