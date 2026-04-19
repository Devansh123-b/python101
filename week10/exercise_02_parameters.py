# ============================================================
# EXERCISE 2: Functions with Parameters
# ============================================================
# TOPIC: Passing arguments into functions
# DIFFICULTY: ⭐⭐ (Easy-Medium)
#
# Remember: parameters go inside the parentheses of "def".
# Arguments are the actual values you pass when you call it.
#
#   def say_hi(name):       ← "name" is the PARAMETER
#       print("Hi", name)
#
#   say_hi("Alice")         ← "Alice" is the ARGUMENT
# ============================================================

# ------------------------------------------------------------
# TASK 1
# Define a function called "introduce" that takes TWO
# parameters: "name" and "age".
# It should print something like:
#   "My name is Alex and I am 12 years old."
#
# Then call it with:
#   - your own name and age
#   - a friend's name and age
# ------------------------------------------------------------

#Section 1: Task 1 
def introduce(name,age):
  print("my name is ",name,"and I am",age,"years old")
introduce("Devansh", 11)
introduce("Hanse", 12)
# ------------------------------------------------------------
# TASK 2
# Define a function called "print_rectangle" that takes
# TWO parameters: "width" and "height".
# It should print a rectangle made of "#" characters.
#
# Example — print_rectangle(4, 3) should print:
#   ####
#   ####
#   ####
#
# Hint: use a for loop and string multiplication
# Hint: print("#" * width)  prints "####" when width is 4
# ------------------------------------------------------------

#Section 2: Task 2
def print_rectangle(height,width): 
 for i in range(height):
  print("#" * width)

print_rectangle(4, 5)
print_rectangle(2, 10)
print_rectangle(6, 3)
print_rectangle(3, 7)


# ------------------------------------------------------------
# TASK 3
# Define a function called "temperature_message" that takes
# ONE parameter: "temp" (a number in Celsius).
# It should print:
#   - "It's freezing!" if temp is below 0
#   - "It's cold."     if temp is 0 to 14
#   - "It's warm."     if temp is 15 to 24
#   - "It's hot!"      if temp is 25 or above
#
# Call it with temperatures: -5, 10, 20, 35
# ------------------------------------------------------------

#Section 3: Task 3
def temperature_message(temp):
  if temp < 0:
    print("It's freezing!")
  elif temp < 15:
    print("It's cold!")
  elif temp < 25:
    print("It's warm!")
  else:
    print("It's hot!")

temperature_message(-5)
print("")
temperature_message(10)
print("")
temperature_message(20)
print("")
temperature_message(35)
print("")


# ============================================================
# CHALLENGE (optional)
# Define a function "multiply_and_describe" that takes
# two numbers and prints:
#   "5 times 6 equals 30"   (for inputs 5 and 6)
# Call it with three different pairs of numbers.
# ============================================================

#Section 4: CHALLENGE
def multiply_and_describe(n1,n2):
  sum = n1 * n2
  print("",n1,"multiplied by",n2,"equals",sum)
  print("-" * 20)
multiply_and_describe(3, 4)
multiply_and_describe(5, 6)
multiply_and_describe(7, 8)
