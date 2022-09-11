from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", lastname="lastname1", address="address1", home_number="0000000", work_phone="2222222", phone_number="+79999999999",
            secondary_phone="4444444", email="mail1@test.ru", email2="mail1@test.com", email3="mail1@test.net"),
    Contact(firstname="firstname2", lastname="lastname2", address="address2", home_number="1111111", work_phone="3333333", phone_number="+78888888888",
            secondary_phone="4444444", email="mail2@test.ru", email2="mail2@test.com", email3="mail2@test.net")
]

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