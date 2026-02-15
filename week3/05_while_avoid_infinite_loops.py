# Filename: 05_while_avoid_infinite_loops.py
# Python101 - Week 3: avoiding infinite loops + sentinel + min/max tracker + continue

print("=== Loop Safety + Trackers ===")

# Part 1: Sentinel loop with min/max + total
print("Enter integers. Type 0 to stop.")
print()

total = 0
count = 0
minimum = None
maximum = None

num = int(input("Number (0 to stop): "))

while num != 0:
    # Example: skip negatives (shows continue)
    if num < 0:
        print("Skipping negatives.")
        num = int(input("Number (0 to stop): "))
        continue

    total = total + num
    count = count + 1

    if minimum is None or num < minimum:
        minimum = num
    if maximum is None or num > maximum:
        maximum = num

    num = int(input("Number (0 to stop): "))

print()
if count == 0:
    print("No positive numbers were entered.")
else:
    average = total / count
    print("Count   =", count)
    print("Total   =", total)
    print("Min     =", minimum)
    print("Max     =", maximum)
    print("Average =", average)

print()
# Part 2: String loop mini-task (character counting)
print("Now: count how many digits are in a message.")
message = input("Type a message: ")

digits = 0
for ch in message:
    if ch >= "0" and ch <= "9":
        digits = digits + 1

print("Digit count =", digits)

print()
print("Done.")

# Teaching notes:
# - Sentinel value: 0 means “stop”
# - Infinite loop prevention: ALWAYS update num inside the while loop
# - min/max trackers are common loop patterns
# - continue is useful to skip unwanted inputs cleanly
# - for ch in message loops through characters of a string
