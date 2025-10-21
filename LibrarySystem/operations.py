def add_book():
    book_name = input("Name of book: ")
    author = input("Author: ")
    date = input("Date published: ")    
    with open("library_books.txt","a") as file:
        file.write(f"{book_name} | {author} | {date}")
    with open("library_books.txt", "r") as file:
        print("\n Book added")    
        print(f"{file.read()}")


def search_book(book_name,author,date):
    searching_for = ["{book_name} | {author} | {date} "]
    with open("library_books.txt", "r") as f:
        list_of_books = f.readlines()
    for book in range(len(list_of_books)):
        if list_of_books[book] == searching_for:
            print(f"Book found: list_of_books[book]") 
