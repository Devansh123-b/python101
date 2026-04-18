# ============================================================
# EXAMPLE 3: Functions that RETURN Values
# ============================================================
# So far our functions just print things.
# But functions can also CALCULATE something and SEND IT BACK
# using the "return" keyword.
#
# Think of it like a calculator:
#   - You press buttons (arguments)
#   - It sends back an answer (return value)
# ============================================================

# --- A function that returns a value ---
def add(a, b):
    total = a + b
    return total          # <-- sends the result back to the caller

# Store the returned value in a variable
answer = add(3, 7)
print("3 + 7 =", answer)

# Or use it directly inside print()
print("10 + 25 =", add(10, 25))

print("---")

# --- More return examples ---
def multiply(x, y):
    return x * y

def square(n):
    return n * n

def get_full_name(first, last):
    return first + " " + last   # strings can be returned too!

print("6 x 8 =", multiply(6, 8))
print("9 squared =", square(9))
print("Full name:", get_full_name("Maya", "Johnson"))

print("---")

# --- Using a returned value inside another calculation ---
side = 5
area = square(side)
perimeter = side * 4
print("Square with side", side)
print("  Area     =", area)
print("  Perimeter =", perimeter)

# ============================================================
# KEY IDEAS:
#   - "return" exits the function AND sends a value back.
#   - After return, no more code in that function runs.
#   - You can store the returned value, print it, or use it
#     in more calculations.
# ============================================================
