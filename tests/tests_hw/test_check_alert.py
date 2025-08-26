import time
import pytest
from pages.alerts import Alerts


def test_timer_alert(browser):
    """Тест для таймерного alert"""
    alert_page = Alerts(browser)

    alert_page.visit()
    time.sleep(2)

    # Проверяем наличие кнопки
    assert alert_page.timer_alert_button.exist()

    # Кликаем и ждем alert
    alert_page.timer_alert_button.click()
    time.sleep(6)  # Ждем 5 секунд + 1 секунда запаса

    # Проверяем и закрываем alert
    assert alert_page.alert()
    alert_text = alert_page.alert().text
    assert "This alert appeared after 5 seconds" in alert_text
    alert_page.alert().accept()