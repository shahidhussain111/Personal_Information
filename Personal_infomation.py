contacts_file = "contacts.txt"

def load_contacts():
    contacts = {}
    try:
        with open(contacts_file, "r") as f:
            for line in f:
                name, age, address, phone, email = line.strip().split(";")
                contacts[name] = {
                    "age": age,
                    "address": address,
                    "phone": phone,
                    "email": email
                }
    except FileNotFoundError:
        pass
    return contacts
1
def save_contacts(contacts):
    with open(contacts_file, "w") as f:
        for name, info in contacts.items():
            f.write(f"Name:{name}; Age:{info['age']}; Address:{info['address']}; Phone:{info['phone']}; Email:{info['email']}\n")

def add_contact(contacts):
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists.")
        return
    age = input("Enter age: ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {
        "age": age,
        "address": address,
        "phone": phone,
        "email": email
    }
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Age: {info['age']}")
        print(f"Address: {info['address']}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")

def search_contact(contacts):
    name = input("Enter the name of the contact to search for: ")
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}")
        print(f"Age: {info['age']}")
        print(f"Address: {info['address']}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        age = input(f"Enter new age: ")
        address = input(f"Enter new address: ")
        phone = input(f"Enter new phone number: ")
        email = input(f"Enter new email: ")
        contacts[name] = {
            "age": age,
            "address": address,
            "phone": phone,
            "email": email
        }
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\nPersonal Information Management System")
        print("1. Add new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Save a contact")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            view_contacts(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            update_contact(contacts)
        elif choice == 5:
            delete_contact(contacts)
        elif choice == 6:
            save_contacts(contacts)
            print("Contacts saved.")
        elif choice==7:
            break
            
        else:
            print("Invalid choice. Please try again.")
main()
