# Read the key and the number of lines
key = int(input())
num_lines = int(input())

# Iterate over each line
for _ in range(num_lines):
    # Read the input character
    input_char = input()

    # Convert the character to its ASCII value and add the key
    shifted = ord(input_char) + key

    # Print the shifted character
    print(chr(shifted), end='')
