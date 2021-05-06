from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOG_IN_EMAIL = (By.ID, "id_login-username")
    LOG_IN_PASSWORD = (By.ID, "id_login-password")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.XPATH, "//article/div/div/p[1]")
    ITEM_NAME = (By.XPATH, "//h1")
    ITEM_ADDED_TO_BASKET_NAME = (By.XPATH, "//div[@id='messages']/div/div/strong")
    BASKET_TOTAL_NOW = (By.XPATH, "//div/div/div/p/strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p")