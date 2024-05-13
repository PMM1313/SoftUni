import string

####
# PART 1: read and clean data
with open("pride_and_prejudice.txt") as file:
    text = file.read()

# Clean data by removing capitalisation and punctuation marks
text = text.lower()
for punctuation_mark in string.punctuation:
    text = text.replace(punctuation_mark, " ")

# Split string into a list of strings containing all the words
words = text.split()

####
# PART 2: find words and their frequencies
word_frequencies = {}

# Loop through list of words to populate dictionary
for word in words:
    if word not in word_frequencies.keys():
        word_frequencies[word] = 1
    else:
        word_frequencies[word] = word_frequencies[word] + 1

####
# PART 3: Export words and frequencies to a CSV spreadsheet

with open("words in Pride and Prejudice.csv", "w") as file:
    # Write header line
    file.write("Word,Frequency\n")

    # Loop through dictionary and write key-value pairs to csv
    for key, value in word_frequencies.items():
        file.write(f"{key},{value}\n")