import os
import logging

logger = logging.getLogger(__name__)

BASE_URL = None
USERNAME = None
PASSWORD = None

def load_env():
    logger.info("Loading environment variables")
    global BASE_URL, USERNAME, PASSWORD
    BASE_URL = os.environ.get('AU_BASE_URL')
    USERNAME = os.environ.get('AU_USERNAME')
    PASSWORD = os.environ.get('AU_PASSWORD')
    logger.debug(f"BASE_URL: {BASE_URL}")