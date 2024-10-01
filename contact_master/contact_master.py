class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def _str_(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactMaster:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact added: {new_contact}")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact deleted: {name}")
                return
        print(f"Contact not found: {name}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"Contact found: {contact}")
                return contact
        print(f"Contact not found: {name}")
        return None

    def list_contacts(self):
        if self.contacts:
            print("Listing all contacts:")
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts available.")

def main():
    contact_manager = ContactMaster()
    
    while True:
        print("\nContact Master Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. List Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_manager.add_contact(name, phone, email)
        
        elif choice == '2':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
        
        elif choice == '3':
            name = input("Enter the name of the contact to search: ")
            contact_manager.search_contact(name)
        
        elif choice == '4':
            contact_manager.list_contacts()
        
        elif choice == '5':
            print("Exiting Contact Master...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()