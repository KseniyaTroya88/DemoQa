import time
from pages.tables import Tables


def test_webtables_operations(browser):
    """Тестирование добавления, редактирования и удаления записей в таблице"""
    page = Tables(browser)
    page.visit()
    time.sleep(2)

    # Запоминаем начальное количество кнопок удаления (равно количеству записей)
    initial_delete_buttons = page.btn_delete.find_elements()
    initial_count = len(initial_delete_buttons)
    print(f"Начальное количество записей: {initial_count}")

    # a. Проверяем что есть кнопка Add
    assert page.btn_add.exist()

    # b. Открываем диалоговое окно
    page.btn_add.click()
    time.sleep(1)
    assert page.modal.exist()

    # c. Проверяем что нельзя сохранить пустую форму
    page.btn_submit.click()
    time.sleep(1)
    assert page.modal.exist()

    # d. Заполняем форму и сохраняем
    test_data = {
        'first_name': 'Роман',
        'last_name': 'Сергеев',
        'email': 'roman.sergeev@example.com',
        'age': '29',
        'salary': '75000',
        'department': 'Разработка'
    }

    page.first_name.send_keys(test_data['first_name'])
    page.last_name.send_keys(test_data['last_name'])
    page.email.send_keys(test_data['email'])
    page.age.send_keys(test_data['age'])
    page.salary.send_keys(test_data['salary'])
    page.department.send_keys(test_data['department'])

    page.btn_submit.click()
    time.sleep(2)

    # Проверяем что диалог закрылся
    assert not page.modal.exist()

    # Проверяем что добавилась одна запись (кнопка удаления)
    delete_buttons_after_add = page.btn_delete.find_elements()
    assert len(delete_buttons_after_add) == initial_count + 1, \
        f"Ожидалось {initial_count + 1} записей, но найдено {len(delete_buttons_after_add)}"

    # Проверяем что данные появились в таблице
    cells_text = [cell.text for cell in page.table_cells.find_elements()]
    assert any(test_data['first_name'] in text for text in cells_text)
    assert any(test_data['last_name'] in text for text in cells_text)

    # e. Редактируем запись (кликаем на последнюю кнопку редактирования)
    edit_buttons = page.btn_edit.find_elements()
    edit_buttons[-1].click()  # Кликаем на последнюю кнопку редактирования
    time.sleep(2)
    assert page.modal.exist()

    # f. Меняем имя и сохраняем
    new_first_name = 'Сергей'
    page.first_name.clear()
    page.first_name.send_keys(new_first_name)

    page.btn_submit.click()
    time.sleep(2)
    assert not page.modal.exist()

    # Проверяем что данные обновились
    cells_after_edit = [cell.text for cell in page.table_cells.find_elements()]
    assert any(new_first_name in text for text in cells_after_edit)
    assert not any(test_data['first_name'] in text for text in cells_after_edit)

    # g. Удаляем запись (кликаем на последнюю кнопку удаления)
    delete_buttons_before = page.btn_delete.find_elements()
    delete_buttons_before[-1].click()  # Кликаем на последнюю кнопку удаления
    time.sleep(2)

    # Проверяем что удалилась одна запись
    delete_buttons_after = page.btn_delete.find_elements()
    assert len(delete_buttons_after) == initial_count, \
        f"Ожидалось {initial_count} записей, но найдено {len(delete_buttons_after)}"

    # Проверяем что данные удалились
    cells_after_delete = [cell.text for cell in page.table_cells.find_elements()]
    assert not any(new_first_name in text for text in cells_after_delete)
    assert not any(test_data['last_name'] in text for text in cells_after_delete)