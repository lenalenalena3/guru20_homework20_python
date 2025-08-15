import allure
import pytest
import allure_commons
from dotenv import load_dotenv
from selene import browser, support
import os

from appium import webdriver

from project_android.utils import attach
import config


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default='local_emulator',
        help="Укажите файл настроек: local_emulator, local_real, bstack"
    )

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    context = request.config.getoption("--context") or 'local_emulator'
    options = config.driver_options(context=context)
    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    yield

    attach.add_screenshot()
    attach.add_xml()
    session_id = browser.driver.session_id

    with allure.step('tear down app session with id: ' + session_id):
        browser.quit()

    if context == 'bstack':
        attach.add_bstack_video(session_id)
