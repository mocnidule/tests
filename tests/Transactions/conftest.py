import pytest
from driver import driver


@pytest.fixture(autouse=True)
def setup(url):
    driver.initialize()
    driver.instance.get(url)


@pytest.fixture(scope='class', autouse=True)
def url(request):
    return request.config.getoption('--url')
