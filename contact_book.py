class Contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email

class ContactBook:
    def __init__(self):
        self.contacts=[]


    def add_contact(self,name,phone,email):
        if not phone.isdigit():
            raise ValueError(f"{phone} is an invalid number. ")
        if "@" not in email:
            raise ValueError(f"Invalid email.")


        contact=Contact(name,phone,email)
        self.contacts.append(contact)

    def search_contact(self,name):
        # print(self.contacts)
        for contact in self.contacts:
            if contact.name==name:
                # print(f"{name} :  -{contact.phone}   -{contact.email}")
                return contact
        raise ValueError(f"{name} was not found.")

        
    def update_contact(self,name,phone,email):
        for contact in self.contacts:
            if contact.name==name:
             
                contact.phone=phone
                contact.email=email
                print(f"Contact updated successfully.")
                return 
        raise ValueError(f"{name} was not found.")

        
    def delete_contact(self,name):
        for contact in self.contacts:
            if  contact.name==name:
                self.contacts.remove(contact)
                print(f"Contact deleted successfully.")
                return
        raise ValueError(f"{name} was not found ")   
             
        

    def show_all(self):
        print(f"ALL THE CONTACTS IN THE LIST: \n")
        for contact in self.contacts:
             print(f"{contact.name} :  -{contact.phone}   -{contact.email} ")


        
    def save_contacts(self):
        with open("contacts.txt","w+") as f:
            for contact in self.contacts:
                f.write(f"{contact.name} :  -{contact.phone}   -{contact.email} ")

        print(f"Contacts saved successfully.")

    def load_contacts(self):
        print(f"ALL THE CONTACTS IN THE LIST: \n")
        with open("contacts.txt","r") as f:
            
                info =f.readlines()
                for i in info:
                    print(f"{i}")

       
        

cb = ContactBook()
try:

    cb.add_contact("Ravi", "9876543210", "ravi@gmail.com")
    cb.add_contact("Priya", "1234567890", "priya@gmail.com")
    cb.add_contact("Logan", "abcd", "logangmail.com")  # should fail — invalid phone and email
    # cb.add_contact("Logan", "121889277", "logangmail.com")  # should fail — invalid phone and email
except ValueError as e:
    print(f"Error : {e}")
try:

    cb.search_contact("Ravi")
    cb.search_contact("Gauri")
    
except ValueError as e:
    print(f"Error : {e}")

cb.update_contact("Priya", "9999999999", "new@gmail.com")

try:

    cb.delete_contact("Ravi")
    cb.delete_contact("Ghost")  # should fail
   
    
except ValueError as e:
    print(f"Error : {e}")
cb.show_all()
contact=cb.search_contact("Ravi")
cb.save_contacts()
cb.load_contacts()
cb.show_all()