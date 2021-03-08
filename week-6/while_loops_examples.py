# EXAMPLE 1: Infinite while loop!
# while True:
#   print ("We are stuck here")

# EXAMPLE 2: Using a counter as the condition!
counter = 1
while counter < 5:
  print ("This is iteration #: " + str(counter))
  counter += 1

# EXAMPLE 3: Using a counter but having a BREAK!
counter = 1
while True:
  if counter == 5:
    break
  print ("This is iteration #: " + str(counter))
  counter += 1

# EXAMPLE 4: How to loop through a list using the While loop similar to for loop!

numbers = [1,2,3,4]

current_index = 0
while current_index < len(numbers):
  print("current index = " + str(current_index))
  print (numbers[current_index])
  current_index += 1

# EXAMPLE 5: The While-Else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
