file = open("numbers.txt")

content = file.readlines()
# print(content.split("\map_size"))

total_sum = 0
for el in content:
    try:
        total_sum += int(el[:-1])
    except ValueError:
        continue

print(total_sum)