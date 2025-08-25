import time
from pages.form_page import FormPage

def test_login_form_validation(browser):
    form_page = FormPage(browser)
    form_page.visit()

    # Проверяем плейсхолдеры у полей
    assert form_page.first_name.get_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_attribute('placeholder') == 'name@example.com'

    # Проверяем атрибут pattern у email
    assert form_page.user_email.get_attribute('pattern') is not None

    # Пытаемся отправить пустую форму и проверяем валидацию
    form_page.btn_submit.click_force()
    time.sleep(1)

    # Проверяем наличие класса was-validated у формы через наш элемент
    assert 'was-validated' in form_page.user_form.get_attribute('class')