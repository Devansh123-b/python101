#by Devansh
can_swim = input("Can you swim? ").strip().lower()
age = input("What age are you? ").strip().lower()
if age==10 and can_swim == "yes":
  print("You can go in the deep end.")
else:
  print("Stay in the shallow end.")
