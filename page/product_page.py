from playwright.sync_api import Page

class ProductPage:

    def __init__(self, page: Page, target_env) -> None:
        self.page = page
        self.add_to_cart_locator = "//button[@id='add-to-cart-{item_id}']"
        self.cart_locator = "//a[@class='shopping_cart_link']"
        self.url = target_env['BASE_URL'] + '/inventory.html'
        # self.add_to_cart_locator.

    def goto(self) -> None:
        self.page.goto(self.url)
        
    def add_to_cart(self,
                    list_items: list) -> None:
        for item in list_items:
            item = item.lower().replace(' ', '-')
            self.page.locator(self.add_to_cart_locator.format(item_id=item)).click()

    def click_on_cart(self) -> None:
        self.page.locator(self.cart_locator).click()

    def close(self) -> None:
        self.page.close()