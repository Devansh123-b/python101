# Filename: EX05_while_guess_with_limited_tries_comments_only.py
# EX05 - Guessing Game with Tries + Validation (COMMENTS ONLY)
#
# Goal:
#   Make a guessing game:
#     - secret number is 9
#     - user gets 4 tries
#     - count valid attempts only
#
# New requirements:
#   1) If guess is NOT between 1 and 10, print "Invalid" and DO NOT use up a try.
#      Use continue for this.
#   2) Use an attempts counter that counts valid guesses.
#
# Output rules:
#   - If guess is too low, print "Too low"
#   - If guess is too high, print "Too high"
#   - If correct, print "Correct!" and end early
#   - If they run out of tries, print "Out of tries!"
#
# Rules:
#   - Use a while loop
#   - Use tries_left, attempts
#   - tries_left decreases only for valid guesses
#   - Avoid infinite loops (tries_left must change OR guess must change each loop)
#
# Hint variables:
#   secret = 9
#   tries_left = 4
#   attempts = 0
#
# Suggested structure:
#   while tries_left > 0:
#       guess = int(input(...))
#       if guess < 1 or guess > 10:
#           print("Invalid")
#           continue
#       attempts = attempts + 1
#       tries_left = tries_left - 1
#       ... compare guess ...
#       if guess == secret:
#           break
#
# At the end, print attempts and tries_left as part of the summary.
