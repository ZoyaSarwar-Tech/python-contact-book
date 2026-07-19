contacts={}
def add_contact():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    contacts[name] = phone
    print(f"{name}: contact added successfully")
def view_contact():
    if not contacts:
        print("No contacts found")
        return
    print("---Contact List---")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
def search_contact():
    name = input("Enter your name: ")
    if name in contacts:
        print(f"Name:{name}- Phone No: {contacts[name]}")
    else:
        print("Name not found")
def delete_contact():
    name = input("Enter your name: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} contact deleted successfully")
    else:
        print("Name not found")
while True:
    print("====Contact Book====")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Thank you for contacting us!")
        break
    else:
        print("Invalid choice!Try again.")


