# Read input from the user
input_words = input().strip().lower().split()

# Create a dictionary to count occurrences of each word
word_count = {}
for word in input_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Collect words with odd occurrences
result = [word for word, count in word_count.items() if count % 2 != 0]

# Print the result in lowercase
print(" ".join(result))
