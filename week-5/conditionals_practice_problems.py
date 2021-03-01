# Problem 1 - conditional for in list
problem_1_list = [17, 38, "yessir", "bruh", 21,"markisbestinstructornocap"]

# make a string variable equal to bruh and write a conditional to check if that variable is in this list
# can print out Problem 1 True or something within the conditional


# Problem 2 - indexing list
# Use this link and scroll to the bottom section Testing and use these functions for this problem
# https://www.pythonforbeginners.com/basics/string-manipulation-in-python

# Check if the first element of this list starts with 'P'
# check if the last element of this list is an int (hint: use type)
# check if the 2nd INDEX of this list is a digit

problem_2_list = ["fhilly cheesesteak", 1.43, "96", 4.20, "pi", 3.14, "bussin", 7]


# Problem 3 - condition based on input
# Remember  that input is of type string
# practice using the python input function and determine if what you entered are all letters or all numbers (use the link again!)
# if neither, then print out neither!


# Problem 4 - Chained/Nested Conditionals challenge
# Which branches of the conditional would run?
# What does the list have at the end?
# Try not to print the list, unless you're really having trouble
# If you do, that's okay, but try to understand why that's the end result!
# sorry if i made this hard LOL

x = 7;
y = 10;
problem_4_list = ["w", x, y, "z"]
#problem_4_list.append(y)
#print(problem_4_list)

# CONDITION 1
if x < 10 and y-3 == x: # does this run?
  y = y - 3
  problem_4_list[0] = "a"

  # CONDITION 2:
  if y == x: # would this run?
    blah = 20
  else:
    blah = 40 # or this?

  # CONDITION 3:
  if "x" in problem_4_list: # does this run?
    z = 60
    problem_4_list.append(z)

  elif "7" in problem_4_list: # how about this?
    if x!= y:
      problem_4_list[2] = "k"

  else: # maybe this?

    # CONDITION 4:
    if y!= x: # do we get in this branch?
      problem_4_list.append("70")
      problem_4_list.remove("z")
    else: # or this?
      problem_4_list.remove(x)
      problem_4_list.append(blah)
    
    problem_4_list.append(y)
