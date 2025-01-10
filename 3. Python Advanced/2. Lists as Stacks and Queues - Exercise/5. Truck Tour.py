
number_of_pumps = int(input())

petrol_pumps = [tuple(map(int, input().split())) for _ in range(number_of_pumps)]

total_balance = 0
current_balance = 0
start_index = 0


for i in range(number_of_pumps):
    petrol, distance = petrol_pumps[i]
    total_balance += petrol - distance
    current_balance += petrol - distance

    if current_balance < 0:
        start_index = i + 1
        current_balance = 0

# Output the starting index
print(start_index)
