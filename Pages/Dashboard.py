import pytest
from Config.config import TestData
from Pages.Basepage import BasePage
from selenium.webdriver.common.by import By


class Dashboard(BasePage):
    """Locators"""
    WELCOMETEXT = (By.XPATH, "//b[normalize-space()='Welcome']")
    LOGOUT_LINK = (By.XPATH, "//a[normalize-space()='Log Out']")
    HOME_BUTTON = (By.XPATH, "//a[normalize-space()='home']")
    DASHBOARD_URL = "https://parabank.parasoft.com/parabank/register.htm"

    def __init__(self, driver):
        super().__init__(driver)

    def Dashboard_title(self, title):
        return self.get_title(title)

    def is_logout_link_visible(self):
        return self.is_Visible(self.LOGOUT_LINK)

    def is_welcome_text_visible(self):
        return self.is_Visible(self.WELCOMETEXT)

    def is_HomeButton_visible(self):
        return self.is_Visible(self.HOME_BUTTON)
