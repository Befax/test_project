from .base_page import BasePage
from .locators import LoginPageLocators
from mimesis import Person


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "No substring 'login' in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_EMAIL), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register form is not presented"

    def register_new_user(self):
        person = Person('en')
        email = person.email()
        password = person.password(10)
        self.fill_the_field(*LoginPageLocators.REGISTER_EMAIL, email)
        self.fill_the_field(*LoginPageLocators.REGISTER_PASSWORD, password)
        self.fill_the_field(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD, password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
