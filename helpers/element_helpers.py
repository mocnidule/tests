from selenium.webdriver import Remote
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


def wait_visibility(
        web_driver: Remote,
        by: str,
        selector_name: str,
        fail_on_timeout: bool = True,
        time_to_wait: int = 30
) -> None:
    try:
        WebDriverWait(web_driver, time_to_wait, poll_frequency=1).until(
            ec.presence_of_element_located((by, selector_name))
        )
    except TimeoutException:
        if fail_on_timeout:
            assert False


def click(web_driver: Remote, by: str, selector: str, time_to_wait: int = 30) -> None:
    try:
        WebDriverWait(web_driver, time_to_wait, poll_frequency=1).until(
            ec.element_to_be_clickable((by, selector))
        ).click()
    except TimeoutException:
        pass


def wait_invisibility(
        web_driver: Remote,
        by: str, selector: str,
        time_to_wait: int = 30,
        fail_on_timeout: bool = True
) -> None:
    try:
        WebDriverWait(web_driver, time_to_wait, poll_frequency=1).until(
            ec.invisibility_of_element((by, selector))
        )
    except TimeoutException:
        if fail_on_timeout:
            assert False


def explicit_wait(seconds: int) -> None:
    time.sleep(seconds)

