
string1 = input()
string2 = input()


last_printed = string1


for letter in range(len(string1)):

    new_string = string2[:letter + 1] + string1[letter + 1:]

    if new_string != last_printed:
        print(new_string)
        last_printed = new_string
