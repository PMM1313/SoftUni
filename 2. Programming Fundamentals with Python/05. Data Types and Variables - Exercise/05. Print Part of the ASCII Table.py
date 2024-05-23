
start_index = int(input())
end_index = int(input())

ascii_characters = []

for index in range(start_index, end_index + 1):
    ascii_characters.append(chr(index))

output = ' '.join(ascii_characters)

print(output)
