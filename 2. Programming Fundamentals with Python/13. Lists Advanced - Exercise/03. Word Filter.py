def word_filter(text):
    # Split the input text into words
    words = text.split()

    # Use list comprehension to filter words with even length
    even_length_words = [word for word in words if len(word) % 2 == 0]

    # Print each filtered word on a new line
    for word in even_length_words:
        print(word)


text = input()

word_filter(text)
