import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import conftest

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHubSpot(BaseTest):

    @pytest.mark.parametrize(
        "username, password",
        [
            ("johndoe2","Password123!"),
            ("emilysmith9","EmSmith@2024")
         ]
    )

    def test_login(self,username,password):
        """
        This menthod is used to login to the Parabank site
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        self.driver.find_element(By.NAME,"username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='loginPanel']/form/div[3]/input").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[href='logout.htm']").click()





