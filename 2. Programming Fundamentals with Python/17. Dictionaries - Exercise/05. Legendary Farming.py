key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
obtained_item = None

legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

while not obtained_item:
    materials = input().lower().split()

    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1]

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                obtained_item = legendary_items[material]
                key_materials[material] -= 250
                break
        else:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += quantity

    if obtained_item:
        print(f"{obtained_item} obtained!")

        for material, quantity in key_materials.items():
            print(f"{material}: {quantity}")

        for material, quantity in junk_items.items():
            print(f"{material}: {quantity}")
