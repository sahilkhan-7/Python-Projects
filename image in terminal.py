from PIL import Image

# Open the image
image = Image.open("Projects in Python/hanging spiderman.jpg")

# Define the characters used to represent different shades in ASCII art
ASCII_CHARS = "@%#*+=-:. "

# Resize the image and convert it to grayscale
image = image.resize((50, 50))
image = image.convert('L')

# Determine the range of pixel values in the image
min_pixel_value = min(image.getdata())
max_pixel_value = max(image.getdata())

max_width = 100
max_height = 40

if image.width > max_width or image.height > max_height:
    image.thumbnail((max_width, max_height))

# Convert the image to ASCII art
ascii_art = ""

for pixel_value in image.getdata():
    # Normalize the pixel value to fit within the range of ASCII_CHARS
    normalized_value = int((pixel_value - min_pixel_value) / (max_pixel_value - min_pixel_value) * (len(ASCII_CHARS) - 1))
    ascii_art += ASCII_CHARS[normalized_value]

# Print the ASCII art to the terminal
print(ascii_art)
