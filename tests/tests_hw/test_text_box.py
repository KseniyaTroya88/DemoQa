from pages.text_box import TextBox
import time

def test_text_box_submit(browser):
    text_box = TextBox(browser)
    text_box.visit()

    # Прокручиваем страницу чтобы кнопка была видимой
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Записываем текст в поля через переменные
    test_name = "Testus Pythonovichev"
    test_address = "Saint-Petersburg, Sadovaya str., 1"

    text_box.full_name.send_keys(test_name)
    text_box.current_address.send_keys(test_address)

    # Нажимаем на кнопку submit используя force click
    text_box.btn_submit.click_force()
    time.sleep(2)

    # Проверяем результат
    assert text_box.output_name.get_text() == f"Name:{test_name}"
    assert text_box.output_address.get_text() == f"Current Address :{test_address}"