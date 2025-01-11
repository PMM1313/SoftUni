
number_of_guests = int(input())

normal_guests = set()
vip_guests = set()

for _ in range(number_of_guests):
    guest_number = input()

    if guest_number[0].isdigit():  # Check if the first character is a digit
        vip_guests.add(guest_number)
    else:
        normal_guests.add(guest_number)

guest_or_command = 0
while guest_or_command != 'END':
    guest_or_command = input()
    if guest_or_command == 'END':
        break
    elif guest_or_command[0].isdigit():  # Check if the first character is a digit
        vip_guests.remove(guest_or_command)
    else:
        normal_guests.remove(guest_or_command)


print(len(vip_guests) + len(normal_guests))
if vip_guests:
    sorted_vip = sorted(vip_guests)
    print("\n".join(sorted_vip))
if normal_guests:
    sorted_norm = sorted(normal_guests)
    print("\n".join(sorted_norm))