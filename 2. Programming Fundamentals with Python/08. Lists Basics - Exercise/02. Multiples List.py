factor = int(input())
count = int(input())

lst = []
iterations = 1

for number in range(count):
    new_number = factor * iterations
    lst.append(new_number)
    iterations += 1
print(lst)
