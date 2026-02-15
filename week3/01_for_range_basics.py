# Filename: 01_for_range_basics.py
# Python101 - Week 3: for loops + range()

print("=== for + range() Basics ===")

print("Count from 1 to 5:")
for i in range(1, 6):
    print(i)

print()
print("Count by 2s from 0 to 10:")
for i in range(0, 11, 2):
    print(i)

print()
print("Countdown from 5 to 1:")
for i in range(5, 0, -1):
    print(i)

print()
print("Done.")

# Teaching notes:
# - range(start, stop, step)
# - stop is NOT included
# - step can be negative for countdowns
