def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in text if char not in vowels])
    return result


input_text1 = input()


print(remove_vowels(input_text1))
