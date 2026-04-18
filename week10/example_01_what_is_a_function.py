# ============================================================
# EXAMPLE 1: What is a Function?
# ============================================================
# A function is like a RECIPE. You write the steps once,
# and you can use them as many times as you want!
#
# STRUCTURE of a function:
#
#   def function_name():
#       # code goes here (indented!)
#
# "def" tells Python: "Hey, I'm creating a function!"
# ============================================================

# --- Defining (creating) a function ---
def say_hello():
    print("Hello there!")
    print("Welcome to Python functions!")
    print("Functions are awesome!")

# --- Calling (using) a function ---
# Nothing runs until you CALL the function by writing its name + ()
say_hello()

print("---")   # separator

# You can call the same function multiple times!
say_hello()
say_hello()

# ============================================================
# NOTICE:
#   - We wrote the recipe ONCE (def say_hello)
#   - We used it THREE times just by calling say_hello()
#   - Without functions, we'd have to copy-paste those
#     3 print lines every single time. Functions save effort!
# ============================================================
