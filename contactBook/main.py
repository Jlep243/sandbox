from contacts import contacts
from contacts import Contact

while True:
    option =  input("1.Look up|2.view all contacts|3.Update contact|4.Add contact|5.Remove contact|6.exit: ")

    if option == "1":
        lookupOption = input("Would you like to lookup by phone, email, address, or name: ")
        identifier = input(f"{lookupOption}: ")
        for contact in contacts:
            if contact[lookupOption] == identifier:
                print(f"\n name: {contact["name"]}| phone: {contact["phone"]}| email: {contact["email"]}| address: {contact["address"]}") 

    elif option== "2":
        for contact in contacts:
            print(f"\n{contact["name"]}|\n phone:{contact["phone"]}|\n email: {contact["email"]}")

    elif option == "3":
        person = input("which contact would you like to update: ")
        for contact in contacts:
            if contact["name"] == person:
                choice = input("what would you like to change? name|phone|email|address: ")
                contact[choice] = input(f"{choice}: ")
                 
    elif option == "4":
        name = input(" name: ")
        phone = input(" phone: ")
        email = input(" email: ")
        address = input(" address: ")
        Contact(name,phone,email,address)
    elif option.lower() == "exit":
        exit() 
