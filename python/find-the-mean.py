#set numbers and reset total
num = [6, 357, 209, 15, 92, 36, 12]
total = 0

#repeat through whole list of numbers
for x in num:
  total += x

#print total               v making total a string to concat
print("Your total is: " + str(total))
#and turning it back into an integer
int(total)

#find the mean
mean = total / len(num)
#and make it a string to concat + print
print("The mean is: " + str(mean))
