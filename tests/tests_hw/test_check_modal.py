import time
import pytest
from pages.modal_dialogs import ModalDialogs

def test_modal_dialogs(browser):
    """Тест для модальных окон"""
    modal_page = ModalDialogs(browser)

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
    modal_page.close_small_modal.click()
    time.sleep(1)

    # Large modal
    modal_page.large_modal_button.click()
    time.sleep(1)
    assert modal_page.modal_content.exist()
    modal_page.close_large_modal.click()
    time.sleep(1)