def reverse_text(text):
    index = len(text) - 1

    while index >= 0:
        yield text[index]
        index -= 1