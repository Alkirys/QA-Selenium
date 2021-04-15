from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent


class FilterLocators:
    def __init__(self):
        self.root = '//div[@class="content__info-block-wrapper"]'
        self.genres_button = '//button[@class="genres-btn"]'
        self.genres_refs = '//div[@class="sub-menu__list"]/a'


class Filter(BaseComponent):
    def __init__(self, driver):
        super(Filter, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = FilterLocators()

    def click_genres_button(self):
        """
        Нажимает на кнопку "Фильтр"
        """
        films = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.genres_button))
        )
        films.click()

    def get_genres_refs(self):
        """
        Получает элементы всех жанров
        """
        genres = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.genres_refs))
        )
        return genres

    def click_genre(self, genre):
        """
        Нажимает на один из жанров
        """
        genre.click()

