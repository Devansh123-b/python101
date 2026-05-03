# ============================================================
# Grade 7 – Python 101 – Week 11 Practice Problems
# Topic: Functions that Return Values
# ============================================================
# In this file you will find TWO problems to complete.
# Read every comment carefully before writing your code.
# Each problem should take you about 10 minutes.
# ============================================================


# ============================================================
# PROBLEM 1: Temperature Converter
# DIFFICULTY: ⭐⭐ (Easy-Medium)
# ============================================================
# A function can take a value, calculate something, and
# RETURN the result — just like a calculator.
#
# You will write two functions that convert temperatures
# between Celsius and Fahrenheit.
#
# Formulas:
#   Celsius → Fahrenheit :  F = (C × 9/5) + 32
#   Fahrenheit → Celsius :  C = (F − 32) × 5/9
# ============================================================


# ------------------------------------------------------------
# STEP 1
# Define a function called "celsius_to_fahrenheit" that:
#   - Takes ONE number called "celsius"
#   - RETURNS the temperature converted to Fahrenheit
#
# Hint: round(result, 1) rounds to 1 decimal place
# ------------------------------------------------------------

# 👉 Write celsius_to_fahrenheit here:


# ------------------------------------------------------------
# STEP 2
# Define a function called "fahrenheit_to_celsius" that:
#   - Takes ONE number called "fahrenheit"
#   - RETURNS the temperature converted to Celsius
#
# Hint: round(result, 1) rounds to 1 decimal place
# ------------------------------------------------------------

# 👉 Write fahrenheit_to_celsius here:


# ------------------------------------------------------------
# STEP 3
# Test both functions by printing the four conversions below.
#
# Expected output:
#   0 C = 32.0 F
#   100 C = 212.0 F
#   32 F = 0.0 C
#   98.6 F = 37.0 C
# ------------------------------------------------------------

# 👉 Print celsius_to_fahrenheit(0)   — expected: 32.0


# 👉 Print celsius_to_fahrenheit(100) — expected: 212.0


# 👉 Print fahrenheit_to_celsius(32)  — expected: 0.0


# 👉 Print fahrenheit_to_celsius(98.6) — expected: 37.0


print("---")


# ------------------------------------------------------------
# CHALLENGE (optional)
# Define a function called "describe_weather" that:
#   - Takes ONE number: "celsius"
#   - RETURNS a string describing the weather:
#       30 and above → "Hot"
#       20 – 29      → "Warm"
#       10 – 19      → "Cool"
#       Below 10     → "Cold"
#
# Then call it and print the result for a few temperatures.
# ------------------------------------------------------------

# 👉 Write describe_weather here (optional):


# 👉 Test describe_weather with at least 3 temperatures (optional):


print("=" * 50)


# ============================================================
# PROBLEM 2: Pizza Price Calculator
# DIFFICULTY: ⭐⭐⭐ (Medium)
# ============================================================
# Big programs are built from SMALL functions that call
# each other. You will write three helper functions, then
# combine them inside one main function.
#
# Pizza pricing rules:
#   Base price  →  small = $8 | medium = $12 | large = $16
#   Toppings    →  each topping costs $1.50
#   Tax         →  13% added to the subtotal
# ============================================================


# ------------------------------------------------------------
# STEP 1
# Define a function called "get_base_price" that:
#   - Takes ONE string: "size"  ("small", "medium", "large")
#   - RETURNS the base price as a number:
#       "small"  → 8
#       "medium" → 12
#       "large"  → 16
#       anything else → 0
# ------------------------------------------------------------

# 👉 Write get_base_price here:


# ------------------------------------------------------------
# STEP 2
# Define a function called "add_toppings_cost" that:
#   - Takes ONE number: "num_toppings"
#   - RETURNS the total topping cost
#     (each topping costs 1.50)
# ------------------------------------------------------------

# 👉 Write add_toppings_cost here:


# ------------------------------------------------------------
# STEP 3
# Define a function called "apply_tax" that:
#   - Takes ONE number: "price"
#   - RETURNS the price after adding 13% tax
#
# Hint: round(result, 2) rounds to 2 decimal places
# ------------------------------------------------------------

# 👉 Write apply_tax here:


# ------------------------------------------------------------
# STEP 4
# Define a function called "print_order" that takes:
#   - customer_name  (string)
#   - size           (string: "small", "medium", or "large")
#   - num_toppings   (number)
#
# Inside print_order you must:
#   1. CALL get_base_price  to get the base price
#   2. CALL add_toppings_cost to get the topping cost
#   3. Add them together to get the subtotal
#   4. CALL apply_tax to get the final total
#   5. Print a receipt that looks exactly like this:
#
#   ==============================
#           PIZZA ORDER
#   ==============================
#   Customer  : Sam Rivera
#   Size      : medium
#   Toppings  : 3
#   Subtotal  : $13.50
#   Total     : $15.26
#   ==============================
#
# Hint: use round(subtotal, 2) when printing the subtotal
# Hint: "$" + str(price) puts a dollar sign in front
# ------------------------------------------------------------

# 👉 Write print_order here (it must call all three helpers!):


# ------------------------------------------------------------
# STEP 5
# Test your pizza system by calling print_order at least TWICE
# with different customers, sizes, and topping counts.
# Make sure you try different sizes so all three prices appear.
# ------------------------------------------------------------

# 👉 Call print_order for customer 1:


# 👉 Call print_order for customer 2:


# ------------------------------------------------------------
# CHALLENGE (optional)
# Define a function called "is_good_deal" that:
#   - Takes ONE number: the final total price
#   - RETURNS True if the total is under $15, False otherwise
#
# Then update print_order to also print:
#   Deal      : Yes    (if is_good_deal returns True)
#   Deal      : No     (if is_good_deal returns False)
# ------------------------------------------------------------

# 👉 Write is_good_deal here (optional):


# 👉 Update print_order above to use is_good_deal (optional)


# ============================================================
# KEY REMINDERS
# ------------------------------------------------------------
# - "return" sends a value back. Without it the function
#   gives back None and your calculations will break.
# - You can store a returned value in a variable:
#       price = get_base_price("large")
# - You can also pass a returned value straight into another
#   function call:
#       final = apply_tax(get_base_price("large"))
# ============================================================
