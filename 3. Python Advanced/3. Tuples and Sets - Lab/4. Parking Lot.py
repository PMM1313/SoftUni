
number_of_cars = int(input())
cars = set()

for _ in range(number_of_cars):
    direction, registration = input().split(', ')

    if direction == 'IN':
        cars.add(registration)
    elif direction == 'OUT':
        cars.discard(registration)

print("\n".join(cars) if cars else "Parking Lot is Empty")