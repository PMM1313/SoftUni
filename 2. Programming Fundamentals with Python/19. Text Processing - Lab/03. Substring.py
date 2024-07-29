# Read the two input strings
substring = input()
main_string = input()

# Loop to remove all occurrences of the substring from the main string
while substring in main_string:
    main_string = main_string.replace(substring, "")

# Print the resulting string
print(main_string)