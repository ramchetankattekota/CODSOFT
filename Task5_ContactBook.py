contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")

            for name, details in contacts.items():
                print("\n-------------------")
                print("Name:", name)
                print("Phone:", details["Phone"])
                print("Email:", details["Email"])
                print("Address:", details["Address"])

    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print("\nContact Found:")
            print("Name:", name)
            print("Phone:", contacts[name]["Phone"])
            print("Email:", contacts[name]["Email"])
            print("Address:", contacts[name]["Address"])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to update: ")

        if name in contacts:
            contacts[name]["Phone"] = input("New Phone: ")
            contacts[name]["Email"] = input("New Email: ")
            contacts[name]["Address"] = input("New Address: ")

            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice!")
