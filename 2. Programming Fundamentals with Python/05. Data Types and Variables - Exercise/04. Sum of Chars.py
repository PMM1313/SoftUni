
number_of_lines = int(input())
total_sum = 0

for number in range(number_of_lines):

    letter = input()
    code = ord(letter)
    total_sum += code

print(f'The sum equals: {total_sum}')
