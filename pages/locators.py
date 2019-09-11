from selenium.webdriver.common.by import By

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_PRICE = (By.CSS_SELECTOR,"div.product_main .price_color")
	BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR,"#messages div:nth-child(3) p")
	#NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages div:nth-child(1) strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages div:nth-child(1)")
	BOOK_NAME = (By.CSS_SELECTOR,"div.product_main h1")