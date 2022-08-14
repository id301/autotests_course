# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest
#import unittest, time, re



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="dsfdfs", header="dfsdf", footer="dfdsfdf"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

if __name__ == "__main__":
    unittest.main()