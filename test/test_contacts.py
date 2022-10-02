__author__ = 'id301'

import re
from random import randrange
from model.contact import Contact

# def test_contacts_on_homepage_and_editpage(app):
#     contacts_from_homepage = app.contact.get_contact_list_v2()
#     index = randrange(len(contacts_from_homepage))
#     contact_from_homepage = contacts_from_homepage[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#
#     assert contact_from_homepage.lastname == contact_from_edit_page.lastname
#     assert contact_from_homepage.firstname == contact_from_edit_page.firstname
#     assert contact_from_homepage.address == contact_from_edit_page.address
#     assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_edit_page)
#     assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)

def test_contacts_on_homepage_and_db(app, db):
    contacts_from_homepage = sorted(app.contact.get_contact_list_v2(), key=Contact.get_id)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.get_id)

    for index in range(len(contacts_from_homepage)):
        assert contacts_from_homepage[index].lastname == contacts_from_db[index].lastname
        assert contacts_from_homepage[index].firstname == contacts_from_db[index].firstname
        assert contacts_from_homepage[index].address == del_double_space(contacts_from_db[index].address).strip()
        assert contacts_from_homepage[index].all_emails_from_homepage == merge_emails_like_on_home_page(contacts_from_db[index])
        assert contacts_from_homepage[index].all_phones_from_homepage == merge_phones_like_on_home_page(contacts_from_db[index])

def clear(s):
    return re.sub("[() -]", "", s)

def del_double_space(s):
    return s.replace('  ', ' ')

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_number, contact.phone_number, contact.work_phone,
                                        contact.secondary_phone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3])))