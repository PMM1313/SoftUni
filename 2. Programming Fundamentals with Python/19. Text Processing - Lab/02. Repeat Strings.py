# Read the input string
input_string = input()

# Split the input string into individual words
words = input_string.split()

# Initialize an empty result string
result = ""

# Loop through each word
for word in words:
    # Repeat the word N times, where N is the length of the word
    repeated_word = word * len(word)
    # Add the repeated word to the result string
    result += repeated_word

# Print the final concatenated result string
print(result)