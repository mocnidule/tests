import pytest
from driver import driver


@pytest.fixture(autouse=True)
def setup(request, url):
    driver.initialize()
    driver.instance.get(url)
    request.cls.driver = driver.instance


@pytest.fixture(scope='class', autouse=True)
def url(request):
    return request.config.getoption('--url')
