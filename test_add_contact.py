# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_add_contact_page()
    app.add_contact(Contact("John", "Doe", "City, random street, 1 building", "3417698", "+79342319032",
                "test@test.ru"))
    app.return_to_contacts_page()
    app.logout()
