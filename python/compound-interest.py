import time
import random
import math


#prompt user
print("Hello! Welcome to the Compound Interest Program!")
print("Interest is 6% per year")
print("")
print("How much money will you deposit?")
#save deposit as a variable, and make it a float
depInput = input("")
dep = float(depInput)
#save number of years as a variable, and make it a float it too
print("How many years do you plan to leave it?")
yrsInput = input("")
yrs = int(yrsInput)

#calculate 1st year. done for variable convenience
year1 = (dep * 0.06) + dep

i = 1
finalAmount = year1

#loop for each year
while i < yrs:
    finalAmount = (finalAmount * 0.06) + finalAmount
    i += 1



#added "load time" just for fun
print("Calculating...")
time.sleep(random.randint(1, 5))
#                                                v make the end result at least 4 characters, with 2 numbers past the decimal point
print("Your total, after", yrs, "years, is $", '{:04.2f}'.format(finalAmount))
