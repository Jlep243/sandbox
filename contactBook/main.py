from contacts import contacts
option =  input("1.Look up|2.view all contacts|3.Update contact|4.Add contact|5.Remove contact:")
if option == "1":
    #while True:
    lookupOption = input("Would you like to lookup by phone, email, address, or name: ")
    identifier = input(f"{lookupOption}: ")
    for contact in contacts:
        if contact[lookupOption] == identifier:
            print(contact)
		 
elif option== "2":
    for contact in contacts:
        print(f"\n{contact["name"]}|\n phone:{contact["phone"]}|\n email: {contact["email"]}")
if option == "3":
 	person = input("which contact would you like to update:")

#for contact in contacts:
#    print(contact["name"])
    

