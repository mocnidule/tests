from driver import driver
from time import sleep


def handle_new_window():
    sleep(1)
    new_window = driver.instance.window_handles[1]
    driver.instance.switch_to.window(new_window)


def handle_default_window():
    sleep(1)
    default_window = driver.instance.window_handles[0]
    driver.instance.switch_to.window(default_window)


def handle_second_window():
    sleep(1)
    new_window = driver.instance.window_handles[2]
    driver.instance.switch_to.window(new_window)


def handle_third_window():
    sleep(1)
    new_window = driver.instance.window_handles[3]
    driver.instance.switch_to.window(new_window)