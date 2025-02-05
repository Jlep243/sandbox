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
            author_or_title = input("would you like to search by author or title? ")
            Library.search_for_book(author_or_title)
        # elif options == "2":
            
        # elif options == "3":

    def search_for_book(author_or_title):
        if author_or_title == "title":
            title = input("search for title: ")
            print("   ")
            books_found = []
            a = 0
            b = 0
            for i in range(len(books)):
                book_title = books[i]["title"]
                book_author = books[i]["author"]
                if title.lower() == book_title.lower():
                    books_found.append(book_title)
                    books_found.append(book_author)
            for book in books_found:
                a += 1
                b += 1
                if a % 2 != 0:
                    print(f"Title:{book}")
                elif a % 2 == 0:
                    print(f"Author:{book} \n")
            Library.library_options(key=True,username="jack")

        elif author_or_title == "author":
            author = input("search by author: ")
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
        
        