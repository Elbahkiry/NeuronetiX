from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

logo = """
    ______                                         ____  _____                       __                       
 .' ___  |                                       |_   \|_   _|                     [  |                      
/ .'   \_| __   _   .---.  .--.   .--.    ,--.     |   \ | |  __   _   _ .--..--.   | |.--.   .---.  _ .--.  
| |   ____[  | | | / /__\\( (`\] ( (`\]  `'_\ :    | |\ \| | [  | | | [ `.-. .-. |  | '/'`\ \/ /__\\[ `/'`\] 
\ `.___]  || \_/ |,| \__., `'.'.  `'.'.  // | |,  _| |_\   |_ | \_/ |, | | | | | |  |  \__/ || \__., | |     
 `._____.' '.__.'_/ '.__.'[\__) )[\__) ) \'-;__/ |_____|\____|'.__.'_/[___||__||__][__;.__.'  '.__.'[___]    
                                                                                                             
"""
#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"Nice work, The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL

print(logo)
#Choosing a random number between 1 and 100.
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
print(f"Test, the correct answer is {answer}") 

turns = set_difficulty()
guess = 0
game_is_on = True
while guess != answer and game_is_on:
  print(f"You have {turns} attempts remaining to guess the number.")

  guess = int(input("Make a guess: "))

  turns = check_answer(guess, answer, turns)
  if turns == 0:
    print("You've run out of guesses, you lose.")
    game_is_on = False
  elif guess != answer:
    print("Guess again.")



