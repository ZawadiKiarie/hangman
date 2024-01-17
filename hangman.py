import random
from words import words
import string 

def get_valid_word(words):
  word = random.choice(words)
  while '-' in word or ' ' in word:
    word = random.choice(words)

  return word.upper()

def hangman():
  word = get_valid_word(words)
  lives = 6
  word_letters = set(word)#letters in the word
  alphabet = set(string.ascii_uppercase)
  used_letters = set()#store what the user has guessed

  

  while len(word_letters) > 0 and lives > 0:
    print("You have", lives, "lives left and your used letters are: ", ' '.join(used_letters))
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print("Current word: " , ' '.join(word_list))
    
    used_letter = input("Guess a letter that is in the word: ").upper()
    if used_letter in alphabet - used_letters:#valid character in the alphabet that i haven't used
      used_letters.add(used_letter)
      if used_letter in  word_letters:
        word_letters.remove(used_letter)
      else:
        lives = lives - 1
        print("Letter is not in the word.")
    elif used_letter in used_letters:
      print("You already used that letter. Try again")
    else:
      print("Invalid character. Try again")

  #gets here(breaks  out of loop) when len(word_letters) == 0 meaning they have guesses the word correctly OR lives == 0 they have died
  if lives == 0:
    print(f"You Died! The word was {word}")
  else:
    print(f"You won! The word was {word}")

hangman()
