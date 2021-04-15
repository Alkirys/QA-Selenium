from components.navbar_form import NavbarForm
from components.auth_form import AuthForm
from components.popup_film import PopupFilm
from components.infoblock_film import InfoblockFilm
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
        self.popup_film = PopupFilm(self.driver)
        self.infoblock_film = InfoblockFilm(self.driver)

    def open_auth_popup(self):
        self.navbar_form.click_login_menu()
        self.navbar_form.click_login_button()

    def auth(self, email, password):
        self.auth_form.set_email(email)
        self.auth_form.set_password(password)
        self.auth_form.submit()

    def check_auth(self) -> bool:
        return self.navbar_form.check_auth_is_right()

    def open_popup(self):
        self.popup_film.open_popup()

    def click_infoblock_like_button(self):
        self.popup_film.click_like_button()

    def check_infoblock_liked(self) -> bool:
        return self.popup_film.check_like_clicked()

    def click_infoblock_dislike_button(self):
        self.popup_film.click_dislike_button()

    def check_infoblock_disliked(self) -> bool:
        return self.popup_film.check_dislike_clicked()

    def click_genre(self):
        self.popup_film.click_genre_anchor()

    def check_genre_redirect(self) -> bool:
        return self.popup_film.check_genre_redirect()

    def click_actor(self):
        self.popup_film.click_actor_anchor()

    def check_actor_redirect(self) -> bool:
        return self.popup_film.check_actor_redirect()

    def click_director(self):
        self.popup_film.click_director_anchor()

    def check_director_redirect(self) -> bool:
        return self.popup_film.check_director_redirect()

    def is_same_films(self) -> bool:
        return self.popup_film.is_same_films()

    def click_same_film(self):
        self.popup_film.click_same_film()

    def check_same_film_popup_open(self) -> bool:
        return self.popup_film.check_same_film_name()
