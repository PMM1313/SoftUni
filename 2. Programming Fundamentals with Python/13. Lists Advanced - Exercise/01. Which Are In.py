def find_substrings():
    # Read input sequences
    first_sequence = input().split(", ")
    second_sequence = input().split(", ")

    # Find substrings
    result = []
    for s1 in first_sequence:
        for s2 in second_sequence:
            if s1 in s2:
                result.append(s1)
                break

    # Print the result
    print(result)


# Example usage:
find_substrings()