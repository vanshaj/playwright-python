from playwright.sync_api import Page

class ProductPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.add_to_cart_locator = "//button[@id='add-to-cart-{item_id}']"
        self.cart_locator = "//a[@class='shopping_cart_link']"
        # self.add_to_cart_locator.

    def goto(self):
        self.page.goto('https://www.saucedemo.com/inventory.html')
        
    def add_to_cart(self,
                    list_items: list) -> None:
        for item in list_items:
            item = item.lower().replace(' ', '-')
            self.page.locator(self.add_to_cart_locator.format(item_id=item)).click()

    def click_on_cart(self) -> None:
        self.page.locator(self.cart_locator).click()

    def close(self) -> None:
        self.page.close()