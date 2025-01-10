

clothes_in_the_box = input().split(' ')
capacity = int(input())

rack = []
racks_used = 1

while clothes_in_the_box:
    item = int(clothes_in_the_box.pop())
    current_value = sum(rack)

    if item + current_value < capacity:
        rack.append(item)

    elif item + current_value == capacity:
        rack.append(item)
        rack = []

        if clothes_in_the_box:
            racks_used += 1

    elif item + current_value > capacity:
        rack = []
        racks_used += 1
        rack.append(item)

print(racks_used)
