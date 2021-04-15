from components.popup_film import PopupFilm
from components.infoblock_film import InfoblockFilm
from pages.base import BasePage


class SerialPage(BasePage):
    """
    Страница сериала
    """

    def __init__(self, driver):
        self.PATH = 'serials'
        self.popup_film = PopupFilm(driver)
        super(SerialPage, self).__init__(driver, self.popup_film.locators.root)
        self.infoblock_film = InfoblockFilm(self.driver)

    def open_popup(self):
        self.popup_film.open_popup()

    def click_season_button(self) -> bool:
        return self.popup_film.click_season_if_exist()

    def check_season_changed(self) -> bool:
        return self.popup_film.check_season_changed()

    def click_serial_episode(self) -> bool:
        return self.popup_film.click_episode()

    def check_player_is_open(self) -> bool:
        return self.popup_film.check_player_is_open()

    def open_infoblock(self):
        self.infoblock_film.open_infoblock()

    def click_infoblock_details(self):
        self.infoblock_film.click_infoblock_tab_button("Детали")

    def check_infoblock_details_open(self) -> bool:
        return self.infoblock_film.check_details_clicked()

    def click_infoblock_seasons(self):
        self.infoblock_film.click_infoblock_tab_button("Сезоны")

    def check_infoblock_seasons_open(self) -> bool:
        return self.infoblock_film.check_seasons_clicked()

    def click_infoblock_season_button(self):
        self.infoblock_film.click_season_button()

    def check_episodes_open(self) -> bool:
        return self.infoblock_film.check_episodes_open()

    def click_episode(self):
        self.infoblock_film.click_episode()

    def check_player_open(self) -> bool:
        return self.infoblock_film.check_player_open()

    def close_infoblock(self):
        self.infoblock_film.click_close_button()

    def check_infoblock_close(self) -> bool:
        return self.infoblock_film.check_infoblock_closed()