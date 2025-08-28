from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        # Специфичные элементы для работы с модальными окнами
        self.small_modal_button = WebElement(driver, '#showSmallModal')
        self.large_modal_button = WebElement(driver, '#showLargeModal')
        self.modal_content = WebElement(driver, '.modal-content')
        self.close_small_modal = WebElement(driver, '#closeSmallModal')
        self.close_large_modal = WebElement(driver, '#closeLargeModal')