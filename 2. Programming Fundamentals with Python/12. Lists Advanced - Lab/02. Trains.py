def train_operations(num_wagons):


    train = [0] * num_wagons

    while True:
        command = input()

        if command == "End":
            break

        parts = command.split()
        action = parts[0]

        if action == "add":
            people = int(parts[1])
            train[-1] += people
        elif action == "insert":
            index = int(parts[1])
            people = int(parts[2])
            train[index] += people
        elif action == "leave":
            index = int(parts[1])
            people = int(parts[2])
            train[index] -= people


    print(train)

# Read the number of wagons
num_wagons = int(input())


train_operations(num_wagons)