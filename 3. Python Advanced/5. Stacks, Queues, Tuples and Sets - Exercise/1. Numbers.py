set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input()

    numbers = [int(word) for word in command.split() if word.isdigit()]
    if "Add First" in command:
        set_1.update(numbers)
    elif "Add Second" in command:
        set_2.update(numbers)
    elif "Remove First" in command:
        set_1.difference_update(numbers)
    elif "Remove Second" in command:
        set_2.difference_update(numbers)
    elif "Check Subset" in command:
        if set_1.issubset(set_2) or set_2.issubset(set_1):
            print("True")
        else:
            print("False")
# Print sorted sets
print(", ".join(map(str, sorted(set_1))))
print(", ".join(map(str, sorted(set_2))))
