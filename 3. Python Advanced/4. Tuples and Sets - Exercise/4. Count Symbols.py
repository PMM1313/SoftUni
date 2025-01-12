string_input = input()

letters_count = {}

# Count the frequency of each character
for i in string_input:
    if i not in letters_count:
        letters_count[i] = 1
    else:
        letters_count[i] += 1

# Sort the keys alphabetically
sorted_keys = sorted(letters_count.keys())

# Print the formatted output
print("\n".join([f"{char}: {letters_count[char]} time/s" for char in sorted_keys]))