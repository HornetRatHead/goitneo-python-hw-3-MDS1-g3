def parse_input(user_input):
    if not user_input.strip():
        raise ValueError("Input cannot be empty!")
    
    split_input = user_input.split()
    
    if not split_input:
        raise ValueError("Please enter a command.")
    
    cmd = split_input[0].strip().lower()
    args = split_input[1:]
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as e:
            return str(e)

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists. Use 'change' command to update."
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError("Contact not found.")

def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")
            
            elif command == "add":
                print(add_contact(args, contacts))

            elif command == "change":
                print(change_contact(args, contacts))
            
            elif command == "phone":
                print(show_phone(args, contacts))
            
            elif command == "all":
                print(show_all(contacts))
            
            else:
                print("Invalid command.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()