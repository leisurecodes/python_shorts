# ANSI color codes dictionary
color_codes = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'white': '\033[97m',
    'reset': '\033[0m'  # Reset color
}

# take color input from user
user_color = input("Enter a color " \
    "(red, green, blue, yellow): "
).lower()

# get message from user
message = input("Enter message to display: ")

# display message in user selected color
if user_color in color_codes:
    print(
        color_codes[user_color] + 
        message + 
        color_codes['reset']
    )
else:
    print("Invalid color. Default message: ")
    print(message)