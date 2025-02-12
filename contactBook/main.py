from contacts import contacts

option =  input("1.Look up|2.view all contacts|3.Update contact|4.Add contact|5.Remove contact:")
if option == "1":
    print("hello world")
elif option == "2":
    for contact in contacts:
        print(f"\n{contact["name"]}|\n phone:{contact["phone"]}|\n email: {contact["email"]}")

