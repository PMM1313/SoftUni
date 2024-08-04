from collections import defaultdict


def process_commands():
    # Dictionary to store plant information
    plants = {}
    # Dictionary to track the count of thirsty plants in each section
    sections = defaultdict(int)

    while True:
        command = input().strip()

        if command == "EndDay":
            break

        if command.startswith("Plant:"):
            # Handle adding or updating plant records
            _, details = command.split("Plant: ")
            plant_name, water_needed, section = details.split('-')
            water_needed = int(water_needed)

            if plant_name in plants:
                # Update water needed for existing plant without changing section
                current_plant = plants[plant_name]
                current_plant['water_needed'] += water_needed
            else:
                # Add new plant record
                plants[plant_name] = {'water_needed': water_needed, 'section': section}
                sections[section] += 1

        elif command.startswith("Water:"):
            # Handle watering plants
            _, details = command.split("Water: ")
            plant_name, water_amount = details.split('-')
            water_amount = int(water_amount)

            if plant_name in plants:
                # Update water needed for the plant
                plant = plants[plant_name]
                plant['water_needed'] -= water_amount

                if plant['water_needed'] <= 0:
                    # Plant is sufficiently watered
                    section = plant['section']
                    del plants[plant_name]
                    sections[section] -= 1
                    if sections[section] == 0:
                        del sections[section]
                    print(f"{plant_name} has been sufficiently watered.")

    # Print results
    print("Plants needing water:")
    if plants:
        for plant, info in plants.items():
            print(f" {plant} -> {info['water_needed']}ml left")

    print("Sections with thirsty plants:")
    if sections:
        for section, count in sections.items():
            print(f" {section}: {count}")
    else:
        print()


if __name__ == "__main__":
    process_commands()

