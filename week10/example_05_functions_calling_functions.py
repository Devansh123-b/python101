# ============================================================
# EXAMPLE 5: Functions Calling Other Functions
# ============================================================
# Just like LEGO bricks snap together, functions can call
# other functions. This lets you build BIG programs from
# small, simple pieces.
#
# This example builds a mini Pizza Order System!
# ============================================================

# --- Small helper functions ---
def calculate_base_price(size):
    """Returns the base price for a pizza size."""
    if size == "small":
        return 8
    elif size == "medium":
        return 12
    elif size == "large":
        return 16
    else:
        return 0   # unknown size

def calculate_topping_cost(num_toppings):
    """Each topping costs $1.50."""
    return num_toppings * 1.50

def apply_discount(price, is_member):
    """Members get 10% off."""
    if is_member:
        return price * 0.90   # 90% of price = 10% discount
    else:
        return price

# --- Big function that USES all the helpers ---
def calculate_order(size, num_toppings, is_member):
    """Calculates the final pizza price using helper functions."""
    base      = calculate_base_price(num_toppings=num_toppings, size=size)
    toppings  = calculate_topping_cost(num_toppings)
    subtotal  = base + toppings
    final     = apply_discount(subtotal, is_member)
    return final

# --- Main program ---
def print_receipt(size, num_toppings, is_member):
    """Prints a nice receipt."""
    total = calculate_order(size, num_toppings, is_member)
    print("===== PIZZA RECEIPT =====")
    print("Size      :", size)
    print("Toppings  :", num_toppings)
    print("Member?   :", "Yes" if is_member else "No")
    print("Total     : $" + str(round(total, 2)))
    print("=========================")

# Two orders
print_receipt("large",  3, is_member=True)
print()
print_receipt("medium", 1, is_member=False)

# ============================================================
# KEY IDEAS:
#   - Each function does ONE job — small and focused.
#   - The big function (print_receipt) delegates work to
#     smaller helpers.
#   - This is called DECOMPOSITION — breaking a big problem
#     into smaller, manageable pieces.
#   - Notice the triple-quoted strings (""" """) — those are
#     called DOCSTRINGS and describe what a function does.
# ============================================================
