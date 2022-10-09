__author__ = 'id301'

from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, db, orm):
    #Precond - check if at least one contact and at least one group exists
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact("John", "Doe", "City, random street, 1 building", "3417698", "+79342319032",
                                "test@test.ru"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    #Test itself
    contact, group = add_new_contact_to_group(app, db, orm)
    assert contact in orm.get_contacts_in_group(group)

def add_new_contact_to_group(app, db, orm):
    groups = db.get_group_list()
    group = None
    contact = None
    pair_found = False
    while not pair_found:
        group = random.choice(groups)
        contacts = orm.get_contacts_not_in_group(group)
        if len(contacts) > 0:
            contact = random.choice(contacts)
            pair_found = True
    app.contact.choose_contact(contact.id)
    app.contact.add_to_group(group.id)
    return contact, group
