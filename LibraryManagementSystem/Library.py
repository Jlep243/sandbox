books = [
    {"title": "1984", "author": "Jane Austen", "is_borrowed": False},
    {"title": "Foundation", "author": "Jane Austen", "is_borrowed": False},
    {"title": "1984", "author": "George Orwell", "is_borrowed": False},
    {"title": "Pride and Prejudice", "author": "Agatha Christie", "is_borrowed": False},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "is_borrowed": False},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "is_borrowed": False},
    {"title": "Murder on the Orient Express", "author": "J.K. Rowling", "is_borrowed": False},
    {"title": "1984", "author": "Jane Austen", "is_borrowed": False},
    {"title": "Foundation", "author": "J.R.R. Tolkien", "is_borrowed": False},
    {"title": "The Hobbit", "author": "Isaac Asimov", "is_borrowed": False}
]



class Library:
    def library_options(key,username):
        print(f"welcome to the library")
        options = input("1.Search for book, 2.Put book on hold, 3.Borrow book, 4.Return book: ")
        if options == "1":
            author_or_title = input("would you like to search by author or title?")
            search_for_book(author_or_title)
        # elif options == "2":
            
        # elif options == "3":

    # def search_for_book(author_or_title):
    #     for i in range(len(books)):
    

