import pytest
from test_cources.pages.locators import LINK
from .pages.product_page import PageObject
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from test_cources.pages.basket_page import BasketPage
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    browser.get(link)
    browser.implicitly_wait(10)
    button = browser.find_element_by_css_selector("#add_to_basket_form > button")
    button.click()

    page = PageObject(browser, link)
    page.resolve_alert()
    page.verify_messages_after_adding_to_basket()

    time.sleep(3)


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasePage(browser, LINK)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, LINK)
    page.should_not_see_product_in_basket_opened_from_main_page()
    time.sleep(7)


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LINK)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "PassWordnotCommon123456789"
        page.register_new_user(email, password)
        page = BasePage(browser, LINK)
        browser.implicitly_wait(15)
        page.should_be_authorized_user()
        time.sleep(7)

    def test_user_cant_see_success_message(self, browser):
        page = PageObject(browser, LINK)
        browser.implicitly_wait(10)
        page.should_not_be_success_message_after_login()
        time.sleep(3)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        browser.get(link)
        browser.implicitly_wait(10)
        button = browser.find_element_by_css_selector("#add_to_basket_form > button")
        button.click()

        page = PageObject(browser, link)
        page.resolve_alert()
        page.verify_messages_after_adding_to_basket()
        time.sleep(3)
