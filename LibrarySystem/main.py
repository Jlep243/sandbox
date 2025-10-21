import operations

def main():
    while True:
        option = input("|1.Login|2.Search|3.AddBook|4.Exit: ")
        option = option.lower()  
        match option:
            case "1"| "login":
                user_name = input("username: ")
                password = input("password: ")
            case "2"|"search": 
                book_name = input("book title: ")
                author = input("Author: ")
                date = input("Date: ")
                operations.search_book(book_name,author,date)
            case "3"|"addbook":
                operations.add_book() 
            case "4"|"exit":
                input("Shutting down.... \n press enter...")
                break


if __name__ == "__main__":
    main()
