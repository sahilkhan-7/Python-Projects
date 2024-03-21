# import random
# from words import words
# import string


# def get_valid_word(words):
#     word = random.choice(words)  # randomly chooses something from the list
#     while '-' in word or ' ' in word:
#         word = random.choice(words)

#     return word.upper()


# def hangman():
#     word = get_valid_word(words)
#     word_letters = set(word)  # letters in the word
#     alphabet = set(string.ascii_uppercase)
#     used_letters = set()  # what the user has guessed

#     lives = 7

#     # getting user input
#     while word_letters and lives > 0:
#         # letters used
#         # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
#         print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

#         # what current word is (ie W - R D)
#         word_list = [letter if letter in used_letters else '-' for letter in word]

#         print('Current word: ', ' '.join(word_list))

#         user_letter = input('Guess a letter: ').upper()
#         if user_letter in alphabet - used_letters:
#             used_letters.add(user_letter)
#             if user_letter in word_letters:
#                 word_letters.remove(user_letter)
#                 print('')

#             else:
#                 lives -= 1
#                 print('\nYour letter,', user_letter, 'is not in the word.')

#         elif user_letter in used_letters:
#             print('\nYou have already used that letter. Guess another letter.')

#         else:
#             print('\nThat is not a valid letter.')

#     # gets here when len(word_letters) == 0 OR when lives == 0
#     if lives == 0:
#         print(lives_visual_dict[lives])
#         print('You died, sorry. The word was', word)
#     else:
#         print('YAY! You guessed the word', word, '!!')


# if __name__ == '__main__':
#     hangman()


import random



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

def choose_word():
    words = ['python', 'hangman', 'programming', 'computer', 'science', 'algorithm', 'developer', 'software']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word has", len(word), "letters.")

    while True:
        print("\nAttempts left:", attempts)
        print("Guessed letters:", guessed_letters)
        print("Word:", display_word(word, guessed_letters))

        if '_' not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word:", word)
            break

        if attempts == 0:
            print("Sorry, you've run out of attempts. The word was:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Sorry, that letter is not in the word.")
            attempts -= 1

hangman()



def hangman(name):
    validletters = string.ascii_uppercase
    word = random.choice(words).upper()
    guessed_letters = []

    guessmade = ''
    lives = 8
    while len(word)>0:
        print("\nLives left:", lives)
        print("Guessed letters:", guessed_letters)
        print("Word:", display_word(word, guessed_letters))
        
        current_word = ''

        for letter in word:
            if letter in guessmade:
                current_word = current_word + letter
            else :
                current_word = current_word + '_' + ' '

        if current_word == word:
            print(current_word)
            print("Congratulations! You've guessed the word:", word)
            break

        print('Guess the word', current_word)
        user_letter = input('Enter your user_letter: ').upper()

        if user_letter in validletters:
            guessmade += user_letter
        else:
            user_letter = input('Enter a valid character: ').upper()


        if user_letter not in word:
            lives -= 1
            if lives == 7:
                print('You have 9 lives left.')
                print(stages[0])

            if lives == 6:
                print('You have 8 lives left.')
                print(stages[1])

            if lives == 5:
                print('You have 7 lives left.')
                print(stages[2])

            if lives == 4:
                print('You have 6 lives left.')
                print(stages[3])

            if lives == 3:
                print('You have 5 lives left.')
                print(stages[4])

            if lives == 2:
                print('You have 4 lives left.')
                print(stages[5])
            
            if lives == 1:
                print(f'{name}, last Breath counting. Take care')
                print('You have 3 lives left.')
                print(stages[6])
            
            if lives == 0:
                print('You have 2 lives left.')
                print(stages[7])
                print(f'{name}, you let the kind man die. ')
                print('The word is ', word)
                break


if __name__ == '__main__':
    print(logo)
    name = input('Enter your name: ')
    choice = input('Do you wanna play: ')
    if choice == 'yes' or choice == 'Yes' or choice == 'Y' or choice == 'y':
        hangman(name)
    else:
        print('ok, exiting the program.')