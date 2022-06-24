from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def can_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_BUSKET)
        button.click()
        self.solve_quiz_and_get_code()
        book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_BOOK).text
        assert book in message_name, "Некорректное название книги"
        price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert price in message_price, "Неверная цена"
