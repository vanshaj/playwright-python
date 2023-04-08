import logging
from playwright.sync_api import Page

logger = logging.getLogger(__name__)

class LoginPage:
    def __init__(self,
                 page: Page,
                 target_env) -> None:
        self.page = page
        self.username_locator = "//input[@placeholder='Username']"
        self.password_locator = "//input[@placeholder='Password']"
        self.login_button_locator = "//input[@id='login-button']"
        self.url = target_env['BASE_URL']
        self.username = target_env['USERNAME']
        self.password = target_env['PASSWORD']

    def login(self) -> None:
        self.page.goto(self.url)
        self.page.locator(self.username_locator).fill(self.username)
        self.page.locator(self.password_locator).fill(self.password)
        self.page.locator(self.login_button_locator).click()
        self.page.close()