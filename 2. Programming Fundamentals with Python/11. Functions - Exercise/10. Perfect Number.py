def is_perfect_number(number):
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum == number


number = int(input())
if is_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")