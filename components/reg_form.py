from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent
from selenium.common.exceptions import TimeoutException


class RegLocators:
    def __init__(self):
        self.header = '//h1[@class="popup-container__heading"]'


class RegForm(BaseComponent):
    def __init__(self, driver):
        super(RegForm, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = RegLocators()
    
    def check_appearance(self) -> bool:
        """
        Ождиает пока не откроется попап регистрации
        """
        try:
            element = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, self.locators.header), "Регистрация"))
        except TimeoutException:
            return False
        return True
