from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.phone_valid(value)

    def phone_valid(self, phone):
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError('Invalid phone number.')
        return True


class Birthday(Field):
    pass


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday

    def add_birthday(self, birthday):
        self.birthday = birthday

    def days_to_birthday(self, birthday: str):
        birthday_datetime = datetime.strptime(birthday, '%d %B %Y').date()
        current_year_birthday = datetime(datetime.now().year, birthday_datetime.month, birthday_datetime.day).date()
        if current_year_birthday.month >= datetime.now().month:
            difference = current_year_birthday - datetime.now().date()
            return f'Days left until birthday: {difference.days}'
        else:
            difference = datetime(current_year_birthday.year + 1, current_year_birthday.month, current_year_birthday.day).date() - datetime.now().date()
            return f'Days left until birthday: {difference.days}'

    def add_phone(self, phone):
        try:
            p = Phone(phone)    # created p which is an instance of class Phone
            if p.phone_valid(phone):
                self.phones.append(p)
        except ValueError as e:
            print(e)

    def edit_phone(self, old_phone, new_phone):
        phone_found = False
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                phone_found = True
                break
        if not phone_found:
            raise ValueError('Phone was not found.')

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def __str__(self):
        if not self.birthday:
            return 'Contact name: {:<10} Phones: {:<25} Birthday: {:<25} {}'.format(self.name.value, '; '.join(p.value for p in self.phones), 'No birthday details.', 'No birthday details.')
        else:
            return 'Contact name: {:<10} Phones: {:<25} Birthday: {:<25} {}'.format(self.name.value, '; '.join(p.value for p in self.phones), self.birthday, self.days_to_birthday(self.birthday))


class AddressBook(UserDict):
    def add_record(self, contact):
        self.data.update({contact.name.value: contact})

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print('Phone was not found.')

    def delete(self, name):
        try:
            if name in self.data:
                self.data.pop(name)
            else:
                raise KeyError
        except KeyError:
            print(f'"{name}" is not in the address book.')

    def iterator(self, n):
        if n > len(book.data):
            print(f'There are only {len(book.data)} records in Address Book.')
        counter = 0
        result = ''
        for _, record in self.data.items():
            result += f'{record}\n'
            counter += 1
            if counter == n:
                yield result
                result = ''
