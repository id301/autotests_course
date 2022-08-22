# -*- coding: utf-8 -*-
from model.group import Group
#import unittest, time, re


def test_add_group(app):
    app.group.create(Group(name="dsfdfs", header="dfsdf", footer="dfdsfdf"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))