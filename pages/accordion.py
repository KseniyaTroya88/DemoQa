from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        # Элементы для первого теста (домашнее задание №8)
        self.section1_content = WebElement(driver, '#section1Content > p')
        self.section1_heading = WebElement(driver, '#section1Heading')

        # Элементы для второго теста (домашнее задание №8)
        self.section2_content_p1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section2_content_p2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section3_content = WebElement(driver, '#section3Content > p')