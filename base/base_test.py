import pytest

from config.data import Data
from pages.login import LoginPage
from pages.dashboard import DashboardPage
from pages.personal_page import PersonalPage


class BaseTest:

    data: Data

    login: LoginPage
    dashboard: DashboardPage
    personal_page: PersonalPage


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login = LoginPage(driver)
        request.cls.dashboard = DashboardPage(driver)
        request.cls.personal_page = PersonalPage(driver)

