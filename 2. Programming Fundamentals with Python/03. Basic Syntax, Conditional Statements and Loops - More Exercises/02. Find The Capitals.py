word = input()

capital_letter_list = []

for index, letter in enumerate(word):
    if letter.isupper():
        capital_letter_list.append(index)

print(capital_letter_list)
