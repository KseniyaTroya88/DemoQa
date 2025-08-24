import time
from pages.accordion import Accordion

def test_visible_accordion(browser):

     # Переход на страницу:
    accordion_page = Accordion(browser)
    accordion_page.visit()

    # Проверка видимости элемента:
    assert accordion_page.section1_content.visible()

    # Клик на заголовок
    accordion_page.section1_heading.click()
    time.sleep(2)

    # Проверка элемента на НЕвидимость:
    assert not accordion_page.section1_content.visible()

def test_visible_accordion_default(browser):

    # Переход на страницу
    accordion_page = Accordion(browser)
    accordion_page.visit()

    # Проверка на то, что следующие элементы должны быть скрыты по умолчанию:
    assert not accordion_page.section2_content_p1.visible()
    assert not accordion_page.section2_content_p2.visible()
    assert not accordion_page.section3_content.visible()