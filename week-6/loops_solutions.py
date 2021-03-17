# Problem 1 part 1 - Using whatever looping method you prefer, print out all the even numbers in this list BUT don't print any that are greater than 500 

numbers = [ 951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]


'''
#answer:

for num in numbers:
  if (num % 2 == 0 and num < 500):
    print(num)
'''


# Problem 1 part 2 - using the same list, use looping to add up all the values in the list

total = 0

'''
answer:

for num in numbers:
  total += num

print(total) should be 54189
'''

# Problem 2: print the following pattern using loops

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

'''
answer example:

num_string = ""

for number in range (1,6):
  num_string += str(number)
  num_string += " "
  print (num_string)

'''

# Problem 3: Use the random library to get a random number from 1-100 and then use a while loop to keep subtracting by 5 until you reach 0 (if subtracting by 5 would get you a negative number, subtract by whatever you need to to get it to 0)
# print out each iteration of the loop and the last iteration of the loop!

# example: random number = 23 -> 18 -> 13 -> 8 -> 3 -> 0

'''
answer:
import random

random_num = random.randint(1,100)

while random_num != 0:
  print (random_num)
  if random_num - 5 < 0:
    random_num -= random_num
  else:
    random_num -= 5
else:
  print (random_num)
'''

# Problem 4: Take integer inputs from user until they press q ( Ask to press q to quit after every integer input ). Print average of all numbers.
# HINT: have a counter to know how much to divide by

'''
answer:

average = 0
counter = 0

while True:
  user_input = input("Insert number or 'q': ")
  if user_input == 'q':
    break
  else:
    average += int(user_input)
    counter += 1

print ("Average = " + str(average / counter))
'''

# Problem 5: Write a Python program to guess a number between 1 to 9. Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

'''
answer:

import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')

'''