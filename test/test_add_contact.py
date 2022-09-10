# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(prefix, len):
    symbols = string.digits
    return prefix +"".join([random.choice(symbols) for i in range(len)])

def random_email(postfix, len_name, len_domain):
    symbols = string.ascii_letters + string.digits
    return ("".join([random.choice(symbols) for i in range(random.randrange(len_name))]) +
    "@" + "".join([random.choice(symbols) for i in range(random.randrange(len_domain))]) + postfix)


testdata = [Contact(firstname="", lastname="", address="", home_number="", work_phone="", phone_number="",
                    secondary_phone="", email="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            address=random_string("Addr:", 20), home_number=random_phone("", 7), work_phone=random_phone("", 7),
            phone_number=random_phone("+7", 10), secondary_phone=random_phone("+7", 10), email=random_email(".ru", 10, 9),
            email2=random_email(".ru", 15, 6), email3=random_email(".com", 20, 10))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.get_id) == sorted(new_contacts, key=Contact.get_id)