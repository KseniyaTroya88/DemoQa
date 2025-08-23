from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

# Проверка текста в подвале (футере):
def test_check_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    # Проверяем URL
    assert demo_qa_page.equal_url()

    # Проверяем текст футера
    actual_text = demo_qa_page.footer_text.get_text()
    expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    assert actual_text == expected_text

# Проверка текста после перехода на:
# 1. Страницу 'https://demoqa.com/' - переход на сайт
# 2. Страницу 'https://demoqa.com/elements' через кнопку - проверка работоспособности кнопки
# Проверка расположения текста (по центру) == 'Please select an item from left to start practice.'

def test_check_center_text_after_navigation(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    # a. Переходим на главную страницу
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()

    # b. Переходим на страницу Elements через кнопку
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()

    # c. Проверяем центровку текста
    actual_text = elements_page.center_text.get_text()
    expected_text = 'Please select an item from left to start practice.'
    assert actual_text == expected_text