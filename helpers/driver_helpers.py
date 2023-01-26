from driver import driver
from reporting.allure import attach_screenshot


def tear_down():
    # for logs in driver.instance.get_log('browser'):
    #     print(logs)
    attach_screenshot(driver.instance, 'Test Done')
    driver.quit_driver()