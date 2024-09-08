import pytest
from selenium import webdriver
import time

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("..........>>>>>>>>>>Setting up<<<<<<<<<<..........")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    yield
    print("..........((((((((((Tear Down))))))))))..........")
    driver.quit()


def test_bankTitle(init_driver):
    assert driver.title == "ParaBank | Welcome | Online Banking"


def test_currentURL(init_driver):
    assert driver.current_url == "https://parabank.parasoft.com/parabank/index.htm"


