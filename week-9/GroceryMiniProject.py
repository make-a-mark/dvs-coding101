#Project spec: Self Check Out
# You are a grocery shopper! You will have the abiltiy to put items in the shopping cart. You can stop shopping at any time via the command prompt. You will also need to figure out how much the items in your cart will cost. In addition you will be asked to pay and you will have to return the proper amount of change.  

inventory = [("apple", .75), ("orange", 1.3), ("milk", 2.0), ("eggs", 6), ("bacon", 5), ("cake", 12), ("cheesecake", 14), ("banana", 1.1), ("chicken", 8), ("cereal", 3.5), ("granola", 3)] #Add More Items later
global cart
cart = []

# Startup window/message
def main():
  print("Welcome to the self service grocery store!")
  checkout = False
  while (not checkout):
    if (checkout == None):
      print("Invalid answer")
      checkout = ask_checkout()
    elif (checkout == False):
      add_item = ask_add()
      while (not is_available(add_item)):
        not_available(add_item)
        if ask_checkout() == True:
          break
        elif ask_checkout() == False:
          continue
        add_item = ask_add()
      item_count = ask_count(add_item)
      addToCart(add_item, int(item_count))
      checkout = ask_checkout()
  makingPayment(calculatePrices(cart, inventory))
  

def ask_add():
  print("What would you like to add to your cart?")
  item = input("I would like to add: ")
  return item
  
def ask_count(item):
  count = input("How many " + item + "s do you want to add to your cart?: ")
  return count

def ask_checkout():
  answer = input("Would you like to checkout? (y/n) : ")
  if (answer == "y"):
    return True
  elif (answer == "n"):
    return False
  else:
    return None
  
def not_available(item):
  print("Sorry, we don't have " + item + " in stock")
  
  

def addToCart(item, count):
  #TODO: This will take the item someone wants to purchase, as well as the amount they want and append it to their cart that amount of times. So if they ask for 5 apples, this function will put apple 5 times in their cart array.
  i = 0
  _________________:
    cart.__________
    i += 1
  
def is_available(item):
  #TODO: Loop through the list of available items (invetory) and check if the item exist. Return true if it's an item they can purchase, false if it doesn't exist in the list of inventory. Hint: A for loop could be helpful. Since the items i
  ...

def calculatePrices(itemsPurchased, inventory):
  #TODO: This function will take in the inventory, which has the item and its price, as well as the customers cart. Take the customer's cart, find the respective price for that item in our inventory, and add it up to their total cost.
  totalCost = 0
  for ________ in __________:
    for _________ in __________:
      ...
    ...
  return totalCost

def makingPayment(cost):
  #TODO With the total cost, take the customers payment and return their change.
  
main()