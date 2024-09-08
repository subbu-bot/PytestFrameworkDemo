from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This class is the parent of all the classes"""
""" It contains General methods & utilities of all the pages """


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_Visible(self, by_locator):
        element = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 25).until(EC.title_is(title))
        return self.driver.title

