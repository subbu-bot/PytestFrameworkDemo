import pytest
from selenium import webdriver
@pytest.mark.loginGiants
def test_login_OpenAI():
    driver = webdriver.Chrome()
    driver.get("https://openai.com/")
    driver.maximize_window()
    assert driver.title == "OpenAI"
    driver.quit()

def test_login_Google():
    driver = webdriver.Chrome()
    driver.get("https://google.com/")
    driver.maximize_window()
    assert driver.title == "OpenAI"
    driver.quit()

def test_login_Instagram():
    driver = webdriver.Chrome()
    driver.get("https://instagram.com/")
    driver.maximize_window()
    assert driver.title == "Instagram"
    driver.quit()

def test_login_Bank():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.maximize_window()
    assert driver.title == "ParaBank | Welcome | Online Banking"
    driver.quit()