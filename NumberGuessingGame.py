#Number Guessing Game Objectives:
import random;
print('welcome to Number Guessing Game!')

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
mode_of_difficulty = input('choose the difficulty mode: easy or hard?')
print('I am thinking of a number between 1 and 100 ')
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
secret_number = random.randint(1, 100);

if mode_of_difficulty == "easy":
  attempts=10
else:
  attempts=5
while(attempts>0):
  guess= int(input("Make a guess"))
  if(guess>secret_number):
    print("Too high.")
  elif (guess<secret_number):
    print("Too low.")
  else:
    print(f"You made the correct guess {guess}");
    break;
  attempts=attempts-1
