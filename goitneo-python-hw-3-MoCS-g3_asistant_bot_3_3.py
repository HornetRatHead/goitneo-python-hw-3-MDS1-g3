import datetime
from collections import UserDict
import re
#import json

#Start class list

class Birthday:
    def __init__(self, date: str):
        self._date = None
        self.date = date

    @property
    def date(self):
        return self._date.strftime('%d.%m.%Y')

    @date.setter
    def date(self, value: str):
        if not re.match(r'^\d{2}.\d{2}.\d{4}$', value):
            raise ValueError("Incorrect date format, should be DD.MM.YYYY")
        self._date = datetime.strptime(value, '%d.%m.%Y')


class Phone:
    def __init__(self, number: str):
        self._number = None
        self.number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value: str):
        if not re.match(r'^\+?[\d\s\-]+$', value):
            raise ValueError("Incorrect phone number format")
        self._number = value


class Record:
    def __init__(self, name: str, phone: Phone, birthday: Birthday = None):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def add_birthday(self, date: str):
        self.birthday = Birthday(date)

    def change_phone(self, new_phone: str):
        self.phone = Phone(new_phone)

    def get_phone(self):
        return self.phone.number if self.phone else None

    def get_birthday(self):
        return self.birthday.date if self.birthday else None


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record: Record):
        self.records.append(record)

    def save_to_file(self, filename: str):
        pass  # Залишено пустим, оскільки функція збереження в файл не була надана

    def load_from_file(self, filename: str):
        pass  # Залишено пустим, оскільки функція завантаження з файлу не була надана

    def get_birthdays_per_week(self):
        result = []
        now = datetime.datetime.now()
        week_later = now + datetime.timedelta(days=7)

        for record in self.records:
            if record.birthday:
                birth_date = datetime.datetime.strptime(record.get_birthday(), '%d.%m.%Y').replace(year=now.year)
                if now <= birth_date <= week_later:
                    result.append(record.name)
        return result

    def find_record(self, name: str):
        for record in self.records:
            if record.name == name:
                return record


#End class list

def parse_input(user_input: str):
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]
    return command, args

def add_contact(args, book):
    name, phone = args
    if book.get_phone(name):
        return "confirm_overwrite", name, phone
    book.add(name, phone)
    return f"Added {name} with phone {phone}"

def confirm_and_update(name, phone, book):
    overwrite = input(f"{name} is already in contacts. Overwrite? (yes = 1/no = ANY) ")
    if overwrite.lower() == '1':
        book.change_phone(name, phone)
        return f"Updated {name}'s phone to {phone}"
    return f"{name}'s phone not changed"

def change_contact(args, book):
    name, phone = args
    if book.get_phone(name):
        book.change_phone(name, phone)
        return f"Updated {name}'s phone to {phone}"
    return f"{name} not found in contacts"

def show_phone(args, book):
    name = args[0]
    phone = book.get_phone(name)
    return f"{name}'s phone is {phone}" if phone else f"{name} not found"

def show_all(book):
    all_records = book.show_all()
    return '\n'.join([f"{name}: {phone}" for name, phone in all_records])

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input.lower())

        if not args and command in ["add", "change", "phone", "add-birthday", "show-birthday"]:
            print("Invalid command: missing arguments.")
            continue

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

        elif command == "add-birthday":
            name, date = args
            book.add_birthday(name, date)
            print(f"Added birthday for {name} on {date}")

        elif command == "show-birthday":
            name = args[0]
            birthday = book.show_birthday(name)
            if birthday:
                print(f"{name}'s birthday is on {birthday}")
            else:
                print(f"No birthday set for {name}")

        elif command == "birthdays":
            names = book.get_birthdays_per_week()
            print("Birthdays in the next week for:", ', '.join(names))

        else:
            print("Invalid command.")




if __name__ == "__main__":
    main()


