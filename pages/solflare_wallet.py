import driver.driver
from helpers.window_helpers import *
from selenium.webdriver.common.by import By
from pages.app_page import select_solflare_web
from helpers.element_helpers import *
from selenium.common.exceptions import TimeoutException

create_new_wallet_button = '//*[contains(text(),"I NEED A NEW WALLET")]'
already_have_wallet_button = '//*[contains(text(),"I ALREADY HAVE A WALLET")]'
advanced_button = '//*[contains(text(),"Advanced")]'
quick_setup = '//*[contains(text(),"Quick setup")]'
skip_button = '//span[contains(text(),"Skip")]'
wrote_down_mnemonic_button = '//*[contains(text(),"I SAVED MY RECOVERY PHRASE")]'
verify_button = '//span[contains(text(),"Verify")]'
allow_button = '//span[contains(text(),"Allow")]'
allow_button_capital = '//span[contains(text(),"ALLOW")]'
next_step_button = '//span[contains(text(),"Next step")]'
close_button = '//span[contains(text(),"Close")]'
copy_mnemonic_button = '//*[contains(text(),"Copy")]'
access_button = '//span[contains(text(),"Access")]'
mnemonic_input = '//input[@id="mnemonic-input-0"]'
mnemonic_input_reconnect = '// textarea[1]'
field_set = '//*[@aria-haspopup="listbox"]'
select_right_wallet = '(//div[contains(@class, "MuiListItemText-multiline")])[2]'
continue_button = '//*[contains(text(),"Continue")]'
phase_12 = '//button[contains(text(),"12")]'
mnemonic_1 = '//input[@id="mnemonic-input-0"]'
mnemonic_2 = '//input[@id="mnemonic-input-1"]'
mnemonic_3 = '//input[@id="mnemonic-input-2"]'
mnemonic_4 = '//input[@id="mnemonic-input-3"]'
mnemonic_5 = '//input[@id="mnemonic-input-4"]'
mnemonic_6 = '//input[@id="mnemonic-input-5"]'
mnemonic_7 = '//input[@id="mnemonic-input-6"]'
mnemonic_8 = '//input[@id="mnemonic-input-7"]'
mnemonic_9 = '//input[@id="mnemonic-input-8"]'
mnemonic_10 = '//input[@id="mnemonic-input-9"]'
mnemonic_11 = '//input[@id="mnemonic-input-10"]'
mnemonic_12 = '//input[@id="mnemonic-input-11"]'
password = '//input[@name="password"]'
repeat_password = '//input[@name="password2"]'
connect_button = '//*[contains(text(),"Connect")]'
import_all_button = '//*[contains(text(),"Import all")]'
menu_button = '//button[@id="headlessui-menu-button-1"]'
disconnect_wallet = '//span[contains(text(),"Disconnect Wallet")]'
solflare_settings_button = '//p[contains(text(),"Settings")]'
main_account_button = '(//div[@role="button"])[1]'
add_new_account_button = '//span[contains(text(),"Add a new account")]'
pick_recipient_wallet = '(//span[@data-id="mnemonic_account_checkbox"])[2]'
save_button = '//button[@data-id="save_button"]'
menu_var = '(//button)[1]'


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


def connect_sender_wallet():
    select_solflare_web()
    handle_new_window()
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
    select_solflare_web()
    connect_button_handler()
    handle_default_window()


def connect_recipient_wallet():
    driver.instance.refresh()
    select_solflare_web()
    handle_new_window()
    click(driver.instance, By.XPATH, solflare_settings_button)
    click(driver.instance, By.XPATH, main_account_button)
    click(driver.instance, By.XPATH, pick_recipient_wallet)
    click(driver.instance, By.XPATH, save_button)
    click(driver.instance, By.XPATH, '//span[contains(text(),"BarpKdmxv3K8FaJ1KsH6mvGo9GrWNKsRbWu7CLEahAzv")]')
    handle_default_window()
    select_solflare_web()
    select_solflare_web()
    handle_second_window()
    # uncomment if not using headless
    connect_button_handler()
    # click(driver.instance, By.XPATH, connect_button)
    # comment
    # out if using headless
    handle_default_window()


