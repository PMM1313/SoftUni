list_of_integers = input()
number = int(input())

list_of_integers = list_of_integers.split()

integers = []

for x in list_of_integers:
    integers.append(int(x))

for num in range(number):
    lowest_number = min(integers)
    integers.remove(lowest_number)

print(", ".join(map(str, integers)))
