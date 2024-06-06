def round_numbers(string):
    rounded = []
    converted = []

    for element in string:
        element = float(element)
        converted.append(element)

    for number in converted:
        rounded_number = round(number)
        rounded.append(rounded_number)
    return rounded


string = input().split()
lst = round_numbers(string)
print(lst)
