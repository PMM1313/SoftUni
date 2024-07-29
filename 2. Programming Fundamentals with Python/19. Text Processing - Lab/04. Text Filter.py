# Read the banned words and text from input
banned_words = input().split(", ")
text = input()

# Loop through each banned word
for word in banned_words:
    # Create a replacement string of asterisks of the same length as the banned word
    replacement = '*' * len(word)
    # Replace all occurrences of the banned word in the text with the replacement string
    text = text.replace(word, replacement)

# Print the resulting text
print(text)
