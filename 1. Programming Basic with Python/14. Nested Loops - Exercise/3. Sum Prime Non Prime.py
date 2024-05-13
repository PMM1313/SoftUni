sum_prime = 0
sum_non_prime = 0

while True:
    number = input()
    if number == "stop":
        break

    number = int(number)

    if number < 0:
        print("Number is negative.")
        continue

    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += number
    else:
        sum_non_prime += number

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
