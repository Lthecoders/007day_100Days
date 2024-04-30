# tvShow = input("What is your favorite tv show? ")
# if tvShow == "TMKOC":
#   print("Ugh, why?")

#   faveCharacter = input("Who is your favorite character? ")
#   if faveCharacter == "gETA LAL":
#     print("Right answer")
#     age = input("what was his age?")
#     if age == 50:
#       print("yes his age was 50")
#     else:
#       print("to young")
#   else:
#     print("Nah, Daddy Pig's the greatest")
# elif tvShow == "paw patrol":
#   print("Aww, sad times")
# else:
#   print("Yeah, that's cool and all…")

# tvShow = input("What is your favourite tv show? ")
# if tvShow == "peppa pig":
#   print("Ugh, why?")
#   faveCharacter = input("Who is your favourite character? ")
#   if faveCharacter == "daddy pig":
#     print("Right answer")
#   else:
#     print("Nah, Daddy Pig's the greatest")
# elif tvShow == "paw patrol":
#   print("Aww, sad times")
# else:
#   print("Yeah, that's cool and all…")

# order = input("What would you like to order: pizza or hamburger? ")
# if order == "hamburger":
#   print("Thank you.")
#   cheese = input("Do you want cheese?")
#   if cheese == "yes":
#     print("You got it.")
#   else:
#     print("No cheese it is.")
# elif order == "pizza":
#   print("Pizza coming up.")
#   toppings = input("Do you want pepperoni on that?")
#   if toppings == "yes":
#     print("We will add pepperoni.")
# else:
#   print("Your pizza will not have pepperoni.")
"------------day 7 challenge--------------------"

print("Fake AVENGERS FAN Finder")
print("----------------\n")

intro = "********please put your favourite hero name in lower case or else it will not work accordingly********\n\n"
print(intro.upper())

Marvel = input("tell me you will like question based on iron man or hulk? ")
if Marvel == "iron man":
  tell = input("when was last time iron appeared ")
  if tell == "endgame":
    print("you got that by peru chance")
    q_2 = input("who was almost there to get picked up Thors hammer? ")
    if q_2 == "vision":
      print("\033[32m", "that's great, Nice😍😍", "\033[0m")
    else:
      print("\033[31m", "hence proved you are not an marvel fan. 😒", "\033[0m")
  else:
    print("\033[31m", "hence proved you are not an marvel fan. 😒", "\033[0m")
elif Marvel == "hulk":
  ans = input(
      "\ntell me the first location in INDIA where hulk was spooted there? ")
  if ans == "kolkata":
    print("\033[32m", "you are a true marvel fan😍😍", "\033[0m")
  else:
    print("\033[31m", "hence proved you are not an marvel fan. 😒", "\033[0m")
else:
  print("\033[31m", "do not put any other superhero name", "\033[0m")
