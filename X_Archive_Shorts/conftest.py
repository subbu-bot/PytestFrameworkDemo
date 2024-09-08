import pytest
from selenium import webdriver


# Commented
# @pytest.fixture()
# def totalpoints():
#     points = 90
#     return points

@pytest.fixture(params=["Chrome", "Firefox", "Edge"], scope='class')
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
    driver.implicitly_wait(25)
    driver.delete_all_cookies()

    yield
    print(f"..........(((((((((( {param.capitalize()} Tear Down ))))))))))..........")
    driver.quit()
