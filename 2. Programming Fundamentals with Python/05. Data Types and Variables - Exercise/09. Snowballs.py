import math

number_of_snow_balls = int(input())

best_value = 0
best_weigth = 0
best_time = 0
best_quality = 0
rounded_best_value = 0

for snowball in range(1, number_of_snow_balls + 1):
    weigth = int(input())
    time = int(input())
    quality = int(input())

    value_for_ball = (weigth / time) ** quality

    if value_for_ball > best_value:
        best_value = value_for_ball
        rounded_best_value = math.floor(best_value)
        best_weigth = weigth
        best_time = time
        best_quality = quality

print(f'{best_weigth} : {best_time} = {rounded_best_value} ({best_quality})')
