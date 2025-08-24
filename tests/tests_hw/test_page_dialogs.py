import time
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):

    modal_page = ModalDialogs(browser)
    modal_page.visit()
    assert modal_page.all_buttons.check_count_elements(5)


def test_navigation_modal(browser):

    modal_page = ModalDialogs(browser)
    modal_page.visit()

    browser.refresh()
    time.sleep(1)

    modal_page.icon.click()
    time.sleep(2)

    browser.back()
    time.sleep(2)

    browser.set_window_size(900, 400)
    time.sleep(1)

    browser.forward()
    time.sleep(2)

    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'

    browser.set_window_size(1000, 1000)
    time.sleep(1)