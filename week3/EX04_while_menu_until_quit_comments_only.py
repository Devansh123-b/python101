# Filename: EX04_while_menu_until_quit_comments_only.py
# EX04 - Menu Until Quit + String Loop Option (COMMENTS ONLY)
#
# Goal:
#   Build a simple menu that repeats until the user chooses "q".
#
# Menu:
#   a) Say hello
#   b) Square a number
#   c) Count vowels in a word   <-- NEW
#   q) Quit
#
# Behavior:
#   - If "a": print "Hello!"
#   - If "b": ask for a number and print its square
#   - If "c": ask for a word and count vowels (a,e,i,o,u)
#   - If "q": print "Goodbye!" and stop
#   - Otherwise: print "Invalid choice"
#
# Rules:
#   - Use a while loop
#   - Avoid infinite loops by updating choice every time
#   - For vowel counting, use:
#       for ch in word.lower():
#           if ch in "aeiou": ...
#
# Hint:
#   choice = input("Choose a/b/c/q: ").strip().lower()
#   while choice != "q":
#       ...
#       choice = input("Choose a/b/c/q: ").strip().lower()
