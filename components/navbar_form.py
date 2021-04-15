from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent


class NavbarLocators:
    def __init__(self):
        self.login_menu_btn = '//img[@class="header__arrow"]'
        self.login_btn = '//*[contains(text(),"Вход")]'
        self.my_list_btn = '//a[@href="/mylist"]'


class NavbarForm(BaseComponent):
    def __init__(self, driver):
        super(NavbarForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = NavbarLocators()

    def click_login_menu(self):
        """
        Вызывает подменю для входа
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.login_menu_btn))
        )
        submit.click()

    def click_login_button(self):
        """
        Кликает на кнопку "Вход"
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.login_btn))
        )
        submit.click()

    def check_auth_is_right(self) -> bool:
        """
        Ождиает пока не откроется главная страница на которой будет вкладка "Мой список"
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.my_list_btn)))
        return element.text
