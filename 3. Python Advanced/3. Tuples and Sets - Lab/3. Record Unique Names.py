number_of_names = int(input())

my_set = set()

for _ in range(number_of_names):
    name = input()
    my_set.add(name)

for name in my_set:
    print(f'{name}')
