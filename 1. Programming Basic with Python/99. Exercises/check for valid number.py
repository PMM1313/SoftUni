import math

NUMBER = input("Enter a NUMBER: ")

specific_characters = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ','}


def convert_number_to_float():  # Convert the input NUMBER to a float
    try:
        num = float(NUMBER)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()

    return num


if ',' in NUMBER and all(char in specific_characters for char in NUMBER):
    valid_number = NUMBER.replace(',', '.')
    if valid_number.count('.') <= 1:
        print("Modified number:", valid_number)
        NUMBER = valid_number

        converted_number = convert_number_to_float()

        # Round the NUMBER up to the next higher NUMBER to the second decimal place
        rounded_number = math.ceil(converted_number * 100) / 100

        if valid_number != converted_number:
            print("Rounded number:", rounded_number)
        else:
            pass
    else:
        print("Too much ',' in the number. Please enter a valid number.")
