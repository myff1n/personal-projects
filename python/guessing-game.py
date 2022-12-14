import random

def endGame():
  string_wins = str(wins)
  print("Win counter: " + string_wins)
  print("Play again? Y/N");
  coin = input("").upper();
  if coin == "Y":
    game()
  else:
    print("See you next time");


def game():
  #set number and reset win boolean
  num = random.randrange(1,11)
  global correct;
  global wins;
  correct = False;
  #loop to keep user guessing
  while correct == False:
    print("Guess a number between 1 and 10:")
    guess = input("");
    #guess is blank
    if guess == "":
      print("Please input a number")
    #right number guessed
    elif float(guess) == num:
      correct = True;
      wins += 1;
      print("You Win!");
      #run endgame function
      endGame();
    #if user goes over 10 (checks for 11 and above)
    elif float(guess) >= 11:
      print("That number is above 10");
    #if user goes under 1 (checks for 0 and below)
    elif float(guess) <= 0:
      print("That number is below 1");
    #guess is too high
    elif float(guess) > num:
      print("Too high, guess again");
    #guess is too low
    elif float(guess) < num:
      print("Too low, guess again")
    #guess is a letter
    else:
      print("Please input a number");

      
#reset wins variable
wins = 0;

#starting prompt
print("Would you like to play a game? Y/N")
confirmStart = input("").upper();

if confirmStart == "Y":
  game()
else:
  print("See you next time")
