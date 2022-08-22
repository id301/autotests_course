# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.contact.add(Contact("John", "Doe", "City, random street, 1 building", "3417698", "+79342319032",
                "test@test.ru"))
