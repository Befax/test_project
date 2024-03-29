from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def names_are_equal(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_added_to_basket_name = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TO_BASKET_NAME).text
        assert item_added_to_basket_name == item_name, "names  are not equal"

    def prices_are_equal(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        basket_total_now = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_NOW).text
        assert basket_total_now == price, "prices are noy equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message doesn't disappear, but should do"
