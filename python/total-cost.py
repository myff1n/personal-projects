import time
import random

global purchaseList
purchaseList = []
global totalCost
totalCost = 0

#prompt user for number of items
print("How many items are you purchasing?")
itemsPurchased = input("")

itemsPurchased = int(itemsPurchased)

#prompt user for tax
print("How much tax? (in decimal, ex. 0.07 = 7%)")
tax = float(input(""))

#prompt user for cost (to the 100ths decimal)
itemNumber = 1

while itemNumber <= itemsPurchased:
  print(f"What is the cost of item {itemNumber}?")
  itemCost = float(input(""))
  
  #add tax to item cost, store in list
  itemCost = itemCost + (itemCost * tax)
  purchaseList.append(itemCost)
  
  itemNumber += 1
  
  #add up all list items and print
for x in purchaseList:
  totalCost += x

#"load time", for fun
print("Calculating...")
time.sleep(random.randint(1, 5))
  
print(f"After tax, the total cost of your {itemsPurchased} items is: $" '{:03.2f}'.format(totalCost))
