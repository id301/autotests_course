# -*- coding: utf-8 -*-
from model.group import Group
#import unittest, time, re


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="dsfdfs", header="dfsdf", footer="dfdsfdf"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()