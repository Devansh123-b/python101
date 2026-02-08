# Filename: EX05_decision_program_comments_only.py
# EX05 - Decision-making program (COMMENTS ONLY)
#
# Goal:
#   Make a “Lunch Chooser” program.
#
# Ask:
#   1) "Do you want something hot?" (yes/no)
#   2) "Do you want something healthy?" (yes/no)
#
# Rules:
#   hot AND healthy         -> "Soup"
#   hot AND NOT healthy     -> "Pizza"
#   NOT hot AND healthy     -> "Salad"
#   NOT hot AND NOT healthy -> "Sandwich"
#
# Hint:
#   hot = input(...).strip().lower() == "yes"
#   healthy = input(...).strip().lower() == "yes"
#   if hot and healthy:
#       ...
