import pytest
from driver import driver
from reporting.allure import attach_screenshot


@pytest.fixture(autouse=True)
def setup(url):
    driver.initialize()
    driver.instance.get(url)
    yield
    # for logs in driver.instance.get_log('browser'):
    #     print(logs)
    attach_screenshot(driver.instance, 'Test Done')
    driver.quit_driver()


@pytest.fixture(scope='class', autouse=True)
def url(request):
    return request.config.getoption('--url')
