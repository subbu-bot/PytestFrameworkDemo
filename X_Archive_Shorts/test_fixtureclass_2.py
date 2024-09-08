import pytest
from selenium import webdriver
import time


@pytest.fixture(params =["Chrome", "Firefox", "Edge"], scope='class')
def init_driver(request):
    param = request.param.lower()
    print(f"..........>>>>>>>>>> Setting up {param.capitalize()} Browser <<<<<<<<<<..........")
    if request.param == "Chrome":
        driver = webdriver.Chrome()
    elif request.param == "Firefox":
        driver = webdriver.Firefox()
    elif request.param == "Edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {param}")

    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()

    yield
    print(f"..........(((((((((( {param.capitalize()} Tear Down ))))))))))..........")
    driver.quit()

@pytest.mark.usefixtures("init_driver")
class Basetest:
    pass

class Test_google(Basetest):
    def test_webapp(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        assert self.driver.title == "ParaBank | Welcome | Online Banking"

    def test_currentURL(self):
        assert self.driver.current_url == "https://parabank.parasoft.com/parabank/index.htm"