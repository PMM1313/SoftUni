from collections import deque

liters = int(input())

people = deque()

name = input()

while name != 'Start':
    people.append(name)
    name = input()

command = input()
while command != 'End':
    if command.startswith('refill'):
        _, litters_to_refill = command.split()
        litters_to_refill = int(litters_to_refill)
        liters += litters_to_refill
    else:
        litters_requested = int(command)
        name = people.popleft()
        if litters_requested <= liters:
            liters -= litters_requested
            print(f'{name} got water')
        else:
            print(f'{name} must wait')
    command = input()
print(f'{liters} liters left')
