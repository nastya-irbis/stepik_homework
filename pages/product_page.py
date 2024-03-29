from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def click_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
    
    def product_should_be_added_to_basket(self):
        self.should_be_equal_names()
        self.should_be_equal_prices()

    def should_be_equal_names(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name = book_name.text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        success_message = success_message.text
        assert (f"{book_name} has been added to your basket.") == success_message, "There is wrong success message"

    def should_be_equal_prices(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price.text
        basket_price_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE)
        basket_price_message = basket_price_message.text
        assert (f"Your basket total is now {product_price}") == basket_price_message, "There is wrong price message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"