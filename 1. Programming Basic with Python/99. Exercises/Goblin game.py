import random

# Display welcome messages
print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and excitement (!)")

# Get player name
player_name = input("What is your name? ")
num_letters = len(player_name)
if num_letters <= 2:
    print(f"Who the fuck named you '{player_name}' ?")

# Get the desired NUMBER of doors within the specified range
while True:
    try:
        desired_number_of_doors = int(input("Enter the desired NUMBER of doors (between 5 and 10): "))
        if not (5 <= desired_number_of_doors <= 10):
            print("The desired NUMBER of doors needs to be in the range of 5 to 10.")
            if desired_number_of_doors == 10:
                print('Feeling lucky, uh ? Good luck finding the motherfucker')
        else:
            break  # Break the loop if input is valid
    except ValueError:  # Handle non-integer input
        print("Please enter a valid NUMBER from 5 to 10.")

print(player_name + ", can you find the goblin?")

print("|_|" * desired_number_of_doors)

goblin_position = random.randint(1, desired_number_of_doors, )

keep_trying = True

# Main game loop
times_not_found = 0
max_attempts = 5  # Adjust as needed
guessed_position = 0
typed_letter = 0

while keep_trying:
    try:
        guessed_position = int(input("Can you guess where the goblin is hiding? "))
        if not 1 <= guessed_position <= desired_number_of_doors:  # Check if guessed position is within the range
            print("Please guess a NUMBER between 1 and", desired_number_of_doors)
            continue
    except ValueError:  # Handle non-integer input
        typed_letter += 1
        if typed_letter == 3:
            print('You typed a letter 3 times in a row ... are you an idiot ?')
        print(f"Please enter a valid NUMBER from 1 to {desired_number_of_doors}.")
        continue

    if guessed_position == goblin_position:  # If player guesses correctly
        print("Well done. You've found the goblin.")
        keep_trying = False
    else:  # If player's guess is incorrect
        times_not_found += 1

        if times_not_found < 3:
            print("No, sorry. The goblin is still hiding somewhere.")

        if times_not_found == 3:
            print("Goblin is well hidden, uh... :D")

        if times_not_found == max_attempts:
            print("Goblin is hidden too well. No point in searching more. Closing the game.")
            break

print("Thank you for playing. Now get back to work!")
