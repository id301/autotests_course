__author__ = 'id301'

import pymysql
from model.group import Group
from model.contact import Contact
from model.group_contact_bind import GroupContactBind

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home_number, phone_number, work_phone, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                    home_number=home_number, phone_number=phone_number, work_phone=work_phone,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def get_entities_from_address_in_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, group_id from address_in_groups')
            for row in cursor:
                (id, group_id) = row
                list.append(GroupContactBind(contact_id=str(id), group_id=str(group_id)))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()