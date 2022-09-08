__author__ = 'id301'

import re
from random import randrange

def test_contacts_on_homepage(app):
    contacts_from_homepage = app.contact.get_contact_list_v2()
    index = randrange(len(contacts_from_homepage))
    contact_from_homepage = contacts_from_homepage[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

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