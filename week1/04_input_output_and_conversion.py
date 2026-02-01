# Python101 - Lesson 4: input() + output + converting text to numbers

name = input("What is your name? ")
print("Hello,", name)

print()  # blank line

# input() always gives text (a string), even if the user types 12
age_text = input("How old are you? ")
age = int(age_text)  # convert text -> number (integer)

print("Next year you will be", age + 1)

# Teaching notes:
# - input() is like Scratch "ask and wait"
# - int(...) converts text like "12" into the number 12
# - If the user types something non-numeric, int(...) will error (that's okay for now)
