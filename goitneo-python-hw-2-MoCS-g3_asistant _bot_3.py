from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Phone number must have 10 digits")
        self.value = value

    @staticmethod
    def validate(phone_number):
        return bool(re.match(r'^\d{10}$', phone_number))

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_obj = Phone(phone)
        if phone_obj in self.phones:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone, new_phone):
        old_phone_obj = Phone(old_phone)
        if old_phone_obj in self.phones:
            index = self.phones.index(old_phone_obj)
            self.phones[index] = Phone(new_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

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

@input_error
def add_record(args, book):
    name = args[0]
    record = Record(name)
    book.add_record(record)
    return "Record added."

@input_error
def find_record(args, book):
    name = args[0]руддщ
    record = book.find(name)
    if record:
        return str(record)
    else:
        raise KeyError("Record not found.")

@input_error
def delete_record(args, book):
    name = args[0]
    book.delete(name)
    return "Record deleted."

@input_error
def add_phone_to_record(args, book):
    name, phone = args
    record = book.find(name)
    if record:
        record.add_phone(phone)
        return f"Phone {phone} added to {name}."
    else:
        raise KeyError("Record not found.")

@input_error
def remove_phone_from_record(args, book):
    name, phone = args
    record = book.find(name)
    if record:
        record.remove_phone(phone)
        return f"Phone {phone} removed from {name}."
    else:
        raise KeyError("Record not found.")

@input_error
def edit_phone_in_record(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return f"Phone {old_phone} changed to {new_phone} in {name}."
    else:
        raise KeyError("Record not found.")

def main():
    contacts = {}
    book = AddressBook()
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
            elif command == "add_record":
                print(add_record(args, book))
            elif command == "find_record":
                print(find_record(args, book))
            elif command == "delete_record":
                print(delete_record(args, book))
            elif command == "add_phone":
                print(add_phone_to_record(args, book))
            elif command == "remove_phone":
                print(remove_phone_from_record(args, book))
            elif command == "edit_phone":
                print(edit_phone_in_record(args, book))
            else:
                print("Invalid command.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()