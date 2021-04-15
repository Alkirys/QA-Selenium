from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent


class PlayerLocators:
    def __init__(self):
        self.watch_page = '//div[@class="watch__page"]'


class Player(BaseComponent):
    def __init__(self, driver):
        super(Player, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = PlayerLocators()
    
    def check_appearance(self) -> bool:
        """
        Ождиает пока не откроется страница просмотра
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.watch_page)))
        return element.text
