import pytest
from selene.support.shared import browser
import os
from dotenv import load_dotenv


load_dotenv()
shop_url = os.getenv("SHOP_API_URL")


@pytest.fixture(scope="function", autouse=True)
def browser_config():
    browser.config.base_url = shop_url
    browser.config.window_width = 1920
    browser.config.window_height = 900

    yield browser


def pytest_addoption(parser):
    parser.addoption("--env", default="prod")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")
