
tank_capacity = 255


current_water = 0


n = int(input().strip())


for _ in range(n):

    pour = int(input().strip())

    if current_water + pour > tank_capacity:
        print("Insufficient capacity!")
    else:
        current_water += pour

print(current_water)
