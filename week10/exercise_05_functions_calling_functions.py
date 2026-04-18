# ============================================================
# EXERCISE 5: Functions Calling Other Functions
# ============================================================
# TOPIC: Decomposition — building a program from small pieces
# DIFFICULTY: ⭐⭐⭐⭐ (Medium-Hard)
#
# You are going to build a MINI REPORT CARD GENERATOR!
#
# Break the big problem into small helper functions, then
# combine them in one main function.
# ============================================================

# ============================================================
# YOUR MISSION
# Build a report card system for a student with 3 subjects.
# The program should:
#   1. Calculate the average of 3 scores
#   2. Convert the average to a letter grade (A/B/C/D/F)
#   3. Write a comment based on the grade
#   4. Print a nicely formatted report card
# ============================================================

# ------------------------------------------------------------
# STEP 1
# Define a function called "calculate_average" that takes
# THREE numbers (score1, score2, score3) and RETURNS their
# average (sum divided by 3).
# ------------------------------------------------------------

# 👉 Write calculate_average here:


# ------------------------------------------------------------
# STEP 2
# Define a function called "score_to_grade" that takes ONE
# number (the average score 0–100) and RETURNS a letter grade:
#   90 and above → "A"
#   80 – 89      → "B"
#   70 – 79      → "C"
#   60 – 69      → "D"
#   Below 60     → "F"
# ------------------------------------------------------------

# 👉 Write score_to_grade here:


# ------------------------------------------------------------
# STEP 3
# Define a function called "grade_comment" that takes ONE
# string (the letter grade) and RETURNS an encouraging comment:
#   "A" → "Outstanding work! Keep it up!"
#   "B" → "Great job! Almost perfect!"
#   "C" → "Good effort! A little more practice will help."
#   "D" → "Keep trying! Ask your teacher for help."
#   "F" → "Don't give up! Let's work together to improve."
# ------------------------------------------------------------

# 👉 Write grade_comment here:


# ------------------------------------------------------------
# STEP 4
# Define a function called "print_report_card" that takes:
#   - student_name  (string)
#   - subject       (string, e.g. "Math")
#   - score1, score2, score3  (three test scores)
#
# It should:
#   1. CALL calculate_average to get the average
#   2. CALL score_to_grade to get the grade letter
#   3. CALL grade_comment to get the comment
#   4. Print a report card like this:
#
#   ========================================
#   REPORT CARD
#   ========================================
#   Student : Alex Johnson
#   Subject : Math
#   Scores  : 85, 90, 78
#   Average : 84.33
#   Grade   : B
#   Comment : Great job! Almost perfect!
#   ========================================
#
# Hint: round(number, 2) rounds to 2 decimal places
# Hint: str(score1) + ", " + str(score2) + ...  joins scores
# ------------------------------------------------------------

# 👉 Write print_report_card here (it calls ALL the helpers!):


# ------------------------------------------------------------
# STEP 5
# Test your full system by calling print_report_card for
# at least TWO different students with different scores.
# Make sure different grades appear in your test output!
# ------------------------------------------------------------

# 👉 Call print_report_card for student 1:


# 👉 Call print_report_card for student 2:


# ============================================================
# CHALLENGE (optional)
# Add a NEW helper function called "is_passing" that takes the
# average score and returns True if it's >= 60, False otherwise.
# Update print_report_card to also print:
#   Status: PASS  or  Status: FAIL
# ============================================================

# 👉 Write is_passing here (optional):

# 👉 Update print_report_card to use it (optional):
