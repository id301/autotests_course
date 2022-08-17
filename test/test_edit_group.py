__author__ = 'id301'

from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="Edited", header="Edited", footer="Edited"))
    app.session.logout()