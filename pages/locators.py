from selenium.webdriver.common.by import By

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_LINK_ON_LOGIN = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class BookPageLocators():
    BOOK_NAME_TEXT = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    MSG_BOOK_NAME_TEXT = (By.CSS_SELECTOR,"#messages > div:nth-child(1) > div")
    BOOK_PRICE_TEXT = (By.CSS_SELECTOR,"#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    BASKET_PRICE_TEXT = (By.CSS_SELECTOR,"#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1)")


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    BOOKS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    MSG_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")