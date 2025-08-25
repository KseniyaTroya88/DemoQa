import time
from pages.form_page import FormPage


def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('text')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)
    form_page.modal_dialog.click_force()
    form_page.btn_close_modal.click_force()


def test_login_form_simple(browser):
    form_page = FormPage(browser)
    form_page.visit()

    # Заполняем только основные поля
    form_page.first_name.send_keys('Борис')
    form_page.last_name.send_keys('Петров')
    form_page.user_email.send_keys('boris.petrov@example.com')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9876543210')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('Санкт-Петербург, Кирочная ул., 25')

    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)

    # Проверяем что модальное окно появилось
    assert form_page.modal_dialog.exist()

    def test_state_city(browser):
        form_page = FormPage(browser)
        form_page.visit()

        # Прокрутка и заполнение основных полей
        form_page.state.scroll_to_element()
        form_page.state.click_force()
        time.sleep(1)

        # Выбор штата и города через force click
        form_page.state_dropdown.click_force()
        time.sleep(1)
        form_page.city.click_force()
        form_page.city_dropdown.click_force()
        time.sleep(1)