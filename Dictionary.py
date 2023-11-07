import json
from difflib import get_close_matches
data = json.load(open("Projects in Python/data.json"))


def dict(word):
    if word.lower() in data:
        return data[word.lower()]

    elif (len(get_close_matches(word, data.keys()))) > 0:
        print(f'Did you mean {get_close_matches(word, data.keys())[0]}')
        decide = input('Enter y for Yes and n for No : ')
        if decide.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide.lower() == 'n':
            return f'The word {word} doesn\'t exist.'
        else:
            return 'Please enter correct input.'

    else:
        return f'{word} doesn\'t exist.'


word = input("Enter the word you want to search : ")
result = dict(word)


if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)
