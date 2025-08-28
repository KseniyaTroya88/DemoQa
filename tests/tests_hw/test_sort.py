import time
import pytest
from pages.tables import Tables

def test_table_sorting(browser):
    """Тест сортировки таблицы"""
    table_page = Tables(browser)
    table_page.visit()
    time.sleep(2)

    # Заголовки столбцов для сортировки
    headers = [
        table_page.first_name_header,
        table_page.last_name_header,
        table_page.age_header,
        table_page.email_header,
        table_page.salary_header,
        table_page.department_header
    ]

    for header in headers:
        if header.exist():
            # Кликаем для сортировки
            header.click()
            time.sleep(1)

            # Проверяем наличие класса сортировки
            class_attribute = header.get_dom_attribute('class')
            assert 'sortable' in class_attribute or 'asc' in class_attribute or 'desc' in class_attribute