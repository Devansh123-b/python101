# 🔐 Mini Project: Secure System Login

In this project, you will build a **simple security login system** using Python.

Your program will:
- Ask for a username
- Check if the user is authorized
- Generate a **random 2-digit security code between 10 and 20**
- Allow **3 attempts** to unlock the system

This project uses:
- `input()`
- `print()`
- `if / else`
- `while` loops
- boolean variables
- logical conditions (`and`)
- the `random` module
- `.strip()` and `.lower()`

---

# 🧩 Program Requirements

## 1. Import the random module

Your program should generate a random security code.

Example:

```python
import random
````

---

# 2. Ask for the user's name

Prompt the user to enter their name.

Use `.strip()` and `.lower()` so the program accepts inputs like:

* `"Admin"`
* `"ADMIN"`
* `" admin "`

Example idea:

```python
name = input("Enter your name: ").strip().lower()
```

---

# 3. Check if the user is authorized

Only the user **Admin** can access the system.

If the name is **not `"admin"`**, print:

```
Access Unauthorized
```

Then the program should end.

If the name **is `"admin"`**, print:

```
Welcome Admin
Security verification required
```

---

# 4. Generate a 4-digit security code

Create a random number between **10 and 20**.

Example:

```python
code = random.randint(10, 20)
```

---

# 5. Create your control variables

Create the following variables:

* `attempts = 3`
* `system_unlocked = False`

---

# 6. Use a while loop

Use a `while` loop so the user can try to enter the security code.

The loop should continue **while**:

* attempts are greater than 0
* the system is still locked

Example structure:

```python
while attempts > 0 and system_unlocked == False:
```

---

# 7. Ask for the security code

Inside the loop:

* Ask the user to enter the **2-digit code between 10 and 20**
* Convert the input to an integer

Example idea:

```python
guess = int(input("Enter the 4-digit code: "))
```

---

# 8. Check the code

If the guess **matches the generated code**:

```
Access Granted
System Unlocked
```

Set the boolean variable so the loop stops.

---

# 9. If the code is incorrect

If the guess is wrong:

* subtract 1 from `attempts`
* print a message
* show the number of attempts remaining

Example output:

```
Incorrect code
Attempts remaining: 2
```

---

# 10. If all attempts are used

If the user runs out of attempts, print:

```
Security Locked
```

---

# 💻 Example Output

```
Enter your name: ADMIN

Welcome Admin
Security verification required

Enter the 2-digit code: 15
Incorrect code
Attempts remaining: 2

Enter the 2-digit code: 19
Incorrect code
Attempts remaining: 1

Enter the 2-digit code: 11
Access Granted
System Unlocked
```

---

# ⭐ Bonus Challenge (Optional)

Add a **hint system**:

* If the guess is **greater than the code**, print `"Too high"`
* If the guess is **less than the code**, print `"Too low"`

Example:

```
Too high
Attempts remaining: 2
```

