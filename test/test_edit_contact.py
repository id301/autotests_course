__author__ = 'id301'

from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact("Edited name", "Edited surname", "Edited City, random street, 1 building", "000000", "+79999999999",
                "edited@test.ru"))
    app.session.logout()
