__author__ = 'id301'

from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, home_number=None, phone_number=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home_number = home_number
        self.phone_number = phone_number
        self.email = email
        self.id = id

    def __repr__(self):
        return f"{self.id}: {self.firstname} {self.lastname}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def get_id(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize