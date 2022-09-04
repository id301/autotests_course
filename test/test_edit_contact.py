__author__ = 'id301'

from model.contact import Contact
from random import randrange

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact("John", "Doe", "City, random street, 1 building", "3417698", "+79342319032",
                                "test@test.ru"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact("Edited name", "Edited surname", "Edited City, random street, 1 building", "000000", "+79999999999",
                "edited@test.ru")
    contact.id = old_contacts[index].id
    app.contact.edit_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.get_id) == sorted(new_contacts, key=Contact.get_id)
