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
    contact, group = random_add_contact_to_group(app, db)
    assert contact in orm.get_contacts_in_group(group)

def random_add_contact_to_group(app, db):
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    app.contact.choose_contact(contact.id)
    groups = db.get_group_list()
    group = random.choice(groups)
    app.contact.add_to_group(group.id)
    return contact, group
