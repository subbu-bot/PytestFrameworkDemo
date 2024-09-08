import time

import pytest
from Pages.Login import Login
from Pages.Registration import Registration
from Tests.Basetest import Basetest
from Config.config import TestData
from faker import *

fake = Faker()

class TestRegistration(Basetest):

    def test_register_Link(self):
        self.loginPage = Login(self.driver)
        flag = self.loginPage.is_register_link_visible()
        assert flag

    @pytest.mark.fullregression
    @pytest.mark.sanity
    def test_registration(self):
        self.login = Login(self.driver)
        register = self.login.do_click_register()
        register.do_register(fake.first_name(),
                                 fake.last_name(),
                                 fake.address(),
                                 fake.city(),
                                 fake.state(),
                                 fake.zipcode(),
                                 fake.phone_number(),
                                 fake.ssn(),
                                 fake.user_name(),
                                 TestData.PASSWORD,
                                 TestData.PASSWORD)