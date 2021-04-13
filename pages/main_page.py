from components.navbar_form import NavbarForm
from components.auth_form import AuthForm
from components.preview import Preview
from components.info_popup import InfoPopup
from components.player import Player
from components.card import Card
from components.info_block import InfoBlock
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
        self.preview = Preview(self.driver)
        self.info_popup = InfoPopup(self.driver)
        self.player = Player(self.driver)
        self.card = Card(self.driver)
        self.info_block = InfoBlock(self.driver)

    def open_auth_popup(self):
        self.navbar_form.click_login_menu()
        self.navbar_form.click_login_button()

    def auth(self, email, password):
        self.auth_form.set_email(email)
        self.auth_form.set_password(password)
        self.auth_form.submit()
    
    def open_preview_info_popup(self):
        self.preview.click_info_button()
    
    def open_card_info_block_via_card_click(self):
        self.card.click()
    
    def open_card_info_block(self):
        self.card.click_info_block_btn()
    
    def open_card_player(self):
        self.card.click_player_btn()
    
    def move_to_card(self):
        self.card.move_to()
    
    def open_player(self):
        self.preview.click_play_button()
    
    def open_search_line(self):
        self.navbar_form.click_search_magnifier_to_open()
    
    def search_by_click(self):
        self.navbar_form.click_search_magnifier_to_search()
    
    def search_by_Enter(self):
        self.navbar_form.press_Enter_to_search()
    
    def input_text_into_search_line(self, text: str = 'a'):
        self.open_search_line()
        self.navbar_form.set_search_line_text(text)
    
    def choise_prompt(self):
        self.navbar_form.choise_prompt_label()

    def check_auth(self) -> bool:
        return self.navbar_form.check_auth_is_right()
    
    def check_info_popup_appearance(self) -> bool:
        return self.info_popup.check_appearance()
    
    def check_info_block_appearance(self) -> bool:
        return self.info_block.check_appearance()
    
    def check_player_appearance(self) -> bool:
        return self.player.check_appearance()
    
    def check_search_line_appearance(self) -> bool:
        return self.navbar_form.check_search_line_appearance()
    
    def check_search_line_disappearance(self) -> bool:
        return self.navbar_form.check_search_line_disappearance()
    
    def check_search_prompt_window_appearance(self) -> bool:
        return self.navbar_form.check_search_prompt_window_appearance()
