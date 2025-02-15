from collections import deque


def make_potions(substance_stack, crystals):
    potions =\
        {"Brew of Immortality": 110,
        "Essence of Resilience": 100,
        "Draught of Wisdom": 90,
        "Potion of Agility": 80,
        "Elixir of Strength": 70}

    made_potions = []
    crystals = deque(crystals)
    crafted_potions_energy = []

    while substance_stack and crystals:
        substance = substance_stack.pop()
        crystal = crystals.popleft()
        total_energy = substance + crystal

        for potion, energy in potions.items():
            if potion not in made_potions and total_energy == energy:
                made_potions.append(potion)
                crafted_potions_energy.append(energy)
                break
        else:
            possible_energies = [energ for energ in potions.values() if energ <= total_energy and energ not in crafted_potions_energy]
            if possible_energies:
                highest_possible = max(possible_energies)
                for potion, energy in potions.items():
                    if energy == highest_possible and potion not in made_potions:
                        made_potions.append(potion)
                        crafted_potions_energy.append(energy)
                        break
                reduced_crystal = crystal - 20
            else:
                reduced_crystal = crystal - 5

            if reduced_crystal > 0:
                crystals.append(reduced_crystal)

        if len(made_potions) == 5:
            break

    if len(made_potions) == 5:
        print("Success! The alchemist has forged all potions!")
    else:
        print("The alchemist failed to complete his quest.")

    if made_potions:
        print("Crafted potions:", ", ".join(made_potions))

    if substance_stack:
        print("Substances:", ", ".join(map(str, reversed(substance_stack))))

    if crystals:
        print("Crystals:", ", ".join(map(str, crystals)))



substances = list(map(int, input().split(", ")))
crystals = list(map(int, input().split(", ")))

make_potions(substances, crystals)
