import time

from Config.config import TestData
from Pages.Basepage import BasePage
from Pages.Dashboard import Dashboard
from selenium.webdriver.common.by import By

class Registration(BasePage):

    """BY Locators"""
    # REGISTER_LINK = (By.XPATH, "//a[normalize-space()='Register']")
    FIRSTNAME = (By.ID, "customer.firstName")
    LASTNAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIPCODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.XPATH, "//input[@id='customer.phoneNumber']")
    SSN = (By.XPATH, "//input[@id='customer.ssn']")
    RUSERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.XPATH, "//input[@value='Register']")


    # Constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Page actions
    def is_register_link_visible(self):
        return self.is_Visible(self.REGISTER)

    def get_registration_page_title(self, title):
        return self.get_title()

    def do_register(self, first_name, last_name, address, city, state, zipcode, phone, ssn, rusername, password, cnpassword):
        self.do_send_keys(self.FIRSTNAME, first_name)
        self.do_send_keys(self.LASTNAME, last_name)
        self.do_send_keys(self.ADDRESS, address)
        self.do_send_keys(self.CITY, city)
        self.do_send_keys(self.STATE, state)
        self.do_send_keys(self.ZIPCODE, zipcode)
        self.do_send_keys(self.PHONE, phone)
        self.do_send_keys(self.SSN, ssn)
        self.do_send_keys(self.RUSERNAME, rusername)
        self.do_send_keys(self.PASSWORD, password)
        self.do_send_keys(self.CONFIRM_PASSWORD, cnpassword)
        self.do_click(self.REGISTER_BUTTON)
        time.sleep(4)
        return Dashboard(self.driver)



