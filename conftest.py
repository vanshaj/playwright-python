import json
import os
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

def pytest_addoption(parser):
  parser.addoption(
    '--config-file',
    action='store',
    default='config.json',
    help='Path to the target environment config file')

@pytest.fixture(scope='session')
def target_env(request):
    config_path = request.config.getoption('--config-file')
    config_path = os.path.join(os.path.dirname(__file__), "config" , config_path)
    with open(config_path) as config_file:
        config_data = json.load(config_file)
    assert 'BASE_URL' in config_data, 'No base url found'
    assert 'USERNAME' in config_data, 'No username found'
    assert 'PASSWORD' in config_data, 'No password found'
    return config_data

@pytest.fixture(scope='session')
def login_to_account(browser_context,
                     target_env):
    page = browser_context.new_page()
    login_page = LoginPage(page, target_env=target_env)
    login_page.login()