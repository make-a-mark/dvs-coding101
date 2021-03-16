def simple_loop(a):
  i = 1
  while (i <= a):
    print(i)
    i+=1
  
def simple_addition(a, b):
  return a + b

def simple_function():
  print("Hey! I'm a simple function")

#Call to simple function
simple_function()

print("\nsimple_addition #1:")
print(simple_addition(1,1.0))
print("\nsimple_addition #2:")
print(simple_addition(1,2))
print("\nsimple_addition #3:")
#Will this work?
print(simple_addition("Edwin ","sucks!"))

print("\nSimple loop #1:")
#Simple loop 
simple_loop(5)
print("\nSimple loop #2:")
#what will happen?
simple_loop(0)
print("\nSimple loop #3:")
simple_loop(1)