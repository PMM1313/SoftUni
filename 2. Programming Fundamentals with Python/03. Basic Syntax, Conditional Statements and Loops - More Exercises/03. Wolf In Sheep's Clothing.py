
input_string = input()

words = input_string.split(', ')
iterations = 0
wolf_found = 0

for word in reversed(words):
    iterations += 1

    if word == 'wolf':
        wolf_found = iterations
        if iterations == 1:
            print('Please go away and stop eating my sheep')
            break

    elif word == 'sheep':
        continue

if iterations > 1:
    sheep_number = wolf_found - 1
    print(f'Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!')

