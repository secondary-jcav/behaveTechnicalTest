import json
import time
from behave import fixture, use_fixture
from selenium import webdriver
"""
Environment controls dealing with before all, before scenario, feature, steps.
Useful for loading variables such as browser path
"""

CONFIG_PATH = 'config.json'
BROWSER_SLEEP = 10


@fixture
def selenium_browser_chrome(context):
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    # Assign chrome path
    chrome_path = data["browser_path"]["chrome"]
    context.browser = webdriver.Chrome(chrome_path)
    yield context.browser
    # cleanup:
    time.sleep(BROWSER_SLEEP)
    context.browser.quit()


def before_all(context):
    """
    Launch browser fixture before any & all tests
    """
    use_fixture(selenium_browser_chrome, context)

