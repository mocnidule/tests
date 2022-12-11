import driver.driver
from selenium.webdriver.common.by import By
from pages.wallet_picker_page import select_solflare_web
from helpers.element_helpers import *
from locators.element_locators import *
from helpers.window_helpers import *
from reporting.allure import attach_screenshot


def approve_in_wallet():
    handle_new_window()
    click(driver.instance, By.XPATH, approve_button)


def additional_approve_in_wallet():
    click(driver.instance, By.XPATH, approve_button)


def allow_button_handler():
    try:
        handle_new_window()
        click(driver.instance, By.XPATH, allow_button)
    except TimeoutException:
        handle_second_window()
        click(driver.instance, By.XPATH, allow_button)


def connect_button_handler():
    try:
        handle_new_window()
        click(driver.instance, By.XPATH, connect_button)
    except TimeoutException:
        handle_second_window()
        click(driver.instance, By.XPATH, connect_button)


def click_already_have_wallet():
    click(driver.instance, By.XPATH, already_have_wallet_button)


def enter_mnemonic():
    # CNKTpPfLkvSjauF2UnbYFyKzw9z1x5T6KxGFcgzk5uP9
    driver.instance.find_element(By.XPATH, mnemonic_1).send_keys('various')
    driver.instance.find_element(By.XPATH, mnemonic_2).send_keys('when')
    driver.instance.find_element(By.XPATH, mnemonic_3).send_keys('layer')
    driver.instance.find_element(By.XPATH, mnemonic_4).send_keys('medal')
    driver.instance.find_element(By.XPATH, mnemonic_5).send_keys('shock')
    driver.instance.find_element(By.XPATH, mnemonic_6).send_keys('surprise')
    driver.instance.find_element(By.XPATH, mnemonic_7).send_keys('anchor')
    driver.instance.find_element(By.XPATH, mnemonic_8).send_keys('coffee')
    driver.instance.find_element(By.XPATH, mnemonic_9).send_keys('fragile')
    driver.instance.find_element(By.XPATH, mnemonic_10).send_keys('wood')
    driver.instance.find_element(By.XPATH, mnemonic_11).send_keys('series')
    driver.instance.find_element(By.XPATH, mnemonic_12).send_keys('month')


def select_web_wallet():
    click(driver.instance, By.XPATH, wallet_connect)


def connect_sender_wallet():
    select_solflare_web()
    driver.instance.switch_to.frame(driver.instance.find_element(By.TAG_NAME, 'iframe'))
    select_web_wallet()
    try:
        handle_new_window()
        click(driver.instance, By.XPATH, already_have_wallet_button)
    except IndexError:
        handle_second_window()
        click(driver.instance, By.XPATH, already_have_wallet_button)
    enter_mnemonic()
    click(driver.instance, By.XPATH, continue_button)
    driver.instance.find_element(By.XPATH, password).send_keys('mocMOC123')
    driver.instance.find_element(By.XPATH, repeat_password).send_keys('mocMOC123')
    click(driver.instance, By.XPATH, continue_button)
    click(driver.instance, By.XPATH, import_all_button)
    explicit_wait(3)
    driver.instance.close()
    handle_default_window()
    select_solflare_web()
    driver.instance.switch_to.frame(driver.instance.find_element(By.TAG_NAME, 'iframe'))
    select_web_wallet()
    connect_button_handler()
    handle_default_window()


def connect_recipient_wallet():
    driver.instance.refresh()
    select_solflare_web()
    handle_new_window()
    click(driver.instance, By.XPATH, '//*[@data-testid="MenuIcon"]')
    click(driver.instance, By.XPATH, '//*[@viewBox="0 0 51 51"]')
    attach_screenshot(driver.instance, 'Wallet')
    click(driver.instance, By.XPATH, '//img[@alt="BarpKdmxv3K8FaJ1KsH6mvGo9GrWNKsRbWu7CLEahAzv"]')
    handle_default_window()
    select_solflare_web()
    select_solflare_web()
    handle_second_window()
    click(driver.instance, By.XPATH, connect_button)
    handle_default_window()


def chose_wallet_connect_page():
    click(driver.instance, By.XPATH, wallet_connect)

