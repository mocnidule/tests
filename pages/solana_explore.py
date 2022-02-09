from driver import driver
from reporting.allure import attach_screenshot
from helpers.window_helpers import handle_third_window, handle_default_window
from selenium.webdriver.common.by import By


token_balances_section = '//h3[contains(text(),"Token Balances")]'


def go_to_token_balances_and_assert():
    handle_third_window()
    token_balance_on_solana = driver.instance.find_element(By.XPATH, token_balances_section)
    driver.instance.execute_script("arguments[0].scrollIntoView();", token_balance_on_solana)
    attach_screenshot(driver.instance, 'Token Balance on Solana Explore')
    handle_default_window()
