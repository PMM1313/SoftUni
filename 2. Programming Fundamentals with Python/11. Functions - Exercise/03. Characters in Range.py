def characters_in_range(char1: str, char2: str) -> str:

    start = ord(char1)
    end = ord(char2)

    # Ensure the range goes from the smaller ASCII value to the larger one
    if start > end:
        start, end = end, start

    result = ' '.join(chr(i) for i in range(start + 1, end))
    return result



char1 = str(input())
char2 = str(input())
result = characters_in_range(char1, char2)
print(result)