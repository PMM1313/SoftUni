import math

radius_as_r = float(input())

pi = 3.14
# calculating area and parameter

area = math.pi * radius_as_r ** 2
parameter = 2 * math.pi * radius_as_r


print(f'{area:.2f}')
print(f'{parameter:.2f}')
