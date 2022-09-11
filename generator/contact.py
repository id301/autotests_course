# -*- coding: utf-8 -*-
import json
from model.contact import Contact
import random
import string
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))