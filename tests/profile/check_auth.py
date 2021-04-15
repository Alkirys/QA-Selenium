import unittest
import time

from pages.main_page import MainPage
from setup.default_setup import default_setup


class CheckAuth(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.page = MainPage(self.driver)
        self.page.open()

    def test_check_auth(self):
        self.page.open_auth_popup()
        self.page.auth(self.EMAIL, self.PASSWORD)
        is_all_right = self.page.check_auth()
        self.assertTrue(is_all_right)

    def tearDown(self):
        self.driver.quit()
