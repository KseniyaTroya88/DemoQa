import time
import pytest
from pages.alerts import Alerts


def test_timer_alert(browser):
    """Тест для таймерного alert - задание №12"""
    alert_page = Alerts(browser)

    # Переходим на страницу
    alert_page.visit()
    time.sleep(2)

    # Проверяем наличие кнопки
    assert alert_page.timerAlertButton.exist()
    assert alert_page.timerAlertButton.get_text() == "Click me"

    # Кликаем и ждем alert
    alert_page.timerAlertButton.click()
    time.sleep(6)  # Ждем 5 секунд + запас

    # Проверяем и закрываем alert
    assert alert_page.alert() is not False
    alert_text = alert_page.alert().text
    assert "This alert appeared after 5 seconds" in alert_text
    alert_page.alert().accept()
    time.sleep(1)


def test_simple_alert(browser):
    """Тест для обычного alert"""
    alert_page = Alerts(browser)
    alert_page.visit()
    time.sleep(2)

    # Проверяем что alert'а нет
    assert not alert_page.alert()

    # Кликаем на кнопку
    alert_page.alertButton.click()
    time.sleep(2)

    # Проверяем что alert появился
    assert alert_page.alert() is not False
    alert_page.alert().accept()
    time.sleep(1)


def test_alert_text(browser):
    """Тест текста в alert"""
    alert_page = Alerts(browser)
    alert_page.visit()
    time.sleep(2)

    alert_page.alertButton.click()
    time.sleep(1)

    # Проверяем текст alert
    assert alert_page.alert().text == 'You clicked a button'

    # Закрываем alert
    alert_page.alert().accept()
    time.sleep(1)

    # Проверяем что alert закрылся
    assert not alert_page.alert()


def test_confirm_alert(browser):
    """Тест confirm alert"""
    alert_page = Alerts(browser)
    alert_page.visit()
    time.sleep(2)

    alert_page.confirmButton.click()
    time.sleep(2)

    # Отменяем alert
    alert_page.alert().dismiss()
    time.sleep(1)

    # Проверяем результат отмены
    assert alert_page.confirmResult.get_text() == 'You selected Cancel'


def test_prompt_alert(browser):
    """Тест prompt alert"""
    alert_page = Alerts(browser)
    name = 'Kseniya'

    alert_page.visit()
    time.sleep(2)

    alert_page.promptButton.click()
    time.sleep(2)

    # Вводим текст и подтверждаем
    alert_page.alert().send_keys(name)
    alert_page.alert().accept()
    time.sleep(1)

    # Проверяем результат
    assert alert_page.promptResult.get_text() == f'You entered {name}'


def test_alert_sequence(browser):
    """Тест последовательности alert'ов"""
    alert_page = Alerts(browser)
    alert_page.visit()
    time.sleep(2)

    # Последовательно тестируем все кнопки
    alert_page.alertButton.click()
    time.sleep(1)
    alert_page.alert().accept()

    alert_page.confirmButton.click()
    time.sleep(1)
    alert_page.alert().dismiss()

    alert_page.promptButton.click()
    time.sleep(1)
    alert_page.alert().send_keys('Test')
    alert_page.alert().accept()

    # Проверяем что все отработало
    assert alert_page.confirmResult.exist()
    assert alert_page.promptResult.exist()