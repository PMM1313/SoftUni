# Read the input string
input_string = input()

# Initialize empty strings for digits, letters, and other characters
digits = ""
letters = ""
others = ""

# Loop through each character in the input string
for char in input_string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        others += char

# Print the results
print(digits)
print(letters)
print(others)
