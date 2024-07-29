# Read the input string
input_string = input()

# Initialize an empty result string
result = ""

# Iterate over the characters in the input string
for i in range(len(input_string)):
    # If it's the first character or different from the previous one, append it to the result
    if i == 0 or input_string[i] != input_string[i - 1]:
        result += input_string[i]

# Print the resulting string
print(result)
