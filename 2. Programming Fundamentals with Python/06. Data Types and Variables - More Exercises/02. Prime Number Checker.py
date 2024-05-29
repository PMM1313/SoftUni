import math


number = int(input())


if number <= 1:
    is_prime = False
else:
    is_prime = True

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break

# Print the result
if is_prime:
    print(f"True")
else:
    print(f"False")
