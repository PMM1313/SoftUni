first_number = int(input())
second_number = int(input())
third_number = int(input())

for first in range(2, first_number + 1, 2):
    for second in (2, 3, 5, 7):
        if second <= second_number:
            for third in range(2, third_number + 1, 2):
                # pin = f"{first} {second} {third}"
                print(f"{first} {second} {third}")

# I cried here ...
