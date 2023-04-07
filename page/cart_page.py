from playwright.sync_api import Page

class CartPage:
    def __init__(self,
                 page: Page) -> None:
        self.page = page
        self.item_locator = page.locator("//div[@class='inventory_item_name']")