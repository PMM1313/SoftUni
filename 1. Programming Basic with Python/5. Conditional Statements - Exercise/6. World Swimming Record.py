import math

record = float(input())
distance = float(input())
time = float(input())

water_resistance = math.floor(distance / 15)
time_delay = water_resistance * 12.5
have_to_swim = distance * time

total_time = have_to_swim + time_delay

if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')

else:
    needed_second = total_time - record
    print(f'No, he failed! He was {needed_second:.2f} seconds slower.')
