from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert "login" in self.browser.current_url, "expected login to be substring of url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        input_password.send_keys(password)
        input_password_repeat = self.browser.find_element(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD)
        input_password_repeat.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()