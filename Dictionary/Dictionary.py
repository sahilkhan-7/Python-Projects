# our data is present in json file, so to handle the json we need to
import json

# get_close_matches is used to get the closest match of the word
from difflib import get_close_matches

# loading the data from json file
data = json.load(open("Projects in Python/data.json"))

# defining function to get the meaning of the word
def dict(word):

    # if the word is present in the data then return the meaning of the word
    if word.lower() in data:
        return data[word.lower()]

    # if the word is not present in the data then return the closest match of the word
    elif (len(get_close_matches(word, data.keys()))) > 0:

        # asking the user if the closest match is the word they are looking for
        print(f'Did you mean {get_close_matches(word, data.keys())[0]}')
        decide = input('Enter y for Yes and n for No : ')
        if decide.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide.lower() == 'n':
            return f'The word {word} doesn\'t exist.'
        else:
            return 'Please enter correct input.'

    # if the word isn't present in the data then return the word doesn't exist
    else:
        return f'{word} doesn\'t exist.'


# getting the user input
word = input("Enter the word you want to search : ")
result = dict(word)

# if the result is a list then print each item in the list
if result is not None:
    if type(result) == list:
        for item in result:
            print(item)
    else:
        print(result)
