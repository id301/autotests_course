__author__ = 'id301'

class ContactHelper:

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

    def edit_first(self, contact):
        wd = self.app.wd
        self.open_contactlist_page()
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill fields
        self.fill_contact_fields(contact)
        # save
        wd.find_element_by_name("update").click()
        self.open_contactlist_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_contactlist_page()
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_contactlist_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))