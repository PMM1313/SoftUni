def assess_happiness():
    # Read input
    happiness_input = input().split()
    factor = int(input())

    # Convert the input strings to integers
    happiness_levels = list(map(int, happiness_input))

    # Multiply each employee's happiness by the factor
    improved_happiness = [h * factor for h in happiness_levels]

    # Calculate the average happiness
    average_happiness = sum(improved_happiness) / len(improved_happiness)

    # Count the number of employees with happiness greater than or equal to the average
    happy_count = len([h for h in improved_happiness if h >= average_happiness])
    total_count = len(improved_happiness)

    # Print the result
    if happy_count >= total_count / 2:
        print(f"Score: {happy_count}/{total_count}. Employees are happy!")
    else:
        print(f"Score: {happy_count}/{total_count}. Employees are not happy!")


# Example usage:
assess_happiness()