import pytest
from Pages.Login import Login
from Tests.Basetest import Basetest
from Config.config import TestData

class TestLogin(Basetest):

    @pytest.mark.fullregression
    @pytest.mark.sanity
    def test_register_Link(self):
        self.loginPage = Login(self.driver)
        flag = self.loginPage.is_register_link_visible()
        assert flag

    @pytest.mark.fullregression
    def test_page_Title(self):
        self.loginPage = Login(self.driver)
        title = self.loginPage.get_title(TestData.TITLE)

    @pytest.mark.fullregression
    @pytest.mark.sanity
    def test_Login(self):
        self.loginPage = Login(self.driver)
        self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
