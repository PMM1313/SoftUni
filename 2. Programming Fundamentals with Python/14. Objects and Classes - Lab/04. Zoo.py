class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            species_list = self.mammals
            species_name = "Mammals"
        elif species == "fish":
            species_list = self.fishes
            species_name = "Fishes"
        elif species == "bird":
            species_list = self.birds
            species_name = "Birds"
        else:
            return "Invalid species"

        return f"{species_name} in {self.name}: {', '.join(species_list)}\nTotal animals: {Zoo.__animals}"

# Read input
zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())
for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

requested_species = input()

# Print the information for the requested species
print(zoo.get_info(requested_species))