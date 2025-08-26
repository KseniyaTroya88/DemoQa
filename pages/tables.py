from components.components import WebElement
from pages.base_page import BasePage


class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables/'
        super().__init__(driver, self.base_url)

        # Основные элементы
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_delete = WebElement(driver, '[title="Delete"]')
        self.btn_edit = WebElement(driver, '[title="Edit"]')
        self.no_data = WebElement(driver, '.rt-noData')

        # Элементы модального окна
        self.modal = WebElement(driver, '.modal-content')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')

        # Элементы таблицы для проверки данных
        self.table_rows = WebElement(driver, '.rt-tr-group')
        self.table_cells = WebElement(driver, '.rt-td')

        # Для домашнего задания 12
        self.first_name_header = WebElement(driver, '.rt-th:-soup-contains("First Name")')
        self.last_name_header = WebElement(driver, '.rt-th:-soup-contains("Last Name")')
        self.age_header = WebElement(driver, '.rt-th:-soup-contains("Age")')
        self.email_header = WebElement(driver, '.rt-th:-soup-contains("Email")')
        self.salary_header = WebElement(driver, '.rt-th:-soup-contains("Salary")')
        self.department_header = WebElement(driver, '.rt-th:-soup-contains("Department")')

        def _get_data_rows(self):
            """Возвращает только строки с данными (исключает заголовки и пустые строки)"""
            all_rows = self.table_rows.find_elements()
            data_rows = []

            for row in all_rows:
                # Проверяем, что строка не пустая и не заголовок
                cells = row.find_elements_by_css_selector('.rt-td')
                if cells and cells[0].text.strip():  # Первая ячейка не пустая
                    data_rows.append(row)

            return data_rows


        # с занятия 11:
        # # Варианты селекторов для кнопок удаления:
        # self.btn_delete_row = WebElement(driver, '#delete-record-undefined')
        #
        # # Варианты для блока "No rows found":
        # self.no_data = WebElement(driver, 'div.rt-noData')
        #
        # # Добавим альтернативный поиск по тексту (xpath)
        # self.no_data_text = WebElement(driver, '//*[contains(text(), "No rows found")]', 'xpath')