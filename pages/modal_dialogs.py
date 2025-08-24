from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        # Элемент с не уникальным локатором для всех кнопок
        self.all_buttons = WebElement(driver, 'button')

        # Элемент иконки для навигации
        self.icon = WebElement(driver, 'header a')