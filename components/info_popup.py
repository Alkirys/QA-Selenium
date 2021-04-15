from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent


class InfoPopupLocators:
    def __init__(self):
        self.popup = '//div[@class="content-popup"]'


class InfoPopup(BaseComponent):
    def __init__(self, driver):
        super(InfoPopup, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = InfoPopupLocators()
    
    def check_appearance(self) -> bool:
        """
        Ождиает пока не откроется информационный попап
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.popup)))
        return element.text
