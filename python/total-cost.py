import math

global purchaseList
purchaseList = []

#prompt user for number of items
print("How many items are you purchasing?")
itemsPurchased = input("")

#prompt user for tax
print("How much tax? (in decimal, ex. 0.07)")
tax = input("")

#prompt user for cost (to the 100ths decimal)
itemNumber = 1

while itemNumber >= itemsPurchased:
  print("What is the cost of item", str(itemNumber), "?")
  itemCost = input("")
  
  #add tax to item cost, store in list
  itemCost = itemCost + (itemCost * tax)
  purchaseList.append(itemCost)
  
  itemNumber += 1
  
  #add up all list items and print
