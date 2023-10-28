def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "confirm_overwrite", name, phone
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def confirm_and_update(name, phone, contacts):
    user_choice = input(f"Contact {name} already exists with phone number {contacts[name]}. Do you want to overwrite it? (yes = 1/ no = ANY): ").strip().lower()
    if user_choice == "1":
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Operation cancelled."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            response = add_contact(args, contacts)
            if isinstance(response, tuple) and response[0] == "confirm_overwrite":
                _, name, phone = response
                print(confirm_and_update(name, phone, contacts))
            else:
                print(response)

        elif command == "change":
            print(change_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))
            
        elif command == "all":
            print(show_all(contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()