gifts_list = input()

gifts_list = gifts_list.split()
command = ''
while command != 'No Money':
    command = input()

    words = command.split()

    if 'OutOfStock' in words:
        item = words[1]
        for i in range(len(gifts_list)):
            if gifts_list[i] == item:
                gifts_list[i] = 'None'

    if 'Required' in command:
        new_gift = words[1]
        index = int(words[2])

        if 0 <= index < len(gifts_list):
            gifts_list[index] = new_gift

    if 'JustInCase' in command:
        new_gift = words[1]

        gifts_list[-1] = new_gift

for gift in gifts_list[:]:
    if gift == 'None':
        gifts_list.remove(gift)


print(' '.join(gifts_list))

