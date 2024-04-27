import random
from words import words
import string

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
      |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''' , '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''' , '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''' , '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

def hangman(name):
    valid_letters = set(string.ascii_uppercase)
    word = random.choice(words).upper()
    # word = 'pineapple'

    guessed_letters = set()
    lives = 8
    while len(word) > 0:
        current_word = ''
        # missed = 0

        for letter in word:
            if letter in guessed_letters:
                current_word += letter
            else :
                current_word += '_' + ' '

        if '_' not in current_word:
            print(current_word)
            print("Congratulations! You've guessed the word:", word)
            break

        print('Guess the word', current_word)
        print('Used letters:', ' '.join(guessed_letters))
        print('Lives left:', lives)

        user_letter = input('Enter your letter: ').upper()

        if user_letter in valid_letters:
            if user_letter in guessed_letters:
                print('You have already guessed that letter.')
            else:
                guessed_letters.add(user_letter)
                if user_letter not in word:
                    print(f'Oops! {user_letter} is not in the word.')
                    print(stages[8 - lives])
                    lives -= 1

                    if lives == 0:
                        print(f'{name}, you let the kind man die.')
                        print('The word was', word)
                        break
        else:
            print('Invalid input. Please enter a valid letter.')

if __name__ == '__main__':
    print(logo)
    name = input('Enter your name: ')
    choice = input('Do you want to play? (yes/no): ').strip().lower()
    if choice == 'yes' or choice == 'y':
        hangman(name)
    else:
        print('Okay, exiting the program.')
