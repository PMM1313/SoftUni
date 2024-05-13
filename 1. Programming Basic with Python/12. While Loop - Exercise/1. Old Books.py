book_needed = str(input())
book_now = str(input())

is_book_found = False
books_checked = 0

while book_now != 'No More Books':
    if book_now == book_needed:
        is_book_found = True
        print(f'You checked {books_checked} books and found it.')
        break

    books_checked += 1
    book_now = str(input())

if not is_book_found:
    print(f'The book you search is not here!')
    print(f'You checked {books_checked} books.')

