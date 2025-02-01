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
            books_found = []
            for i in range(len(books)):
                book_title = books[i]["title"]
                book_author = books[i]["author"]
                
                if title.lower() == book_title.lower():
                    books_found.append({book_title},{book_author})
    
            Library.library_options(key=True,username="jack")
        # elif author_or_title == "author":
        #     author = input("search by author: ")
        #     books_found=[]
        #     book

                    
        
        # elif author_or_title == "author":
        #     author = input("search for author: ")
        #     books_found = []
        #     for i in range(len(books)):
        #         book_author = books[i]["author"]
        #     if author.lower() == book_author.lower():
        #         books_found.append(book_author)
        #         print(f"books_found")
        # Library.library_options(key=True,username="jack")
                # book_title[i]["title"]["author"],book_title[i]["title"]["is_borrowed"]
                # if book_title.lower() == title.lower():
                #     books_found= []
                #     books_found.append(book_title[i]["title"])
                #     print(books_found)
                #     Library.library_options(key=True,username="jack")
                # elif title == "stop":
                #     Library.library_options(key=True,username="jack")