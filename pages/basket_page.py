from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        message = message.text
        assert message == "Your basket is empty. Continue shopping", "There is not message of empty basket"

    def should_not_be_items_to_buy(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket item is presented, but should not be"