# Read the input string
text = input()

# Initialize the encrypted text variable
encrypted_text = ""

# Loop through each character in the input text
for char in text:
    # Shift the character by 3 positions forward in the ASCII table
    encrypted_char = chr(ord(char) + 3)
    # Append the encrypted character to the result
    encrypted_text += encrypted_char

# Print the encrypted text
print(encrypted_text)
