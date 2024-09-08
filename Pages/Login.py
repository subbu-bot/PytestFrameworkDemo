import time

from Config.config import TestData
from Pages.Basepage import BasePage
from Pages.Dashboard import Dashboard
from selenium.webdriver.common.by import By

from Pages.Registration import Registration


class Login(BasePage):

    # BY Locators
    USERNAME = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN = (By.XPATH, "//input[@value='Log In']")
    REGISTER = (By.XPATH, "//a[normalize-space()='Register']")
    ACCOUNT = (By.CSS_SELECTOR, "div[id='leftPanel'] h9")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Page actions
    def get_login_page_title(self, title):
        return self.get_title()

    def is_register_link_visible(self):
        return self.is_Visible(self.REGISTER)

    def do_login(self,username,password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN)
        return Dashboard(self.driver)

    def do_click_register(self):
        self.do_click(self.REGISTER)
        time.sleep(4)
        return Registration(self.driver)


