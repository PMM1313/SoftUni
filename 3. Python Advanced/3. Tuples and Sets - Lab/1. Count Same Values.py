
list_with_numbers = tuple([float(el) for el in input().split()])

data = {}
for el in list_with_numbers:
    data[el] = list_with_numbers.count(el)

for key, value in data.items():
    print(f"{key:.1f} - {value} times")