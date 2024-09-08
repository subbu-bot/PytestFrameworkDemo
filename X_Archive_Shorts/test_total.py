import pytest
import conftest


# Commented
# def test_total_divby3(totalpoints):
#     assert totalpoints % 3 == 0
#
#
# def test_total_divby5(totalpoints):
#     assert totalpoints % 5 == 0
#
#
# def test_total_divby10(totalpoints):
#     assert totalpoints % 10 == 0

@pytest.mark.usefixtures("init_driver")
class Basetest:
    pass

class Test_google(Basetest):
    def test_webapp(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        assert self.driver.title == "ParaBank | Welcome | Online Banking"

    def test_currentURL(self):
        assert self.driver.current_url == "https://parabank.parasoft.com/parabank/index.htm"