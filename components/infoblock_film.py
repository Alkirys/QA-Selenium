from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from components.base_component import BaseComponent


class AuthLocators:
    def __init__(self):
        self.root = '//div[@class="content__info-block-wrapper"]'
        self.film_button = '//div[@class="content__slider-item"]/button'
        self.infoblock_wrapper = '//div[@class="info-block__main-wrapper"]'
        self.details_button = '//a[@class="tabs__list-item-text "]'
        self.details_block = '//div[@class="info-block__page-details info-block_page"]'
        self.seasons_block = '//div[@class="info-block__page-seasons info-block_page"]'
        self.season_button = '//button[@class="seasons-wrapper__button"]'
        self.episode_name = '//div[@class="episode-card__label"]'
        self.episode_button = '//div[@class="content__grid"]/div/button'
        self.close_button = '//button[@class="close-btn"]/img'
        self.infoblock_wrapper = '//div[@class="info-block__main-wrapper"]'
        self.add_my_list_button = '//button[@class="info-block__add-btn add-btn"]'
        # self.need_subscription_label = '//a[contains(@class, "misc-item")]'
        self.need_subscription_label = '//*[@class="modal__name margin"]/span/a'
        self.play_button = '//button[@class="modal__play-btn play-btn item__btn"]'
        self.film_buttons_list = '//*[@class="item__card"]'
        self.subscribe_button = '//*[contains(text(), "Оформить подписку")]'


class InfoblockFilm(BaseComponent):
    def __init__(self, driver):
        super(InfoblockFilm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = AuthLocators()
        self.player_url = ""

    def open_infoblock(self):
        """
        Открывает инфоблок
        """
        film = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.film_button))
        )
        film.click()

    def check_infoblock_open(self) -> bool:
        """
        Проверяет, изменилась ли картинка на кнопке Like после нажатия
        """
        return True

    def click_infoblock_tab_button(self, button_text):
        """
        Нажимает на кнопку Like
        """
        buttons = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.details_button))
        )
        for button in buttons:
            if button.text == button_text:
                button.click()
                break

    def check_details_clicked(self) -> bool:
        """
        Проверяет, изменилась ли картинка на кнопке Like после нажатия
        """
        details_block = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.locators.details_block))
        )
        return len(details_block) == 1

    def check_seasons_clicked(self) -> bool:
        """
        Проверяет, изменилась ли картинка на кнопке Like после нажатия
        """
        seasons_block = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.locators.seasons_block))
        )
        return len(seasons_block) == 1

    def click_season_button(self):
        """
        Нажимает на кнопку Like
        """
        button = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.season_button))
        )
        button.click()

    def check_episodes_open(self) -> bool:
        """
        Проверяет, изменилась ли картинка на кнопке Like после нажатия
        """
        episodes_names = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.locators.episode_name))
        )
        return len(episodes_names) > 0

    def click_episode(self):
        """
        Нажимает на кнопку Like
        """
        button = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.episode_button))
        )
        print(button)
        print(button.text)
        serial_id = button.get_attribute("data-id")
        serial_season = button.get_attribute("data-season")
        serial_episode = button.get_attribute("data-episode")
        self.player_url = 'https://www.flicksbox.ru/watch/' + serial_id + '?season=' + serial_season + '&episode=' + serial_episode
        button.click()

    def check_player_open(self) -> bool:
        """
        Проверяет, изменилась ли картинка на кнопке Like после нажатия
        """
        is_redirect = self.wait.until(
            lambda driver: self.player_url in driver.current_url
        )
        self.player_url = ""
        return is_redirect

    def click_close_button(self):
        """
        Нажимает на кнопку Like
        """
        button = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.close_button))
        )
        button.click()

    def check_infoblock_closed(self) -> bool:
        """
        Проверяет, изменилась ли картинка на кнопке Like после нажатия
        """
        is_closed = WebDriverWait(self.driver, 30, 0.1).until(
            EC.invisibility_of_element_located((By.XPATH, self.locators.infoblock_wrapper))
        )
        return is_closed

    def click_my_list_button(self) -> bool:
        """
        Нажимает на кнопку Like
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.add_my_list_button))
        )
        is_added = submit.get_attribute("data-status")
        submit.click()
        if is_added == "true":
            return False
        else:
            return True

    def get_films(self):
        """
        Нажимает на кнопку Like
        """
        films = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.film_buttons_list))
        )
        return films

    def click_film(self, film):
        """
        Нажимает на кнопку Like
        """
        film.click()

    def check_subscription_label(self):
        """
        Нажимает на кнопку Like
        """
        label = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.need_subscription_label))
        )
        # print(label)
        # print(label.text)
        # print(self.driver.execute_script("return document.getElementsByClassName('misc-item')[0].style.background-color"))
        return label.text == "ТРЕБУЕТСЯ ПОДПИСКА"

    def click_play_button(self):
        """
        Нажимает на кнопку Like
        """
        button = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.play_button))
        )
        button.click()

    def check_subscription_popup_open(self) -> bool:
        """
        Нажимает на кнопку Like
        """
        label = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.subscribe_button))
        )
        return label.text == "Оформить подписку"
