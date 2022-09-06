__author__ = 'id301'

import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list_v2()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_number == contact_from_edit_page.home_number
    assert contact_from_view_page.phone_number == contact_from_edit_page.phone_number
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_number, contact.phone_number, contact.work_phone,
                                        contact.secondary_phone]))))