from collections import deque

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())
crafted_presents = dict()

while True:
    if not materials or not magic_values:
        break

    current_material = materials.pop()
    current_magic = magic_values.popleft()
    total_magic = current_material * current_magic

    if total_magic in presents.keys():
        if presents[total_magic] not in crafted_presents.keys():
            crafted_presents[presents[total_magic]] = 1
            continue
        crafted_presents[presents[total_magic]] += 1
        continue

    if total_magic < 0:
        materials.append(current_material + current_magic)

    elif total_magic > 0:
        current_material += 15
        materials.append(current_material)

    elif total_magic == 0:
        if current_material != 0:
            materials.append(current_material)
        if current_magic != 0:
            magic_values.appendleft(current_magic)

if ('Doll' in crafted_presents and 'Wooden train' in crafted_presents) or \
        ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for key, value in sorted(crafted_presents.items(), key=lambda x: x[0]):
    print(f"{key}: {value}")