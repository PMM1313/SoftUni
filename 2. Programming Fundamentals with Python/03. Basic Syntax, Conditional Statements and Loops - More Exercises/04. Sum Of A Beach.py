input_string = str(input())

words_to_find = ["Sand", "Water", "Fish", "Sun"]

input_lower = input_string.lower()
words_lower = [word.lower() for word in words_to_find]

total_count = 0

for word in words_lower:
    word_lower = word.lower()
    index = input_lower.find(word)

    while index != -1:
        total_count += 1

        index = input_lower.find(word_lower, index + 1)

print(total_count)
