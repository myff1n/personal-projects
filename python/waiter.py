import time

#reset vars and such
global userOrder
userOrder = "null"
global orderList
orderList = []


#dictionary of menu items
global menu
menu = {
  
    "food": {
        "Cookie": 1.29,
        "Pizza": 9.89,
        "Ice Cream": 2.99,
        "Salad": 6.99,
        "Chicken Nuggets": 3.49,
        "Hamburger": 3.99,
        "Fries": 2.99
  }, 

    "drinks": {
        "Water": 0,
        "Pepsi": 2.49,
        "Dr Pepper": 2.49,
        "Coca Cola": 2.49,
        "Sprite": 2.49,
        "Root Beer": 2.49
  }

}


def prompt():
    print('Type "order" to order more, type "review" to review order')
    print('Type "done" if you are done ordering')
    selection = input("").strip().lower()
    if selection == "order": 
      orderGet(); 
      
    elif selection == "review":
      print("")
      print("Currently, your order is:")
      for x in orderList:
          print(x)
      print("")
      prompt();
      
    elif selection == "done":
        userTotal = 0
        print("")
        print("")
        print("")
        print("Your order is:")
        
        for i in orderList:
            if i in menu["food"]:
                userTotal = userTotal + menu["food"][i]
                print(i)
                
            elif i in menu["drinks"]:
                userTotal = userTotal + menu["drinks"][i]
                print(i)
            else:
                print("")
        print(f"with a total of ${usertotal}")
        print("Please pay at the window")
                
    else:
      print ("That is not a valid command.")
      prompt();


def orderGet():
    #print menu and take user order
    print("We have:")
    for i in menu["food"] :
        print("Item: " + i, " Price: $" + str(menu["food"][i]))
    print("")
    for i in menu["drinks"] :
        print("Item: " + i, " Price: $" + str(menu["drinks"][i]))
        
    print("What would you like to order?")
    print("(Please order one item at a time!)")
    userOrder = input("").strip().lower().title()
    
    #check if order is on the menu
    if userOrder in menu["food"]:
        orderList.append(userOrder)
        print("")
        print("Added to order")
        prompt();

    elif userOrder in menu["drinks"]:
        orderList.append(userOrder)
        print("")
        print("Added to order")
        prompt();

    else:
        print("That is not on the menu.")
        print("")
        time.sleep(1)
        orderGet();


orderGet();

