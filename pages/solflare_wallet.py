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
textarea = '//*[@name="mnemonic"]'
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
    click(driver.instance, By.XPATH, textarea)
    driver.instance.find_element(By.XPATH, textarea).send_keys \
        ('animal black credit chunk kid issue powder detail strategy hurdle art ring')


def reconnect_sender_mnemonic():
    click(driver.instance, By.XPATH, textarea)
    driver.instance.find_element(By.XPATH, textarea).send_keys \
        ('pact mountain explain away lawsuit chuckle creek prepare motion try token loyal')


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
    click(driver.instance, By.XPATH, textarea)
    driver.instance.find_element(By.XPATH, textarea).send_keys \
        ('pact mountain explain away lawsuit chuckle creek prepare motion try token loyal')
    handle_rest()


def handle_solflare_for_recipient():
    click(driver.instance, By.XPATH, textarea)
    driver.instance.find_element(By.XPATH, textarea).send_keys \
        ('animal black credit chunk kid issue powder detail strategy hurdle art ring')
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
    # sleep(100)
    # click(driver.instance, By.XPATH, quick_setup)
    handle_default_window()
    select_solflare_web()
    select_solflare_web()
    connect_button_handler()
    handle_default_window()




