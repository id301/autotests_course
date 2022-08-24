__author__ = 'id301'

from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact("John", "Doe", "City, random street, 1 building", "3417698", "+79342319032",
                                "test@test.ru"))
    app.contact.edit_first(Contact("Edited name", "Edited surname", "Edited City, random street, 1 building", "000000", "+79999999999",
                "edited@test.ru"))
