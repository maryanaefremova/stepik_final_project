from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)   #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.can_add_product_to_basket()
