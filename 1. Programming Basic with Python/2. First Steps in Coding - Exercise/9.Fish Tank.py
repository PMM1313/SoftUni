
length = int(input())
wide = int(input())
height = int(input())
used_space = float(input())

# calculating percentage
used_space_as_percentage = used_space / 100


# calculating volume
volume_of_fish_tank = length * wide * height
cubics_to_litters = volume_of_fish_tank / 1000
litters_of_fish_tank = cubics_to_litters

# volume without used space in fish tank
net_volume = litters_of_fish_tank*(1-used_space_as_percentage)

print(net_volume)
