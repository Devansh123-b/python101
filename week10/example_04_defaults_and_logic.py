# ============================================================
# EXAMPLE 4: Default Parameters & Logic Inside Functions
# ============================================================
# 1. DEFAULT PARAMETERS: You can give a parameter a default
#    value so the caller doesn't HAVE to provide it.
#
# 2. LOGIC INSIDE: Functions can contain if/else, loops —
#    anything Python can do!
# ============================================================

# --- Default parameter ---
# If "times" is not given, it defaults to 1
def cheer(team_name, times=1):
    for i in range(times):
        print("Go", team_name + "!!!")

cheer("Eagles")          # uses default times=1
cheer("Tigers", 3)       # overrides default → repeats 3 times

print("---")

# --- if/else inside a function ---
def is_even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

for n in [1, 2, 7, 10, 33]:
    print(n, "is", is_even_or_odd(n))

print("---")

# --- A more complex example: grade checker ---
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [95, 82, 74, 61, 45]
for s in scores:
    print("Score:", s, "→ Grade:", get_grade(s))

# ============================================================
# KEY IDEAS:
#   - Default parameters make functions more flexible.
#   - Functions can hold any Python logic — not just maths.
#   - Combining return + if/else makes very powerful functions.
# ============================================================
