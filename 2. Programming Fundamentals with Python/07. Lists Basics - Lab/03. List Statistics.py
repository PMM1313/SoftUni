n = int(input())

positives = []
negatives = []

for _ in range(n):
    current_number = int(input())

    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)

count_positives = len(positives)
count_negatives = sum(negatives)
print(positives)
print(negatives)

print(f'Count of positives: {count_positives}')
print(f'Sum of negatives: {count_negatives}')
