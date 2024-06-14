def palindrome_strings():
    # Read the input words and the palindrome to search for
    words = input().split()
    search_palindrome = input()

    # Find all palindromes in the input words
    found_palindromes = [word for word in words if word == word[::-1]]

    # Count the occurrences of the given palindrome
    count = found_palindromes.count(search_palindrome)

    # Print the results
    print(found_palindromes)
    print(f"Found palindrome {count} times")

# Example usage: