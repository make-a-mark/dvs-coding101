#For questions 1-9, add the int or the float
#that will make the print statement true in spot
# denoted by the *Your answer here!* . Watch out
# x is not always being updated so keep careful 
# track what the value of x is.
print("#Question 1:")
x = 3
print(x+1 == 4)

print("#Question 2:")
print(x == 3)

print("#Question 3:")
x -= 2
print(x == 1) 

print("#Question 4:")
x = 4 #setting the value of x to 4.
print(x * 2 == 8)

print("#Question 5:")
print(x / 2 == 2.0)

print("#Question 6:")
print(x // 2 == 2)

print("#Question 7:")
x = 2 ** 3
print(x == 8)

print("#Question 8:")
x = 9 % 6
print(x == 3)

print("#Question 9:")
x = 4 * -2
print(x == -8)

#Write the type of x in *Your answer here!*.
#Hint: is it an int or float?
print("#Question 10:")
x = 2 + 1.0
print(type(x) == float) 

print("#Question 11:")
fruits = ["apple", "banana", "cherry"]

#append your favorite fruit to the list!
fruits.append("grapes")
#remove your least favorite fruit!
fruits.remove("cherry")

print("#Question 12:")
s = "Coding "
t = "101"
#In the print below add the statement that 
#would print "Coding 101".
print(s + t)