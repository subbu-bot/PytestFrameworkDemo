import pytest
from selenium import webdriver
import time


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    print("..........>>>>>>>>>>Setting up Chrome<<<<<<<<<<..........")
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()

    yield
    print("..........((((((((((Chrome Tear Down))))))))))..........")
    driver.quit()

@pytest.fixture(scope='class')
def init_firefox_driver(request):
    print("..........>>>>>>>>>>Setting up firefox<<<<<<<<<<..........")
    driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()

    yield
    print("..........((((((((((Firefox Tear Down))))))))))..........")
    driver.quit()

@pytest.fixture(scope='class')
def init_Edge_driver(request):
    print("..........>>>>>>>>>>Setting up Edge<<<<<<<<<<..........")
    driver = webdriver.Edge()
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()

    yield
    print("..........((((((((((Edge Tear Down))))))))))..........")
    driver.quit()


@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome:
    pass
class Test_Chrome_behavior(Base_Chrome):
    def test_bankTitle(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        assert self.driver.title == "ParaBank | Welcome | Online Banking"

    def test_currentURL(self):
        assert self.driver.current_url == "https://parabank.parasoft.com/parabank/index.htm"

@pytest.mark.usefixtures("init_firefox_driver")
class Base_Firefox:
    pass
class Test_Firefox_behavior(Base_Firefox):
    def test_bankTitle(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        assert self.driver.title == "ParaBank | Welcome | Online Banking"

    def test_currentURL(self):
        assert self.driver.current_url == "https://parabank.parasoft.com/parabank/index.htm"

@pytest.mark.usefixtures("init_Edge_driver")
class Base_Edge:
    pass
class Test_Edge_behavior(Base_Edge):
    def test_bankTitle(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        assert self.driver.title == "ParaBank | Welcome | Online Banking"

    def test_currentURL(self):
        assert self.driver.current_url == "https://parabank.parasoft.com/parabank/index.htm"

