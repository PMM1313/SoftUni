
def classify_books(*args, **kwargs):
    fiction_books = {}
    non_fiction_books = {}

    for genre, title in args:
        for isbn, book_title in kwargs.items():
            if book_title == title:
                if genre == "fiction":
                    fiction_books[isbn] = title
                else:
                    non_fiction_books[isbn] = title

    fiction_sorted = sorted(fiction_books.items())

    non_fiction_sorted = sorted(non_fiction_books.items(), reverse=True)

    result = []

    if fiction_sorted:
        result.append("Fiction Books:")
        for isbn, title in fiction_sorted:
            result.append(f"~~~{isbn}#{title}")

    if non_fiction_sorted:
        result.append("Non-Fiction Books:")
        for isbn, title in non_fiction_sorted:
            result.append(f"***{isbn}#{title}")

    return "\n".join(result)
