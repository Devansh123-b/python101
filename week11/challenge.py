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

def celsius_to_fahrenheit(celsius):
    result = (celsius * 9/5) + 32
    return round(result, 1)


# ------------------------------------------------------------
# STEP 2
# Define a function called "fahrenheit_to_celsius" that:
#   - Takes ONE number called "fahrenheit"
#   - RETURNS the temperature converted to Celsius
#
# Hint: round(result, 1) rounds to 1 decimal place
# ------------------------------------------------------------

def fahrenheit_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * 5/9
    return round(result, 1)


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

print(celsius_to_fahrenheit(0))  # Output: 32.0
print(celsius_to_fahrenheit(100))  # Output: 212.0
print(fahrenheit_to_celsius(32))   # Output: 0.0
print(fahrenheit_to_celsius(98.6))  # Output: 37.0
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

def get_base_price(size):
    if size == "small":
        return 8
    elif size == "medium":
        return 12
    elif size == "large":
        return 16
    else:
        return 0


# ------------------------------------------------------------
# STEP 2
# Define a function called "add_toppings_cost" that:
#   - Takes ONE number: "num_toppings"
#   - RETURNS the total topping cost
#     (each topping costs 1.50)
# ------------------------------------------------------------

def add_toppings_cost(num_toppings):
    return num_toppings * 1.5



# ------------------------------------------------------------
# STEP 3
# Define a function called "apply_tax" that:
#   - Takes ONE number: "price"
#   - RETURNS the price after adding 13% tax
#
# Hint: round(result, 2) rounds to 2 decimal places
# ------------------------------------------------------------

def apply_tax(subtotal):
    tax_rate = 0.13  # 13%
    return subtotal * tax_rate



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


def print_order(name=None):

    size = input("What is your desired size of pizza? (small, medium, large) ").lower()
    num_toppings = int(input("How many toppings would you like? "))
    
    base_price = get_base_price(size)
    toppings_cost = add_toppings_cost(num_toppings)
    subtotal = base_price + toppings_cost
    tax = apply_tax(subtotal)
    total = subtotal + tax
    
    print("==============================")
    print("PIZZA ORDER")
    print("==============================")
    print(f"Customer: {name}")
    print(f"Size: {size}")
    print(f"Toppings: {num_toppings}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total: ${total:.2f}")



# ------------------------------------------------------------
# STEP 5
# Test your pizza system by calling print_order at least TWICE
# with different customers, sizes, and topping counts.
# Make sure you try different sizes so all three prices appear.
# ------------------------------------------------------------

print_order("David")

print_order("Emma")


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
