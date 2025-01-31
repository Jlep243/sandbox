from Library import Library
from members import Members
accounts = [
            {"user":"jack","password":"222"},
            {"user": "john", "password": "333"}
            ]

print(accounts[0]["user"])

def login(username, password):
    for i in range(len(accounts)):
        if accounts[i]["user"] == username and accounts[i]["password"] == password:
            key = True
            Library.library_options(key,username)
            break
        else:
            print("This user does not exist")

while True: 
    choice = input("Would you like to login or register? ")

    if choice == "login":
        username = input("username: ")
        password = input("password: ")
        login(username,password)

    elif choice == "register":
        username = input("create username: ")
        password = input("create password: ")
        registered = Members(username, password)

        accounts.append({"username" : registered.user, "password" : registered.password})
        print(f"welcome {registered.user}, please login\n")