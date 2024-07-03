# Read input from the user
input_string = input().strip()

# Split the input string by ", " to get individual characters
characters = input_string.split(", ")

# Create a dictionary using dictionary comprehension to map characters to their ASCII values
ascii_dict = {char: ord(char) for char in characters}

# Print the resulting dictionary
print(ascii_dict)