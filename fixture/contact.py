__author__ = 'id301'

from model.contact import Contact
import re

class ContactHelper:

    contact_cache = None

    def __init__(self, app):
        self.app = app

    def open_contactlist_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_id("MassCB")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        # add firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # add lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # add address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # add phone numbers
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_number)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("%s" % contact.phone_number)
        # add email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("%s" % contact.email)

    def add(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        # fill fields
        self.fill_contact_fields(contact)
        # save
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_contactlist_page()
        self.contact_cache = None

    def edit_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contactlist_page()
        # select first contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill fields
        self.fill_contact_fields(contact)
        # save
        wd.find_element_by_name("update").click()
        self.open_contactlist_page()
        self.contact_cache = None

    def edit_first(self, contact):
        self.edit_by_index(0, contact)

    def view_by_index(self, index):
        wd = self.app.wd
        self.open_contactlist_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contactlist_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contactlist_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_contactlist_page()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_contactlist_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []

            rows = wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr")[1:]
            xpath_left_part = "//table[@id='maintable']/tbody/tr["
            xpath_right_part_id = "]/td[1]/input"
            xpath_right_part_lastname = "]/td[2]"
            xpath_right_part_firstname = "]/td[3]"

            for row in range(len(rows)):
                row += 2
                id = wd.find_element_by_xpath(xpath_left_part + str(row) + xpath_right_part_id).get_attribute("id")
                lastname = wd.find_element_by_xpath(xpath_left_part + str(row) + xpath_right_part_lastname).text
                firstname = wd.find_element_by_xpath(xpath_left_part + str(row) + xpath_right_part_firstname).text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))

        return list(self.contact_cache)

    def get_contact_list_v2(self):
        wd = self.app.wd
        if self.contact_cache is None:
            self.open_contactlist_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                                                  all_phones_from_homepage=all_phones,
                                                  all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        phone_number = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id, home_number=home_number,
                       phone_number=phone_number, work_phone=work_phone, secondary_phone=secondary_phone,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H: (.*)", text).group(1)
        phone_number = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_number=home_number, phone_number=phone_number, work_phone=work_phone,
                       secondary_phone=secondary_phone)

