from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def can_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_BUSKET)
        button.click()
        self.solve_quiz_and_get_code()
        book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_BOOK).text
        assert book == message_name, f"{book} is not {message_name}"
        price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert price == message_price, f"{price} not equal {message_price}"
