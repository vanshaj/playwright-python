import logging
from playwright.sync_api import Page
from config.env import BASE_URL, USERNAME, PASSWORD

logger = logging.getLogger(__name__)

class LoginPage:
    def __init__(self,
                 page: Page) -> None:
        self.page = page
        self.username_locator = "//input[@placeholder='Username']"
        self.password_locator = "//input[@placeholder='Password']"
        self.login_button_locator = "//input[@id='login-button']"

    def login(self) -> None:
        self.page.goto('https://www.saucedemo.com/')
        self.page.locator(self.username_locator).fill('standard_user')
        self.page.locator(self.password_locator).fill('secret_sauce')
        self.page.locator(self.login_button_locator).click()
        self.page.close()