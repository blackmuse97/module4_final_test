from .base_page import BasePage
from .locators import BookPageLocators


class PageObject(BasePage):

    def resolve_alert(self):
        self.solve_quiz_and_get_code()

    def verify_messages_after_adding_to_basket(self):
        book_name_text = self.browser.find_element(*BookPageLocators.BOOK_NAME_TEXT)
        book_name = book_name_text.text

        msg_book_name_text = self.browser.find_element(*BookPageLocators.MSG_BOOK_NAME_TEXT)
        msg_book_name = msg_book_name_text.text

        book_price_text = self.browser.find_element(*BookPageLocators.BOOK_PRICE_TEXT)
        book_price = book_price_text.text

        basket_price_text = self.browser.find_element(*BookPageLocators.BASKET_PRICE_TEXT)
        basket_price = basket_price_text.text
        #
        assert msg_book_name == f"{book_name} has been added to your basket.", "message is incorrect"
        assert basket_price == f"Your basket total is now {book_price}", "price is incorrect"

    def should_not_be_success_message_after_adding_to_basket(self):
        assert self.is_not_element_present(*BookPageLocators.MSG_BOOK_NAME_TEXT), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_login(self):
        msg_text = self.browser.find_element(*BookPageLocators.MSG_BOOK_NAME_TEXT)
        msg = msg_text.text
        assert "has been added to your basket." not in msg, "Success message is not presented"

    def should_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*BookPageLocators.MSG_BOOK_NAME_TEXT), "don't disappeared"



