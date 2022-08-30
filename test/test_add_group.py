# -*- coding: utf-8 -*-
from model.group import Group
#import unittest, time, re


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="dsfdfs", header="dfsdf", footer="dfdsfdf"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)