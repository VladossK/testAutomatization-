from base.base_test import BaseTest
import random
import allure
import pytest



@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):


    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login.open()
        self.login.enter_login(self.data.LOGIN)
        self.login.enter_password(self.data.PASSWORD)
        self.login.click_submit_button()
        self.dashboard.is_opened()
        self.dashboard.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_name(f"Test {random.randint(1,100)}")
        self.personal_page.save_changes( )
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("Success")

