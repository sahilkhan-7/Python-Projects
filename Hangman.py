import random

def hangman(name):
    words = ['Fruits', 'Monkey', 'Children', 'thor', 'iron man', 'Google', 'Homemade', 'Awesome', 
             'Hello', 'World', 'programming', 'lizard', 'Pokemon', 'Superman', 'Pad man']
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    word = random.choice(words)
    # word = 'pineapple'

    guessmade = ''
    turns = 10
    while len(word)>0:
        main = ''
        # missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else :
                main = main + '_' + ' '

        if main == word:
            print(main)
            print('You win!')
            break

        print('Guess the word', main)
        guess = input('Enter your guess: ')

        if guess in validletters:
            guessmade += guess
        else:
            guess = input('Enter a valid character: ')


        if guess not in word:
            turns -= 1
            if turns == 9:
                print('You have 9 turns left.')
                print('---------------------')

            if turns == 8:
                print('You have 8 turns left.')
                print('---------------------')
                print('          O          ')

            if turns == 7:
                print('You have 7 turns left.')
                print('---------------------')
                print('          O          ')
                print('          |          ')

            if turns == 6:
                print('You have 6 turns left.')
                print('---------------------')
                print('          O          ')
                print('          |          ')
                print("         /           ")

            if turns == 5:
                print('You have 5 turns left.')
                print('---------------------')
                print('          O          ')
                print('          |          ')
                print("         / \\        ")

            if turns == 4:
                print('You have 4 turns left.')
                print('---------------------')
                print('        \\ O          ')
                print('          |          ')
                print("         / \\        ")
            
            if turns == 3:
                print('You have 3 turns left.')
                print('---------------------')
                print('        \\ O /       ')
                print('          |          ')
                print("         / \\        ")
            
            if turns == 2:
                print('You have 2 turns left.')
                print('---------------------')
                print('        \\ O /|        ')
                print('          |          ')
                print("         / \\        ")

            if turns == 1:
                print(f'{name}, last Breath counting. Take care')
                print('---------------------')
                print('       \\ O_|/       ')
                print('          |          ')
                print('         / \\        ')

            if turns == 0:
                print(f'{name}, you let the kind man die. ')
                print('---------------------')
                print('          O_|        ')
                print('         /|\\        ')
                print("         / \\        ")

                print()
                print('The word is ', word)
                break


        
name = input('Enter your name: ')
choice = input('Do you wanna play: ')
if choice == 'yes' or choice == 'Yes' or choice == 'Y' or choice == 'y':
    hangman(name)
else:
    print('ok, exiting the program.')
        