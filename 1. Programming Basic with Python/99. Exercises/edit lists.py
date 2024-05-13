
many_numbers = [2, 5, 7, 23, 1, 4, 10]
print(many_numbers)

# change position 3, NUMBER 7
many_numbers[2] = 2000
print(many_numbers)

# put 5000 on the last free position
many_numbers.append(5000)
print(many_numbers)

# remove value from list, in this case NUMBER 23 in the list
many_numbers.remove(23)
print(many_numbers)

# remove position from the list
many_numbers.pop(0)
print(many_numbers)
