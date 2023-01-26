import driver.driver
from selenium.webdriver.common.by import By
from pages.wallet_picker_page import select_solflare
from helpers.element_helpers import *
from locators.element_locators import *
from helpers.window_helpers import *
from reporting.allure import attach_screenshot
from selenium.webdriver.common.keys import Keys


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


def enter_mnemonic_solana():
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


def connect_sender_wallet_on_solana():
    select_solflare()
    driver.instance.switch_to.frame(driver.instance.find_element(By.TAG_NAME, 'iframe'))
    click(driver.instance, By.XPATH, '//button[contains(text(),"Extension")]')
    try:
        handle_new_window()
        click(driver.instance, By.XPATH, already_have_wallet_button)
    except IndexError:
        handle_second_window()
        click(driver.instance, By.XPATH, already_have_wallet_button)
    enter_mnemonic_solana()
    click(driver.instance, By.XPATH, continue_button)
    driver.instance.find_element(By.XPATH, password).send_keys('mocMOC123')
    driver.instance.find_element(By.XPATH, repeat_password).send_keys('mocMOC123')
    click(driver.instance, By.XPATH, continue_button)
    click(driver.instance, By.XPATH, import_all_button)
    click(driver.instance, By.XPATH, not_now_button)
    driver.instance.close()
    handle_default_window()
    driver.instance.switch_to.frame(driver.instance.find_element(By.TAG_NAME, 'iframe'))
    click(driver.instance, By.XPATH, '//button[contains(text(),"Extension")]')
    connect_button_handler()
    handle_default_window()
    select_solflare()
    driver.instance.switch_to.frame(driver.instance.find_element(By.TAG_NAME, 'iframe'))
    click(driver.instance, By.XPATH, '//button[contains(text(),"Extension")]')
    connect_button_handler()
    handle_default_window()


def connect_recipient_wallet_on_solana():
    driver.instance.refresh()
    select_solflare()
    handle_new_window()
    click(driver.instance, By.XPATH, '//*[@data-testid="MenuIcon"]')
    click(driver.instance, By.XPATH, '//*[@viewBox="0 0 51 51"]')
    attach_screenshot(driver.instance, 'Wallet')
    click(driver.instance, By.XPATH, '//img[@alt="BarpKdmxv3K8FaJ1KsH6mvGo9GrWNKsRbWu7CLEahAzv"]')
    handle_default_window()
    select_solflare()
    select_solflare()
    handle_second_window()
    click(driver.instance, By.XPATH, connect_button)
    handle_default_window()


def chose_wallet_connect_page():
    click(driver.instance, By.XPATH, wallet_connect)


def mnemonic_for_aptos():
    driver.instance.find_element(By.XPATH, mnemonic_1).send_keys('buddy')
    driver.instance.find_element(By.XPATH, mnemonic_2).send_keys('monkey')
    driver.instance.find_element(By.XPATH, mnemonic_3).send_keys('job')
    driver.instance.find_element(By.XPATH, mnemonic_4).send_keys('crime')
    driver.instance.find_element(By.XPATH, mnemonic_5).send_keys('dawn')
    driver.instance.find_element(By.XPATH, mnemonic_6).send_keys('bird')
    driver.instance.find_element(By.XPATH, mnemonic_7).send_keys('panda')
    driver.instance.find_element(By.XPATH, mnemonic_8).send_keys('alone')
    driver.instance.find_element(By.XPATH, mnemonic_9).send_keys('hole')
    driver.instance.find_element(By.XPATH, mnemonic_10).send_keys('fragile')
    driver.instance.find_element(By.XPATH, mnemonic_11).send_keys('wire')
    driver.instance.find_element(By.XPATH, mnemonic_12).send_keys('ozone')


def connect_sender_on_aptos():
    handle_new_window()
    click(driver.instance, By.XPATH, '//button[contains(text(),"Import recovery phrase")]')
    driver.instance.find_element(By.XPATH, password).send_keys('mocMOC123')
    driver.instance.find_element(By.XPATH, repeat_password).send_keys('mocMOC123')
    click(driver.instance, By.XPATH, continue_button)
    mnemonic_for_aptos()
    click(driver.instance, By.XPATH, continue_button)
    click(driver.instance, By.XPATH, '//a[contains(text(),"Enter Aptos")]')
    handle_default_window()
    click(driver.instance, By.XPATH, '//button//p[contains(text(),"Rise Wallet")]')
    handle_second_window()
    click(driver.instance, By.XPATH, '(//*[contains(text(),"Connect")])[2]')
    handle_default_window()







