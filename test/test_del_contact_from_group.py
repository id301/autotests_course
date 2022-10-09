__author__ = 'id301'

from model.contact import Contact
from model.group import Group
import random

def test_del_contact_from_group(app, db, orm):
    # Precond - check if at least one contact, at least one group exists and at least one contact is in group
    contact, group = None, None
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact("John", "Doe", "City, random street, 1 building", "3417698", "+79342319032",
                                "test@test.ru"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_entities_from_address_in_groups()) == 0:
        #add contact to group
        contact, group = random_add_contact_to_group(app, db)
    contact, group = get_pair(db, orm)
    app.contact.del_from_group(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_group(group)

def get_pair(db, orm):
    groups = db.get_group_list()
    group = None
    contact = None
    pair_found = False
    while not pair_found:
        group = random.choice(groups)
        contacts = orm.get_contacts_in_group(group)
        if len(contacts) > 0:
            contact = random.choice(contacts)
            pair_found = True
    return contact, group

def random_add_contact_to_group(app, db):
    app.contact.open_contactlist_page()
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    app.contact.choose_contact(contact.id)
    groups = db.get_group_list()
    group = random.choice(groups)
    app.contact.add_to_group(group.id)
    return contact, group