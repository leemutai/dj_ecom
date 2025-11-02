import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """"
    Provide a selenium webdriver instance for Chrome browser.
    """
    options = Options()
    options.headless = False  # Set to True if you want to run in headless mode
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    browser.close()