import pytest
from test_cources.pages.base_page import BasePage
from test_cources.pages.locators import LINK
from test_cources.pages.login_page import LoginPage
from test_cources.pages.basket_page import BasketPage
import time

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
   # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer1"
    page = BasePage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer1"
    page = BasePage(browser, LINK)
    page.open()
    time.sleep(5)
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasePage(browser, LINK)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, LINK)
    page.should_not_see_product_in_basket_opened_from_main_page()
    time.sleep(7)
