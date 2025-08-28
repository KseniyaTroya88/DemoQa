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

        # Заголовки для сортировки
        self.first_name_header = WebElement(driver, '.rt-th:first-child')
        self.last_name_header = WebElement(driver, '.rt-th:nth-child(2)')
        self.age_header = WebElement(driver, '.rt-th:nth-child(3)')
        self.email_header = WebElement(driver, '.rt-th:nth-child(4)')
        self.salary_header = WebElement(driver, '.rt-th:nth-child(5)')
        self.department_header = WebElement(driver, '.rt-th:nth-child(6)')


        # с занятия 11:
        # # Варианты селекторов для кнопок удаления:
        # self.btn_delete_row = WebElement(driver, '#delete-record-undefined')
        #
        # # Варианты для блока "No rows found":
        # self.no_data = WebElement(driver, 'div.rt-noData')
        #
        # # Добавим альтернативный поиск по тексту (xpath)
        # self.no_data_text = WebElement(driver, '//*[contains(text(), "No rows found")]', 'xpath')