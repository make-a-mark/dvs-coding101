# EXAMPLE 0: How a for loop works

numbers = [1,2,3,4]

for current_number in range(len(numbers)):
  print (current_number)


# EXAMPLE 1: Counting Number of occurences in a list

fruits = ["apple", "orange", "banana", "banana", "mango", "orange", "apple"]

num_apples = 0
num_oranges = 0
num_banana = 0
num_mangoes = 0

for fruit in fruits:
  if fruit == "apple":
    num_apples += 1
  elif fruit == "orange":
    num_oranges += 1
  elif fruit == "banana":
    num_banana += 1
  else: # should be mango
    num_mangoes += 1

print ("Number of apples = " + str(num_apples))
print ("Number of oranges = " + str(num_oranges))
print ("Number of bananas = " + str(num_banana))
print ("Number of mangoes = " + str(num_mangoes))

# EXAMPLE 2: Counting Number of occurences in a LONGER list

lots_of_fruits = ["apple", "orange", "banana", "banana", "mango", "orange", "apple", "orange", "banana", "banana", "mango", "apple", "orange", "banana", "banana", "mango", "apple", "orange", "banana", "banana", "orange", "banana", "banana", "mango", "orange", "banana", "mango", "apple", "orange", "orange", "banana", "banana", "mango", "apple", "orange", "banana", "banana", "mango", "apple", "orange", "banana", "banana", "mango", "orange", "apple", "orange", "banana", "banana", "mango", "apple", "orange", "banana", "banana", "mango", "apple", "orange", "banana", "banana", "orange", "banana", "banana", "mango", "orange", "banana", "mango", "apple", "orange", "orange", "banana", "banana", "mango", "apple", "orange", "banana", "banana", "mango"]

num_apples = 0
num_oranges = 0
num_banana = 0
num_mangoes = 0

for fruit in lots_of_fruits:
  if fruit == "apple":
    num_apples += 1
  elif fruit == "orange":
    num_oranges += 1
  elif fruit == "banana":
    num_banana += 1
  else: # should be mango
    num_mangoes += 1

print ("Number of apples = " + str(num_apples))
print ("Number of oranges = " + str(num_oranges))
print ("Number of bananas = " + str(num_banana))
print ("Number of mangoes = " + str(num_mangoes))

# EXAMPLE 3: Printing each letter of a string

word = "sufyan"

for letter in word:
  print (letter)

# EXAMPLE 4: Range!
for number in range(5):
  print (number)

# EXAMPLE 5: Continue!
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# EXAMPLE 6: The For else!
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
# EXAMPLE 7: Nested For Loops!
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

