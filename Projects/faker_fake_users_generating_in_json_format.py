# This is a code for generating fake users and adding them in a database in format .json.
# C'est un code qui nous permet de genérer des utilisateurs inexistants et les ajouter dans une base de données en format .json.
import re
import string
from tinydb import TinyDB, where
from pathlib import Path

class User:

    DB = TinyDB(Path(__file__).resolve().parent / "database.json", indent= 3)
    def __init__(self, first_name: str, last_name: str, phone_number: str="", address: str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        return f'User({self.fullname})'

    def __str__(self):
        return f'{self.fullname}\n{self.phone_number}\n{self.address}'

    @property
    def db_instance(self):
        return User.DB.get((where("first_name") == self.first_name) & (where("last_name") == self.last_name))

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def _checks(self):
        self._check_phone_numbers()
        self._check_names()

    def _check_phone_numbers(self):
        phone_digits = re.sub(r'([+()\s]*)', "", self.phone_number)

        if len(phone_digits) < 10 or not phone_digits.isdigit():
            raise ValueError("The phone number is not valid!")

    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("You should insert first and last name!")

        symbols_to_avoid = string.punctuation + string.digits

        for character in self.first_name + self.last_name:
            if character in symbols_to_avoid:
                raise ValueError("There are invalid symbols in the name!")

    def exists(self):
        if self.db_instance:
            return True

    def delete(self):
        if self.exists():
            return User.DB.remove(doc_ids= [self.db_instance.doc_id])
        else:
            return 'The user doesn\'t exists'

    def save(self, validate_data: False):
        if validate_data:
            self._checks()

        return User.DB.insert(self.__dict__)

def get_all_users():
    return [User(**user) for user in User.DB.all()]

if __name__ == "__main__":
    from faker import Faker                            #==> This is the code that i user to generate the fake users
    fake = Faker(locale= "fr_FR")

    for _ in range(10):
        user = User(first_name= fake.first_name(),
                    last_name= fake.last_name(),
                    phone_number= fake.phone_number(),
                    address= fake.address())
        print(user.save(validate_data=True))
        print("-" * 20)