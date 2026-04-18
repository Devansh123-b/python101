# ============================================================
# EXAMPLE 2: Functions with Parameters (Inputs)
# ============================================================
# Parameters let you PASS information INTO a function.
# Think of it like a vending machine — you give it a choice,
# it gives you back the right snack!
#
# STRUCTURE:
#   def function_name(parameter1, parameter2):
#       # use parameter1 and parameter2 here
# ============================================================

# --- One parameter ---
def greet_student(name):
    print("Hi,", name + "! Ready to learn Python?")

greet_student("Soliman")
greet_student("Devansh")
greet_student("Ashaz")

print("---")

# --- Two parameters ---
def describe_pet(pet_name, animal_type):
    print(pet_name, "is a", animal_type)

describe_pet("Fluffy", "cat")
describe_pet("Rex",    "dog")
describe_pet("Goldie", "fish")

print("---")

# --- Parameters with maths ---
def print_double(number):
    result = number * 2
    print(number, "doubled is", result)

print_double(5)
print_double(13)
print_double(100)

# ============================================================
# KEY IDEAS:
#   - The variable inside def (...) is called a PARAMETER.
#   - The actual value you pass in ("Alice", 5) is an ARGUMENT.
#   - Each call can send different data — same recipe, new ingredients!
# ============================================================
