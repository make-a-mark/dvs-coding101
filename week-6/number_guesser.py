print("Please pick a number from 0-100, don't tell me, and I will guess it!")

guess = 50
initial_fix = 25
counter = 1

got_it = False

while not got_it: # while True:
  user_input = input("Is your number " + str(guess) + "? (y/n)\n")
  
  if user_input == "y":
    got_it = True
  else:
    fix = input("If higher, type 1\nIf lower, type 0\n")
    
    if (fix == "1"):
      guess += initial_fix//counter
      counter += 1
    else:
      guess -= initial_fix//counter
      counter += 1
else:
  print("I told you I would guess your number!")
