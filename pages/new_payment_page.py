from helpers.global_helpers import *
from helpers.fakers_helpers import *
from helpers.element_helpers import *


def enter_release_amount():
    wait_visibility(driver.instance, By.ID, release_amount_input_field)
    try:
        WebDriverWait(driver.instance, 2).until(ec.url_to_be('https://app.streamflow.finance/new-payment'))
        driver.instance.find_element(By.XPATH, amount_input).send_keys('0.01')
    except TimeoutException:
        driver.instance.find_element(By.ID, release_amount_input_field).send_keys(get_released_amount())


def enter_deposited_amount():
    wait_visibility(driver.instance, By.ID, deposited_amount_input_field)
    try:
        WebDriverWait(driver.instance, 2).until(ec.url_to_be('https://app.streamflow.finance/new-payment'))
        driver.instance.find_element(By.XPATH, amount_input).send_keys('0.1')
    except TimeoutException:
        driver.instance.find_element(By.ID, deposited_amount_input_field).send_keys(get_deposited_amount())


def fill_standard_details_for_payment():
    enter_deposited_amount()
    enter_release_amount()
    create_contract_title()
    enter_contract_title()
    enter_wallet_address()
    attach_screenshot(driver.instance, 'Payment Details')


def create_payment_contract():
    click_create_stream_button()


def click_create_stream_button():
    click(driver.instance, By.XPATH, stream_payment_button)