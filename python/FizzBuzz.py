#write numbers 1 - 100
for i in range(1, 101):
  fizz, buzz = False, False
    
  #check if divisible by 3, write to variable
  if i % 3 == 0: 
    fizz = True;

  #check if divisible by 5, write to variable
  if i % 5 == 0: 
    buzz = True;
  
#look at variable(s?) and output
  if fizz and buzz:
    print("FizzBuzz")
  elif fizz:
    print("Fizz")
  elif buzz:
    print("Buzz")
  else:
    print(i)
