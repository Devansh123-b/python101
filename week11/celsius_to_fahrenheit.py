# ============================================================
# Grade 7 – Python 101 – Week 11 Practice Problems
# SOLUTION: Problem 1 – Temperature Converter
# ============================================================


# ------------------------------------------------------------
# STEP 1: celsius_to_fahrenheit
# ------------------------------------------------------------

def celsius_to_fahrenheit(celsius):
    result = (celsius * 9/5) + 32
    return round(result, 1)


# ------------------------------------------------------------
# STEP 2: fahrenheit_to_celsius
# ------------------------------------------------------------

def fahrenheit_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * 5/9
    return round(result, 1)


# ------------------------------------------------------------
# STEP 3: Test both functions
# ------------------------------------------------------------

print("0 C =", celsius_to_fahrenheit(0), "F")       # 32.0
print("100 C =", celsius_to_fahrenheit(100), "F")   # 212.0
print("32 F =", fahrenheit_to_celsius(32), "C")     # 0.0
print("98.6 F =", fahrenheit_to_celsius(98.6), "C") # 37.0

print("---")


# ------------------------------------------------------------
# CHALLENGE: describe_weather
# ------------------------------------------------------------

def describe_weather(celsius):
    if celsius >= 30:
        return "Hot"
    elif celsius >= 20:
        return "Warm"
    elif celsius >= 10:
        return "Cool"
    else:
        return "Cold"

print("35 C ->", describe_weather(35))   # Hot
print("22 C ->", describe_weather(22))   # Warm
print("15 C ->", describe_weather(15))   # Cool
print("5 C ->",  describe_weather(5))    # Cold
