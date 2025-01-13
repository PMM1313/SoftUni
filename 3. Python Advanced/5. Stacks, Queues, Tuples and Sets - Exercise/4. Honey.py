from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar_value = [int(x) for x in input().split()]
symbols = deque(input().split())

dict_symbols = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}

honey_made = 0
while nectar_value and working_bees:
    if working_bees[0] > nectar_value[-1]:
        nectar_value.pop()
    else:
        current_symbol = symbols.popleft()
        if current_symbol == '/' and nectar_value[-1] == 0:
            working_bees.popleft()
            nectar_value.pop()
        else:
            honey_made += abs(dict_symbols[current_symbol](working_bees.popleft(), nectar_value.pop()))

print(f"Total honey made: {honey_made}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar_value:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_value)}")


