from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK_ON_LOGIN), "Login link is not presented"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register is not presented"
        assert True

    def register_new_user(self, email, password):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK_ON_LOGIN)
        login_link.click()
        Email_address = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        Email_address.send_keys(email)
        Password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        Password.send_keys(password)
        Confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_FIELD)
        Confirm_password.send_keys(password)
        Register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        Register.click()