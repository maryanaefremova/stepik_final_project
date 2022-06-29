from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    URL_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    BUTTON_BUSKET = (By.CSS_SELECTOR, ".add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main > p.price_color")
    MESSAGE_NAME_BOOK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, ".alertinner > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")