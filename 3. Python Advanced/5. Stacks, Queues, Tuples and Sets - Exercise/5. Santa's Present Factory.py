from collections import deque

# Input
materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

# Toy magic requirements
toys_magic = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}

# Dictionary to keep count of crafted presents
crafted_presents = {toy: 0 for toy in toys_magic.values()}

# Process while there are materials and magic values
while materials and magic:
    current_material = materials[-1]
    current_magic = magic[0]

    # If either value is zero, remove it
    if current_material == 0:
        materials.pop()
        continue
    if current_magic == 0:
        magic.popleft()
        continue

    # Calculate total magic level
    total_magic = current_material * current_magic

    if total_magic in toys_magic:
        # Craft the present
        crafted_presents[toys_magic[total_magic]] += 1
        materials.pop()
        magic.popleft()
    elif total_magic < 0:
        # Sum the values together if the product is negative
        materials.pop()
        magic.popleft()
        materials.append(current_material + current_magic)
    else:
        # Increase material by 15 and remove magic value if product is positive but doesn't match any toy
        magic.popleft()
        materials[-1] += 15

# Check if at least one of the required pairs of presents is crafted
success = (
    crafted_presents["Doll"] > 0 and crafted_presents["Wooden train"] > 0
) or (crafted_presents["Teddy bear"] > 0 and crafted_presents["Bicycle"] > 0)

# Output results
if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for toy, count in sorted(crafted_presents.items()):
    if count > 0:
        print(f"{toy}: {count}")
