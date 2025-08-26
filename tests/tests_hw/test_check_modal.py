import time
import pytest
from selenium.common.exceptions import TimeoutException
from pages.modal_dialogs import ModalDialogs


def test_modal_dialogs(browser):
    """Тест для модальных окон"""
    modal_page = ModalDialogs(browser)

    # Проверяем доступность страницы
    try:
        modal_page.visit()
        time.sleep(2)
    except Exception:
        pytest.skip("Страница недоступна")

    # Small modal
    assert modal_page.small_modal_button.exist()
    modal_page.small_modal_button.click()
    time.sleep(1)
    assert modal_page.modal_content.exist()
    assert "Small Modal" in modal_page.modal_content.get_text()
    modal_page.close_small_modal.click()
    time.sleep(1)
    assert not modal_page.modal_content.exist()

    # Large modal
    modal_page.large_modal_button.click()
    time.sleep(1)
    assert modal_page.modal_content.exist()
    assert "Large Modal" in modal_page.modal_content.get_text()
    modal_page.close_large_modal.click()
    time.sleep(1)
    assert not modal_page.modal_content.exist()


# modal_dialogs.py
from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.small_modal_button = WebElement(driver, '#showSmallModal')
        self.large_modal_button = WebElement(driver, '#showLargeModal')
        self.modal_content = WebElement(driver, '.modal-content')
        self.close_small_modal = WebElement(driver, '#closeSmallModal')
        self.close_large_modal = WebElement(driver, '#closeLargeModal')