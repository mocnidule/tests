from driver import driver
from helpers.element_helpers import explicit_wait


def handle_default_window():
    explicit_wait(1)
    default_window = driver.instance.window_handles[0]
    driver.instance.switch_to.window(default_window)


def handle_new_window():
    explicit_wait(1)
    new_window = driver.instance.window_handles[1]
    driver.instance.switch_to.window(new_window)


def handle_second_window():
    explicit_wait(1)
    new_window = driver.instance.window_handles[2]
    driver.instance.switch_to.window(new_window)


def handle_third_window():
    explicit_wait(1)
    new_window = driver.instance.window_handles[3]
    driver.instance.switch_to.window(new_window)