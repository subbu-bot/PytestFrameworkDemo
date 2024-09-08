import time

import pytest
from Pages.Dashboard import Dashboard
from Pages.Basepage import BasePage
from Pages.Login import Login
from Tests.Basetest import Basetest
from Config.config import TestData


class TestDashboard(Basetest):

    @pytest.mark.fullregression
    def test_dashboard_title(self):
        self.login = Login(self.driver)
        dashboard = self.login.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = dashboard.Dashboard_title(TestData.DTITLE)
        time.sleep(2)
        assert title == TestData.DTITLE

    @pytest.mark.fullregression
    @pytest.mark.sanity
    def test_logoutlink(self):
        self.login = Login(self.driver)
        dashboard = self.login.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(2)
        is_visible = dashboard.is_logout_link_visible()
        assert is_visible

    @pytest.mark.fullregression
    def test_welcomeText(self):
        self.login = Login(self.driver)
        dashboard = self.login.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(2)
        is_visible = dashboard.is_welcome_text_visible()
        assert is_visible

    @pytest.mark.fullregression
    def test_HomepageButton(self):
        self.login = Login(self.driver)
        dashboard = self.login.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(2)
        is_visible = dashboard.is_HomeButton_visible()
        assert is_visible

#
# def HomeButton(self):
#     self.is_Visible(self.HOME_BUTTON)
