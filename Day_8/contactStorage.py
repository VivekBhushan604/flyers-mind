contacts = {}

while True:
    name = input("Enter contact name (or 'done' to stop): ")

    if name.lower() == "done":
        break

    phone = input("Enter phone number: ")

    contacts[name] = phone

print("\nContacts:")
for name, phone in contacts.items():
    print(f"{name}: {phone}")