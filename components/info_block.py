from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class InfoBlockLocators:
    def __init__(self):
        self.block = '//div[@class="content__info-block"]'


class InfoBlock(BaseComponent):
    def __init__(self, driver):
        super(InfoBlock, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = InfoBlockLocators()
        self.driver = driver
    
    def check_appearance(self) -> bool:
        """
        Ождиает пока не откроется информационный блок
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.block)))
        except TimeoutException:
            return False
        return True
