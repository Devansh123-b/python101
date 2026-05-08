# ============================================================
# Grade 7 – Python 101 – Week 11 Practice Problems
# SOLUTION: Problem 2 – Pizza Price Calculator
# ============================================================


# ------------------------------------------------------------
# STEP 1: get_base_price
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
# STEP 2: add_toppings_cost
# ------------------------------------------------------------

def add_toppings_cost(num_toppings):
    return num_toppings * 1.50


# ------------------------------------------------------------
# STEP 3: apply_tax
# ------------------------------------------------------------

def apply_tax(price):
    return round(price * 1.13, 2)


# ------------------------------------------------------------
# CHALLENGE: is_good_deal
# ------------------------------------------------------------

def is_good_deal(total):
    return total < 15


# ------------------------------------------------------------
# STEP 4: print_order (calls all helpers)
# ------------------------------------------------------------

def print_order(customer_name, size, num_toppings):
    base      = get_base_price(size)
    toppings  = add_toppings_cost(num_toppings)
    subtotal  = round(base + toppings, 2)
    total     = apply_tax(subtotal)
    deal      = "Yes" if is_good_deal(total) else "No"

    print("==============================")
    print("        PIZZA ORDER")
    print("==============================")
    print("Customer  :", customer_name)
    print("Size      :", size)
    print("Toppings  :", num_toppings)
    print("Subtotal  : $" + str(subtotal))
    print("Total     : $" + str(total))
    print("Deal      :", deal)
    print("==============================")
    print()


# ------------------------------------------------------------
# STEP 5: Test with two different customers
# ------------------------------------------------------------

print_order("Sam Rivera", "medium", 3)
print_order("Jordan Lee", "large", 5)
