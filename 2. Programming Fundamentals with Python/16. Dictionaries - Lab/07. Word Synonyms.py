# Read the number of word-synonym pairs
n = int(input().strip())

# Initialize an empty dictionary to store synonyms
synonyms_dict = {}

# Read the word-synonym pairs
for _ in range(n):
    word = input().strip()
    synonym = input().strip()

    # Check if the word already exists in the dictionary
    if word in synonyms_dict:
        synonyms_dict[word].append(synonym)
    else:
        synonyms_dict[word] = [synonym]

# Print the words and their synonyms in the required format
for word, synonyms in synonyms_dict.items():
    print(f"{word} - {', '.join(synonyms)}")