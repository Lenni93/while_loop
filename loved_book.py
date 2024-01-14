search_book = input()
counter_book = 0
book_is_found = False
current_book = input()
while current_book != 'No More Books':
    if current_book == search_book:
        book_is_found = True
        break
    counter_book += 1
    current_book = input()
if book_is_found:
    print(f'You checked {counter_book} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {counter_book} books.')
