contacts = [{"name":"karl","email":"forKarl@gmail.com","address":"copenhagen,Denmark","phone":"929-3421"},
            {"name":"shamwow","email":"shammyWow@yahoo.com","address":"shamwow,street","phone":"902-0921"},
            {"name": "Alice Johnson", "phone": "555-1234", "email": "alice@example.com","address": ""},
            {"name": "Bob Smi", "phone": "555-5678", "email": "bob@example.com","address": " "},
            {"name": "Charlie Brown", "phone": "555-8765", "email": "charlie@example.com", "address": " "},
            {"name": "Dana White", "phone": "555-4321", "email": "dana@example.com", "address": " " },
            {"name": "Eve Adams", "phone": "555-6789", "email": "eve@example.com", "address": " "}]


class Contact:
	
	def __init__(self,name,phone,email,address):
	    self.name = name
	    self.phone = phone
	    self.email = email
	    self.address = address
	    contacts.append({"name":self.name,"phone":self.phone,"email":self.email,"address":self.address})
	    print(f"{self.name} has been added to contacts")

Contact('pepe','678-291-5423','pepe@gmail.com','1543 East 450 South')	
