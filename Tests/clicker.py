import time
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver


# Extend WebElement class to add delays for interaction methods
class SlowWebElement(WebElement):
    def click(self):
        time.sleep(1)  # Introduce a delay before click
        super().click()

    def send_keys(self, *value):
        time.sleep(1)  # Introduce a delay before typing
        super().send_keys(*value)


def test_slow_execution():
    driver = webdriver.Chrome()

    # Replace regular elements with slow elements (for interaction)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    username = SlowWebElement(driver.find_element_by_name("username"))
    password = SlowWebElement(driver.find_element_by_name("password"))

    username.send_keys("user")
    password.send_keys("pass")
    driver.quit()
