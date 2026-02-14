# Filename: 01_if_else_number_check.py
# Python101 - Week 3: if / else with comparisons

print("=== Number Check (positive, negative, or zero) ===")

num = int(input("Enter an integer: "))

if num > 0:
    print("This number is positive.")
else:
    # This else runs for everything that is NOT > 0 (so zero or negative)
    if num == 0:
        print("This number is zero.")
    else:
        print("This number is negative.")

print()
print("Done.")

# Teaching notes:
# - if runs only when the condition is True
# - else runs when the condition is False
# - == checks equality (it does NOT assign)
# - You can put an if inside an else (nested decision)
