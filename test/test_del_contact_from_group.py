__author__ = 'id301'

from model.contact import Contact
from model.group import Group
import random
from test.test_add_contact_to_group import random_add_contact_to_group

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
    # Test itself
    if contact is None and group is None:
        binded_list = db.get_entities_from_address_in_groups()
        binded_pair = random.choice(binded_list)
        for c in db.get_contact_list():
            if c.id == binded_pair.contact_id:
                contact = c
        for g in db.get_group_list():
            if g.id == binded_pair.group_id:
                group = g
    app.contact.del_from_group(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_group(group)
