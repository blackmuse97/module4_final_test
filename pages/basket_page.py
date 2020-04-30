from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_see_product_in_basket_opened_from_main_page(self):
        assert self.is_not_element_present(*BasePageLocators.BOOKS_IN_BASKET), \
            "Book is present in basket after login"
        MSG_ABOUT_EMPTY_BASKET_text = self.browser.find_element(*BasePageLocators.MSG_ABOUT_EMPTY_BASKET).text
        assert "Your basket is empty" in MSG_ABOUT_EMPTY_BASKET_text, "Message about empty basket is incorrect"