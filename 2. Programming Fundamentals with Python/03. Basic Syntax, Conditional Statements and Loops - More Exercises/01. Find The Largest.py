number = str(input())

sorted_digits = sorted(number, reverse=True)

largest_num_str = ''.join(sorted_digits)

largest_num = int(largest_num_str)

print(largest_num)
