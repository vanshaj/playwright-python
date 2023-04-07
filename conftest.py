from playwright.sync_api import playwright
import pytest
import logging
from page.login_page import LoginPage

logger = logging.getLogger(__name__)

@pytest.fixture(scope='session')
def browser_context(playwright: playwright):
    logger.info("Load environment variables")
    logger.info("Logging in with standard_user")
    browser = playwright.chromium
    context = browser.launch_persistent_context(user_data_dir="./report", headless=False)
    yield context
    context.close()

@pytest.fixture(scope='session')
def login_to_account(browser_context):
    page = browser_context.new_page()
    login_page = LoginPage(page)
    login_page.login()