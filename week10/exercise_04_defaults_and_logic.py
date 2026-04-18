# ============================================================
# EXERCISE 4: Default Parameters & Logic Inside Functions
# ============================================================
# TOPIC: Default argument values, if/else inside functions
# DIFFICULTY: ⭐⭐⭐ (Medium)
#
# REMINDER — default parameter syntax:
#
#   def greet(name, greeting="Hello"):
#       print(greeting, name)
#
#   greet("Sam")             → "Hello Sam"    (uses default)
#   greet("Sam", "Howdy")    → "Howdy Sam"    (overrides default)
# ============================================================

# ------------------------------------------------------------
# TASK 1
# Define a function called "repeat_word" that takes:
#   - "word"  (a string)
#   - "times" (an integer, DEFAULT value = 3)
#
# It should RETURN a string with the word repeated that many
# times, separated by spaces.
#
# Expected results:
#   repeat_word("ha")        → "ha ha ha"
#   repeat_word("yes", 5)    → "yes yes yes yes yes"
#   repeat_word("no", 1)     → "no"
#
# Hint: " ".join(["ha", "ha", "ha"])  gives "ha ha ha"
# Hint: [word] * times  gives a list with word repeated
# ------------------------------------------------------------

# 👉 Write your function here:


# 👉 Test all three cases:


# ------------------------------------------------------------
# TASK 2
# Define a function called "bmi_category" that takes:
#   - "weight_kg"  (a float, person's weight in kg)
#   - "height_m"   (a float, person's height in metres)
#
# It should:
#   1. Calculate BMI = weight_kg / (height_m ** 2)
#   2. RETURN the category as a string:
#        BMI < 18.5            → "Underweight"
#        18.5 ≤ BMI < 25.0     → "Normal weight"
#        25.0 ≤ BMI < 30.0     → "Overweight"
#        BMI ≥ 30.0            → "Obese"
#
# Test with: (50, 1.70), (70, 1.75), (90, 1.70), (110, 1.65)
# Print in the format:  "Weight: 70kg, Height: 1.75m → Normal weight"
# ------------------------------------------------------------

# 👉 Write your function here:


# 👉 Test all four cases:


# ------------------------------------------------------------
# TASK 3
# Define a function called "make_username" that takes:
#   - "first_name"  (string)
#   - "last_name"   (string)
#   - "include_number" (boolean, DEFAULT = False)
#   - "number"         (integer, DEFAULT = 1)
#
# Rules:
#   - Username = first letter of first_name + full last_name,
#     all in lowercase.
#   - If include_number is True, add the number at the end.
#
# Expected results:
#   make_username("Alice", "Smith")              → "asmith"
#   make_username("Bob",   "Jones", True)        → "bjones1"
#   make_username("Maya",  "Patel", True, 42)    → "mpatel42"
# ------------------------------------------------------------

# 👉 Write your function here:


# 👉 Test all three cases:


# ============================================================
# CHALLENGE (optional)
# Define a function "fizzbuzz" that takes a number n.
# Return:
#   "FizzBuzz" if divisible by both 3 and 5
#   "Fizz"     if divisible by 3 only
#   "Buzz"     if divisible by 5 only
#   The number itself (as a string) otherwise
#
# Then call it for every number from 1 to 30 and print each.
# ============================================================

# 👉 Write your challenge function here (optional):
