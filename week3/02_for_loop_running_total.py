# Filename: 02_for_loop_running_total.py
# Python101 - Week 3: repetition and automation (running total)

print("=== Running Total ===")

total = 0

print("We will add 5 numbers.")
for i in range(1, 6):
    num = int(input("Enter number #" + str(i) + ": "))
    total = total + num
    print("Current total =", total)

print()
print("Final total =", total)
print("Done.")

# Teaching notes:
# - A loop repeats code many times
# - total = total + num is an accumulator pattern
# - str(i) is used to build a nicer prompt
