books = [
    {"title": "1984", "author": "Jane Austen", "is_borrowed": False,"on_hold": False},
    {"title": "Foundation", "author": "Jane Austen", "is_borrowed": False,"on_hold": False},
    {"title": "1984", "author": "George Orwell", "is_borrowed": False,"on_hold": False},
    {"title": "Pride and Prejudice", "author": "Agatha Christie", "is_borrowed": False,"on_hold": False},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "is_borrowed": False,"on_hold": False},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "is_borrowed": False, "on_hold": False},
    {"title": "Murder on the Orient Express", "author": "J.K. Rowling", "is_borrowed": False, "on_hold": False},
    {"title": "1984", "author": "Jane Austen", "is_borrowed": False, "on_hold": False},
    {"title": "Foundation", "author": "J.R.R. Tolkien", "is_borrowed": False, "on_hold": False},
    {"title": "The Hobbit", "author": "Isaac Asimov", "is_borrowed": False, "on_hold": False}
]



class Library:
    def library_options(key,username):
        print(f"welcome to the library")
        options = input("1.Search for book, 2.Put book on hold, 3.Borrow book, 4.Return book, 5.List of Books: ")
        if options == "1":
            author_or_title = input("would you like to search by author or title? ")
            Library.search_for_book(author_or_title)

        # put books on hold
        elif options == "2":
            Library.put_on_hold()
        # borrow book
        # elif options == "3":
        
        # Return book 
        # elif options == "4"

        #shows list of books
        elif options == "5":
            Library.list_of_books()

    def search_for_book(author_or_title):
        if author_or_title == "title":
            title = input("search for title: ")
            print("\n")
            books_found = []
            a = 0
            for i in range(len(books)):
                book_title = books[i]["title"]
                book_author = books[i]["author"]
                if title.lower() == book_title.lower():
                    books_found.append(book_title)
                    books_found.append(book_author)
            for book in books_found:
                a += 1
                if a % 2 != 0:
                    print(f"Title:{book}")
                elif a % 2 == 0:
                    print(f"Author:{book} \n")
            Library.library_options(key=True,username="jack")

        elif author_or_title == "author":
            author = input("search by author: ")
            print("\n")
            books_found=[]
            a = 0
            for i in range(len(books)):
                book_title = books[i]["title"]
                book_author = books[i]["author"]
                if author.lower() == book_author.lower():
                    books_found.append(book_title)
                    books_found.append(book_author)
            for book in books_found:
                a += 1
                if a % 2 != 0:
                    print(f"Title:{book}")
                elif a % 2 == 0:
                    print(f"Author:{book} \n")
            Library.library_options(key=True,username="jack")
        
    def list_of_books():
        print("\n")
        for book in books:
            print(f"Title: {book["title"]}, Author: {book["author"]}, CheckedOut: {book["is_borrowed"]}")
        print("\n")
        Library.library_options(key=True,username="jack")

    def put_on_hold():
        print("\n")
        book = input("What book would you like to put on hold: ")
        author = input("Who is the author of the book: ")

        # author = input("who is the author: ")
        book_found = []
        print("\n")

        #This goes through the list of dictionaries of each book
        for title in books:
            
            if title['title'].lower() == book.lower() and title['author'].lower() == author:
                title['on_hold'] = False
                print(f"{title["title"]} by {title["author"]} is now on hold")
        print('\n')
        Library.library_options(key=True,username="jack")