from components.navbar_form import NavbarForm
from components.auth_form import AuthForm
from pages.base import BasePage


class MainPage(BasePage):
    """
    Главная Страница
    """

    def __init__(self, driver):
        self.PATH = 'browse'
        self.auth_form = AuthForm(driver)
        super(MainPage, self).__init__(driver, self.auth_form.locators.root)
        self.navbar_form = NavbarForm(self.driver)

    def open_auth_popup(self):
        self.navbar_form.click_login_menu()
        self.navbar_form.click_login_button()

    def auth(self, email, password):
        self.auth_form.set_email(email)
        self.auth_form.set_password(password)
        self.auth_form.submit()

    def check_auth(self) -> bool:
        return self.navbar_form.check_auth_is_right()
