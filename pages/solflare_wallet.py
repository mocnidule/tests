from helpers.window_helpers import *
from selenium.webdriver.common.by import By
from pages.app_page import select_solflare_web
from helpers.element_helpers import *
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

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


def solflare_common_intro():
    select_solflare_web()
    handle_new_window()
    driver.instance.maximize_window()
    click(driver.instance, By.XPATH, create_new_wallet_button)
    click(driver.instance, By.XPATH, copy_mnemonic_button)


def solflare_common_outro():
    click(driver.instance, By.XPATH, continue_button)
    click(driver.instance, By.XPATH, continue_button)
    handle_default_window()
    select_solflare_web()
    select_solflare_web()
    allow_button_handler()
    handle_default_window()


def mnemonic_reconnect_for_recipient():
    handle_new_window()
    click(driver.instance, By.XPATH, already_have_wallet_button)
    reconnect_recipient_mnemonic()
    click(driver.instance, By.XPATH, continue_button)
    explicit_wait(5)
    continue_btn = '//*[contains(text(),"Continue")]'
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    next_button = WebDriverWait(driver.instance, 120, ignored_exceptions=ignored_exceptions) \
        .until(ec.presence_of_element_located((By.XPATH, continue_btn)))
    driver.instance.find_element(By.XPATH, password).send_keys('mocMOC123')
    driver.instance.find_element(By.XPATH, repeat_password).send_keys('mocMOC123')
    next_button.click()
    # click(driver.instance, By.XPATH, advanced_button)
    click(driver.instance, By.XPATH, quick_setup)
    # click(driver.instance, By.XPATH, continue_button)
    handle_default_window()


def mnemonic_reconnect_for_sender():
    handle_new_window()
    click(driver.instance, By.XPATH, already_have_wallet_button)
    reconnect_sender_mnemonic()
    click(driver.instance, By.XPATH, continue_button)
    explicit_wait(5)
    continue_btn = '//*[contains(text(),"Continue")]'
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    next_button = WebDriverWait(driver.instance, 120, ignored_exceptions=ignored_exceptions) \
        .until(ec.presence_of_element_located((By.XPATH, continue_btn)))
    driver.instance.find_element(By.XPATH, password).send_keys('mocMOC123')
    driver.instance.find_element(By.XPATH, repeat_password).send_keys('mocMOC123')
    next_button.click()
    click(driver.instance, By.XPATH, advanced_button)
    click(driver.instance, By.XPATH, select_right_wallet)
    click(driver.instance, By.XPATH, continue_button)
    handle_default_window()


def reconnect_recipient_mnemonic():
    driver.instance.find_element(By.XPATH, mnemonic_1).send_keys('animal')
    driver.instance.find_element(By.XPATH, mnemonic_2).send_keys('black')
    driver.instance.find_element(By.XPATH, mnemonic_3).send_keys('credit')
    driver.instance.find_element(By.XPATH, mnemonic_4).send_keys('chunk')
    driver.instance.find_element(By.XPATH, mnemonic_5).send_keys('kid')
    driver.instance.find_element(By.XPATH, mnemonic_6).send_keys('issue')
    driver.instance.find_element(By.XPATH, mnemonic_7).send_keys('powder')
    driver.instance.find_element(By.XPATH, mnemonic_8).send_keys('detail')
    driver.instance.find_element(By.XPATH, mnemonic_9).send_keys('strategy')
    driver.instance.find_element(By.XPATH, mnemonic_10).send_keys('hurdle')
    driver.instance.find_element(By.XPATH, mnemonic_11).send_keys('art')
    driver.instance.find_element(By.XPATH, mnemonic_12).send_keys('ring')


def reconnect_sender_mnemonic():
    driver.instance.find_element(By.XPATH, mnemonic_1).send_keys('pact')
    driver.instance.find_element(By.XPATH, mnemonic_2).send_keys('mountain')
    driver.instance.find_element(By.XPATH, mnemonic_3).send_keys('explain')
    driver.instance.find_element(By.XPATH, mnemonic_4).send_keys('away')
    driver.instance.find_element(By.XPATH, mnemonic_5).send_keys('lawsuit')
    driver.instance.find_element(By.XPATH, mnemonic_6).send_keys('chuckle')
    driver.instance.find_element(By.XPATH, mnemonic_7).send_keys('creek')
    driver.instance.find_element(By.XPATH, mnemonic_8).send_keys('prepare')
    driver.instance.find_element(By.XPATH, mnemonic_9).send_keys('motion')
    driver.instance.find_element(By.XPATH, mnemonic_10).send_keys('try')
    driver.instance.find_element(By.XPATH, mnemonic_11).send_keys('token')
    driver.instance.find_element(By.XPATH, mnemonic_12).send_keys('loyal')


def allow_button_handler():
    try:
        handle_new_window()
        if allow_button is not None:
            WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, allow_button))).click()
        else:
            WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, allow_button_capital))).click()
    except TimeoutException:
        handle_second_window()
        if allow_button is not None:
            WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, allow_button))).click()
        else:
            WebDriverWait(driver.instance, 20).until(
                ec.element_to_be_clickable((By.XPATH, allow_button_capital))).click()


def connect_button_handler():
    try:
        handle_new_window()
        if connect_button is not None:
            WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, connect_button))).click()
        else:
            WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, connect_button))).click()
    except TimeoutException:
        handle_second_window()
        if connect_button is not None:
            WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, connect_button))).click()
        else:
            WebDriverWait(driver.instance, 20).until(
                ec.element_to_be_clickable((By.XPATH, connect_button))).click()


def click_already_have_wallet():
    click(driver.instance, By.XPATH, already_have_wallet_button)


def handle_solflare_for_sender():
    click(driver.instance, By.XPATH, phase_12)
    driver.instance.find_element(By.XPATH, mnemonic_1).send_keys('pact')
    driver.instance.find_element(By.XPATH, mnemonic_2).send_keys('mountain')
    driver.instance.find_element(By.XPATH, mnemonic_3).send_keys('explain')
    driver.instance.find_element(By.XPATH, mnemonic_4).send_keys('away')
    driver.instance.find_element(By.XPATH, mnemonic_5).send_keys('lawsuit')
    driver.instance.find_element(By.XPATH, mnemonic_6).send_keys('chuckle')
    driver.instance.find_element(By.XPATH, mnemonic_7).send_keys('creek')
    driver.instance.find_element(By.XPATH, mnemonic_8).send_keys('prepare')
    driver.instance.find_element(By.XPATH, mnemonic_9).send_keys('motion')
    driver.instance.find_element(By.XPATH, mnemonic_10).send_keys('try')
    driver.instance.find_element(By.XPATH, mnemonic_11).send_keys('token')
    driver.instance.find_element(By.XPATH, mnemonic_12).send_keys('loyal')
    handle_rest()


def handle_solflare_for_recipient():
    driver.instance.find_element(By.XPATH, mnemonic_1).send_keys('animal')
    driver.instance.find_element(By.XPATH, mnemonic_2).send_keys('black')
    driver.instance.find_element(By.XPATH, mnemonic_3).send_keys('credit')
    driver.instance.find_element(By.XPATH, mnemonic_4).send_keys('chunk')
    driver.instance.find_element(By.XPATH, mnemonic_5).send_keys('kid')
    driver.instance.find_element(By.XPATH, mnemonic_6).send_keys('issue')
    driver.instance.find_element(By.XPATH, mnemonic_7).send_keys('powder')
    driver.instance.find_element(By.XPATH, mnemonic_8).send_keys('detail')
    driver.instance.find_element(By.XPATH, mnemonic_9).send_keys('strategy')
    driver.instance.find_element(By.XPATH, mnemonic_10).send_keys('hurdle')
    driver.instance.find_element(By.XPATH, mnemonic_11).send_keys('art')
    driver.instance.find_element(By.XPATH, mnemonic_12).send_keys('ring')
    handle_rest()


def handle_rest():
    click(driver.instance, By.XPATH, continue_button)
    explicit_wait(2)
    driver.instance.find_element(By.XPATH, password).send_keys('mocMOC123')
    driver.instance.find_element(By.XPATH, repeat_password).send_keys('mocMOC123')
    continue_btn = '//*[contains(text(),"Continue")]'
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    next_button = WebDriverWait(driver.instance, 120, ignored_exceptions=ignored_exceptions) \
        .until(ec.presence_of_element_located((By.XPATH, continue_btn)))
    next_button.click()
    click(driver.instance, By.XPATH, import_all_button)
    handle_default_window()
    select_solflare_web()
    select_solflare_web()
    connect_button_handler()
    handle_default_window()




