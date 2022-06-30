from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    BUTTON_ADD_TO_BUSKET = (By.CSS_SELECTOR, ".add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main > p.price_color")
    MESSAGE_NAME_BOOK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, ".alertinner > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasketPageLocators():
    MESSAGE_EMPTY_BUSKET = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
