__author__ = 'id301'

import random

from model.contact import Contact
import random

def test_edit_first_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.add(Contact("John", "Doe", "City, random street, 1 building", "3417698", "+79342319032",
                                "test@test.ru"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact("Edited name", "Edited surname", "Edited City, random street, 1 building", "000000", "+79999999999",
                "edited@test.ru")
    new_contact.id = contact.id
    app.contact.edit_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact)] = new_contact
    assert sorted(old_contacts, key=Contact.get_id) == sorted(new_contacts, key=Contact.get_id)
    if check_ui:
        assert sorted(new_contacts, key=Contact.get_id) == sorted(app.contact.get_contact_list_v2(), key=Contact.get_id)
