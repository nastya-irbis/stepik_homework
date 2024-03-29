from selenium.webdriver.common.by import By

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
	PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
	CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	VIEW_BASKET_BUTTON =(By.CSS_SELECTOR, "div.basket-mini a.btn-default")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_PRICE = (By.CSS_SELECTOR,"div.product_main .price_color")
	BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR,"#messages div:nth-child(3) p")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages div:nth-child(1) > div")
	BOOK_NAME = (By.CSS_SELECTOR,"div.product_main h1")

class BasketPageLocators():
	EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")
	BASKET_ITEM = (By.CSS_SELECTOR, "div.basket-items")