from components.components import WebElement
from pages.base_page import BasePage

class Alerts(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        # Проверьте эти селекторы!
        self.alertButton = WebElement(driver, '#alertButton')
        self.timerAlertButton = WebElement(driver, '#timerAlertButton')
        self.confirmButton = WebElement(driver, '#confirmButton')
        self.promptButton = WebElement(driver, '#promtButton')
        self.confirmResult = WebElement(driver, '#confirmResult')
        self.promptResult = WebElement(driver, '#promptResult')