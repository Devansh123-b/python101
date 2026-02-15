# Filename: EX03_while_number_validation_comments_only.py
# EX03 - Input Validation with continue (COMMENTS ONLY)
#
# Goal:
#   Keep asking the user for a number from 1 to 10
#   until they enter a valid number.
#
# Output:
#   - If invalid, print "Invalid, try again."
#   - If valid, print "Accepted!"
#
# New requirement:
#   - Use continue to restart the loop after an invalid input
#
# Rules:
#   - Use a while loop
#   - Avoid infinite loops by updating num inside the loop
#
# Hint skeleton:
#   num = int(input("Enter 1-10: "))
#   while True:
#       if num < 1 or num > 10:
#           print("Invalid, try again.")
#           num = int(input("Enter 1-10: "))
#           continue
#       print("Accepted!")
#       break
#
# Note:
#   Using while True is allowed here ONLY because you must use break/continue safely.
