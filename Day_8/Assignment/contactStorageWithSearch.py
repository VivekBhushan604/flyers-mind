contacts = {}

while True:
    name = input("Enter contact name (or 'done' to stop): ")

    if name.lower() == "done":
        break

    phone = input("Enter phone number: ")

    contacts[name] = phone

search_name = input("\nEnter name to search: ")

phone = contacts.get(search_name)

if phone:
    print(f"{search_name}: {phone}")
else:
    print("Contact not found.")