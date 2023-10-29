book_name = input()
book_counter = 0
flag_found = False

while True:
    data = input()

    if data == 'No More Books':
        break
    if data == book_name:
        flag_found = True
        break

    book_counter += 1

if flag_found:
    print(f"You checked {book_counter} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_counter} books.")
