
shelf_with_books = input().split('&')
command = ""

while command != "Done":
    command = input()
    if command == "Done":
        break

    command_parts = command.split(' | ')
    operation = command_parts[0]

    if operation == "Add Book":
        book_name = command_parts[1]
        if book_name not in shelf_with_books:
            shelf_with_books.insert(0, book_name)

    elif operation == "Take Book":
        book_name = command_parts[1]
        if book_name in shelf_with_books:
            shelf_with_books.remove(book_name)

    elif operation == "Swap Books":
        book1 = command_parts[1]
        book2 = command_parts[2]
        if book1 in shelf_with_books and book2 in shelf_with_books:
            index1 = shelf_with_books.index(book1)
            index2 = shelf_with_books.index(book2)
            shelf_with_books[index1], shelf_with_books[index2] = shelf_with_books[index2], shelf_with_books[index1]

    elif operation == "Insert Book":
        book_name = command_parts[1]
        if book_name not in shelf_with_books:
            shelf_with_books.append(book_name)

    elif operation == "Check Book":
        index = int(command_parts[1])
        if 0 <= index < len(shelf_with_books):
            print(shelf_with_books[index])

print(", ".join(shelf_with_books))
