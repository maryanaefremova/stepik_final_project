from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        self.go_to_basket_page()
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket have items"
        self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BUSKET), "Basket is not empty"
