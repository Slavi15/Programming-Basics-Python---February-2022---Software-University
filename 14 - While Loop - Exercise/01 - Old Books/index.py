book_name = str(input())

checked_books = 0

while True:
    text = str(input())

    if text == "No More Books":
        print(f"""The book you search is not here!
        You checked {checked_books} books.""")
        break

    if text == book_name:
        print(f"You checked {checked_books} books and found it.")
        break

    checked_books += 1