# ============================================================
# EXERCISE 1: Define and Call Basic Functions
# ============================================================
# TOPIC: Creating and calling functions (no parameters yet)
# DIFFICULTY: ⭐ (Beginner)
#
# Read each task carefully. Write your code in the spaces
# marked with  👉  below each instruction.
# ============================================================

# ------------------------------------------------------------
# TASK 1
# Define a function called "print_banner" that prints:
#   ********************
#   *  I Love Python!  *
#   ********************
# Then CALL the function so it runs.
# ------------------------------------------------------------

# Section 1: Task 1
def print_banner():
    print("*"*20)
    print("*  I Love Python!  *")
    print("*"*20)

print_banner()


# ------------------------------------------------------------
# TASK 2
# Define a function called "print_favourite_things" that
# prints at least 3 of YOUR favourite things (food, hobbies,
# movies — anything you like!).
# Then call it TWICE.
# ------------------------------------------------------------

# Section 2: Task 2
def print_favourite_things():
    print("- making games")
    print("- making jokes")
    print("- and playing video games")
    print("-" * 15)

print_favourite_things()
print_favourite_things()

# ------------------------------------------------------------
# TASK 3
# Define a function called "count_to_ten" that uses a
# for loop to print the numbers 1 through 10, each on its
# own line.
# Then call it.
# ------------------------------------------------------------

# Section 3: Task 3
def count_to_ten():
    for i in range(1, 11):
        print(i)

count_to_ten()

# ============================================================
# CHALLENGE (optional, for extra fun!)
# Define a function called "print_star_triangle" that prints:
#   *
#   **
#   ***
#   ****
#   *****
# Hint: use a for loop and string multiplication ("*" * n)
# ============================================================

def print_star_triangle():
    for i in range(1, 6):
        print("*" * i)

print_star_triangle()
