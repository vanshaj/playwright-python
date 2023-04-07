from playwright.sync_api import playwright
import pytest
import logging
from page.product_page import ProductPage

logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def product_page(browser_context,
                 login_to_account) -> ProductPage:
    page = browser_context.new_page()
    product_page_object = ProductPage(page)
    product_page_object.goto()
    yield product_page_object
    product_page_object.close()