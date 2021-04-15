from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class AuthLocators:
    def __init__(self):
        self.root = '//div[@class="popup-container"]'
        self.email_field = '//input[@type="email"]'
        self.password_field = '//input[@type="password"]'
        self.submit_btn = '//button[@type="submit"]'


class AuthForm(BaseComponent):
    def __init__(self, driver):
        super(AuthForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = AuthLocators()

    def set_email(self, email: str):
        """
        Вводит логин в окне авторизации
        """
        user_email = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.email_field))
        )
        user_email.send_keys(email)

    def set_password(self, pwd: str):
        """
        Вводит пароль в окне авторизации
        """
        password = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.password_field))
        )
        password.send_keys(pwd)

    def submit(self):
        """
        Завершает авторизацию
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.submit_btn))
        )
        submit.click()
