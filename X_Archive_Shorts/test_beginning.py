import pytest
from selenium import webdriver
import time

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

def tearDown(module):
    driver.quit()

def test_bankTitle():
    assert driver.title == "ParaBank | Welcome | Online Banking"

def test_currentURL():
    assert driver.current_url == "https://parabank.parasoft.com/parabank/index.htm"

