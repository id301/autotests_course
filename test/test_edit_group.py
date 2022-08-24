__author__ = 'id301'

from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Not edited", header="Not edited", footer="Not edited"))
    app.group.edit_first(Group(name="Edited", header="Edited", footer="Edited"))