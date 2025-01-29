from members import Members
from Library import Library
print("Please Login")
accounts = []

while True: 
    choice = input("Would you like to login or register? ")

    if choice == "login":
        username = input("username: ")
        password = input("password: ")
        Library.Library_options()
    elif choice == "register":
        username = input("create username: ")
        password = input("create password: ")
        registered = Members(username, password)
        accounts.append({"username" : registered.user, "password" : registered.password})
        print(f"welcome {registered.user}")
        print(accounts)