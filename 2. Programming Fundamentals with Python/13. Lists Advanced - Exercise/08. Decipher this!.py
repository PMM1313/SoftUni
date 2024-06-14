def decipher_message(message):
    words = message.split()
    deciphered_message = []

    for word in words:
        # Extract ASCII code number and the rest of the word
        code = int(''.join(filter(str.isdigit, word)))  # Extract digits and convert to int
        rest_of_word = ''.join(filter(lambda x: not x.isdigit(), word))  # Remove digits

        # Swap the second and last letter
        if len(rest_of_word) > 1:
            modified_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]
        else:
            modified_word = rest_of_word

        # Combine ASCII character with modified word
        deciphered_word = chr(code) + modified_word
        deciphered_message.append(deciphered_word)

    # Join the deciphered words into a single string and print
    print(' '.join(deciphered_message))


# Example usage:
message = input()
decipher_message(message)