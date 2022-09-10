__author__ = 'id301'

from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, home_number=None, phone_number=None,
                 work_phone=None, secondary_phone=None, email=None, email2=None, email3=None,
                 id=None, all_phones_from_homepage=None, all_emails_from_homepage=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home_number = home_number
        self.phone_number = phone_number
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_homepage = all_emails_from_homepage
        self.id = id

    def __repr__(self):
        return f"{self.id}:{self.firstname};{self.lastname};{self.address};{self.home_number};{self.phone_number};" \
               f"{self.work_phone};{self.secondary_phone};{self.email};{self.email2};{self.email3}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def get_id(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize