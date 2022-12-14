import random

deck = [
  "Ace Of ",
  "2 Of ",
  "3 Of ",
  "4 Of ",
  "5 Of ",
  "6 Of ",
  "7 Of ",
  "8 Of ",
  "9 Of ",
  "10 Of ",
  "Jack Of ",
  "Queen Of ",
  "King Of ",
]
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

#unnecessarily shuffling the deck because it's cards
random.shuffle(deck)

global correct
global wins
correct = False;
wins = 0;


def endGame():
  string_wins = str(wins)
  print("Win counter: " + string_wins)
  print("Play again? Y/N")
  coin = input("").upper()
  if coin == "Y":
    game()
  else:
    print("See you next time")


def game():
  #set number and reset win boolean
  card = random.choice(deck) + random.choice(suits)

  #loop to keep user guessing
  while correct == False:
    print("Guess a card: ")
    print(card[5:])
    guess = input("").title()
    if card[:4] == "King" or "Jack":
      #guess is blank
      if guess == "":
        print("Please input a card")
      #right number guessed
      elif guess == card:
        correct = True
        wins += 1
        print("You Win!")
        #run endgame function
        endGame()
      elif guess[:1] == card[:1] and guess[5:] != card[5:]:
        print("Wrong suit, guess again")
      elif guess[:1] != card[:1] and guess[5:] == card[5:]:
        print("Wrong number, guess again")
      else:
        print("Wrong number and suit, guess again")
    elif card[:5] == "Queen":
      #guess is blank
      if guess == "":
        print("Please input a card")
      #right number guessed
      elif guess == card:
        correct = True
        wins += 1
        print("You Win!")
        #run endgame function
        endGame()
      elif guess[:1] == card[:1] and guess[9:] != card[9:]:
        print("Wrong suit, guess again")
      elif guess[:5] != card[:5] and guess[9:] == card[9:]:
        print("Wrong number, guess again")
      else:
        print("Wrong number and suit, guess again")
    else:
      #guess is blank
      if guess == "":
        print("Please input a card")
      #right number guessed
      elif guess == card:
        correct = True;
        wins += 1;
        print("You Win!")
        #run endgame function
        endGame()
      elif guess[:1] == card[:1] and guess[5:] != card[5:]:
        print("Wrong suit, guess again")
      elif guess[:1] != card[:1] and guess[5:] == card[5:]:
        print("Wrong number, guess again")
      else:
        print("Wrong number and suit, guess again")


#starting prompt
print("Would you like to play a game? Y/N")
confirmStart = input("").upper()[:1]

if confirmStart == "Y":
  game()
else:
  print("See you next time")
