from playwright.sync_api import expect, Page
import pytest
import logging

logger = logging.getLogger(__name__)

items_in_cart = [['Sauce Labs Backpack'], ['Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket']]
class TestCart:
    @pytest.mark.parametrize("items", items_in_cart)
    def test_add_to_cart(self,
                         product_page,
                         items) -> None:
        product_page.add_to_cart(items)
        product_page.click_on_cart()
        

# @pytest.skip("Skip this test for now")
# def test_basic_duckduck_search(page: Page,
#                                search_action) -> None:
#     # Given the DUckDucGo home page is displayed
#     search_action.load()

#     # When the user searches for "panda"
#     search_action.search('panda')
#     # page.fill("//input[@name='q']", 'panda'")

#     # Then the search result title contains "panda"
#     element = page.locator("//input[@id='search_form_input']")
#     expect(element).to_have_value("panda") # will wait for the element to be available then check the value
    
#     # # And the search result links is "panda"
#     # page.locator('.result__title a.result__a').nth(4).wait_for()
#     # titles = page.locator('.result__title a.result__a').all_text_contents()
#     # matcher = [t for t in titles if 'panda' in t.lower()]
#     # assert len(matcher) > 0

#     # # And the search result links pertain to "panda"
#     # expect(page).to_have_title('panda at DuckDuckGo')
#     pass

# def test_basic(function_fixture):
#     logger.debug("test_basic started")
#     logger.info("test_basic started info")

# def test_basic2(function_fixture):
#     logger.debug("test_basic2 started")
#     logger.info("test_basic2 started info")
#     assert False