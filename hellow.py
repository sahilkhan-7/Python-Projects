# import the time module and string module
import string, time

# define the string here to be printed
text = "Hello, World!"

# define a temporary string to store the string
temp = ""

# loop through the string and print each character
for char in text:

    # loop through the printable characters, string.printable is a string of all printable ascii characters
    for i in string.printable:

        # if the character is the same as the current character in the string, print it
        if i == char or char == " ":

            # sleep for 0.02 seconds to make it look like it's being typed
            time.sleep(0.02)
            print(temp+i)

            # add the character to the temporary string
            temp += char
            break

        # if the character is not the same as the current character in the string, print it
        else:
            time.sleep(0.02)
            print(temp + i)


            