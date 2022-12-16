#write numbers 1 - 100 // if change needed, value on right should be 1 more than desired output
for i in range(1, 101):
  fizz, buzz = False, False
    
  #check if divisible by 3, write to variable
  if i % 3 == 0: 
    fizz = True;

  #check if divisible by 5, write to variable
  if i % 5 == 0: 
    buzz = True;
  
#look at variables and output
  #if both fizz and buzz are true, say "FizzBuzz"
  if fizz and buzz:
    print("FizzBuzz")
  #if only fizz is true, say "Fizz"
  elif fizz:
    print("Fizz")
  #if only buzz is true, say "Buzz"
  elif buzz:
    print("Buzz")
  #if neither is true, say the number
  else:
    print(i)
