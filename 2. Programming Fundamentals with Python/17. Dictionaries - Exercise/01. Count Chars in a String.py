characters = [character for character in input() if character != " "]
letters = {}

for character in characters:
    if character not in letters.keys():
        letters[character] = 0
    letters[character] += 1

for symbol, occ in letters.items():
    print(f'{symbol} -> {occ}')
