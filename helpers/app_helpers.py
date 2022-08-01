from pages.solflare_wallet import *
from pages.app_page import *
from helpers.fakers_helpers import create_contract_title
from reporting.allure import attach_screenshot
from selenium.webdriver.common.action_chains import ActionChains
from pages.solana_explore import go_to_token_balances_and_assert
from time import sleep
from selenium.common.exceptions import TimeoutException
from helpers.element_helpers import explicit_wait


def find_contract_and_assert():
    go_to_all_streams_page()
    driver.instance.find_element(By.XPATH, search_contracts_input_field).send_keys(read_contract_title())
    wait_visibility(driver.instance, By.XPATH, "//p[contains(text(),'" + read_contract_title() + "')]")
    attach_screenshot(driver.instance, 'Contract')


def select_devnet():
    click_dropdown_menu()
    click_toggle()


def enter_standard_contract_details():
    enter_amount()
    explicit_wait(2)
    create_contract_title()
    enter_contract_title()
    enter_wallet_address()
    attach_screenshot(driver.instance, 'Filled Vesting Details')


def enter_mainnet_vesting_contract_details():
    wait_visibility(driver.instance, By.XPATH, amount_input)
    driver.instance.find_element(By.XPATH, amount_input).send_keys('0.1')
    explicit_wait(2)
    create_contract_title()
    enter_contract_title()
    enter_wallet_address()
    attach_screenshot(driver.instance, 'Filled Vesting Details')


def sender_fill_big_amount_contract_details():
    enter_big_number()
    explicit_wait(2)
    create_contract_title()
    enter_contract_title()
    enter_wallet_address()


def fill_standard_details_for_streaming():
    enter_deposited_amount()
    enter_release_amount()
    create_contract_title()
    enter_contract_title()
    enter_wallet_address()
    attach_screenshot(driver.instance, 'Filled Streaming Details')


def fill_mainnet_details_for_streaming():
    wait_visibility(driver.instance, By.ID, deposited_amount_input_field)
    driver.instance.find_element(By.ID, deposited_amount_input_field).send_keys('0.1')
    wait_visibility(driver.instance, By.ID, release_amount_input_field)
    driver.instance.find_element(By.ID, release_amount_input_field).send_keys('0.01')
    create_contract_title()
    enter_contract_title()
    enter_wallet_address()
    attach_screenshot(driver.instance, 'Filled Streaming Details')


def create_vesting_contract_and_assert():
    click_create_button()
    approve_transaction_in_solflare()
    handle_default_window()
    find_contract_and_assert()


def create_payment_contract():
    click_create_stream_button()
    approve_transaction_in_solflare()
    handle_default_window()
    find_contract_and_assert()


def find_outgoing_and_assert():
    click_to_outgoing_page()
    transaction_title = "//p[contains(text(),'" + read_contract_title() + "')]"
    title = WebDriverWait(driver.instance, 120).until(ec.presence_of_element_located((By.XPATH, transaction_title)))
    actions = ActionChains(driver.instance)
    actions.move_to_element(title).perform()


def find_incoming_and_assert():
    click_to_incoming_page()
    transaction_title = "//p[contains(text(),'" + read_contract_title() + "')]"
    title = WebDriverWait(driver.instance, 120).until(ec.presence_of_element_located((By.XPATH, transaction_title)))
    actions = ActionChains(driver.instance)
    actions.move_to_element(title).perform()


def find_all_streams_and_assert():
    go_to_all_streams_page()
    transaction_title = "//p[contains(text(),'" + read_contract_title() + "')]"
    title = WebDriverWait(driver.instance, 120).until(ec.presence_of_element_located((By.XPATH, transaction_title)))
    actions = ActionChains(driver.instance)
    actions.move_to_element(title).perform()


def use_random_date_and_time():
    set_random_time()
    set_random_date()


def recipient_withdraw_partial():
    sleep(30)
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, withdraw_button))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, confirm_withdraw_button))).click()
    approve_transaction_in_solflare()
    handle_default_window()
    attach_screenshot(driver.instance, 'Partial Withdraw')


def cancel_contract():
    more_options_button = "((//p[contains(text(),'" + read_contract_title() + \
                          "')]/parent::div/parent::div)[2]//button)[2]"
    options = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, more_options_button)))
    options.click()
    cancel_button_ui = "(((//p[contains(text(),'" + read_contract_title() + "')]/parent::div/parent::div)[2]//button)[2\
    ]/parent::div/parent::div//button[contains(text(),'Cancel')])"
    cancel = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, cancel_button_ui)))
    cancel.click()
    approve_transaction_in_solflare()
    handle_default_window()
    attach_screenshot(driver.instance, 'Contract Canceled')


def transfer_contract():
    go_to_all_streams_page()
    more_options_button = "((//p[contains(text(),'" + read_contract_title() + \
                          "')]/parent::div/parent::div)[2]//button)[2]"
    options = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, more_options_button)))
    options.click()
    transfer_button_ui = "(((//p[contains(text(),'" + read_contract_title() + "')]/parent::div/parent::div)[2]//button)[2\
    ]/parent::div/parent::div//button[contains(text(),'Transfer')])"
    transfer = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, transfer_button_ui)))
    transfer.click()
    transfer_to_new_recipient()
    approve_transaction_in_solflare()
    handle_default_window()
    attach_screenshot(driver.instance, 'Contract Transferred')


def sender_transfer_to_self():
    go_to_all_streams_page()
    more_options_button = "((//p[contains(text(),'" + read_contract_title() + \
                          "')]/parent::div/parent::div)[2]//button)[2]"
    options = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, more_options_button)))
    options.click()
    transfer_button_ui = "(((//p[contains(text(),'" + read_contract_title() + "')]/parent::div/parent::div)[2]//button)[2\
        ]/parent::div/parent::div//button[contains(text(),'Transfer')])"
    transfer = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, transfer_button_ui)))
    transfer.click()
    try:
        elements = driver.instance.find_elements(By.XPATH, '//input[@placeholder="Recipient address"]')
        for element in elements:
            if element.is_displayed() and element.is_enabled():
                element.send_keys('57TCgyLw4pT48A1z5fWwQ9eUWuwfpo2izzYcWVRiqEnP')
            else:
                print('Could not find the element')
    except TimeoutException:
        pass
    click(driver.instance, By.XPATH, confirm_transfer_sender)


def recipient_transfer_to_self():
    go_to_all_streams_page()
    more_options_button = "((//p[contains(text(),'" + read_contract_title() + \
                          "')]/parent::div/parent::div)[2]//button)[2]"
    options = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, more_options_button)))
    options.click()
    transfer_button_ui = "(((//p[contains(text(),'" + read_contract_title() + "')]/parent::div/parent::div)[2]//button)[2\
           ]/parent::div/parent::div//button[contains(text(),'Transfer')])"
    transfer = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, transfer_button_ui)))
    transfer.click()
    try:
        elements = driver.instance.find_elements(By.XPATH, '//input[@placeholder="Recipient address"]')
        for element in elements:
            if element.is_displayed() and element.is_enabled():
                element.send_keys('954fBxNr25X31DbvMkw2ta5KBjkxmMUSFHeUHuXA1VqD')
            else:
                print('Could not find the element')
    except TimeoutException:
        pass
    click(driver.instance, By.XPATH, confirm_transfer_recipient)


def withdraw_contract():
    go_to_all_streams_page()
    more_options_button = "((//p[contains(text(),'" + read_contract_title() + \
                          "')]/parent::div/parent::div)[2]//button)[2]"
    options = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, more_options_button)))
    options.click()
    explicit_wait(100)
    withdraw_contract_button = "(((//p[contains(text(),'" + read_contract_title() + "')]/parent::div/parent::div)[2]//button)[2\
    ]/parent::div/parent::div//button[contains(text(),'Withdraw')])"
    withdraw = WebDriverWait(driver.instance, 20).until(
        ec.presence_of_element_located((By.XPATH, withdraw_contract_button)))
    withdraw.click()
    withdraw_button_confirm = "//p[contains(text(),'" + str(read_amount()) + "')]/parent::div//button[1]"
    button = WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, withdraw_button_confirm)))
    button.click()
    approve_transaction_in_solflare()
    handle_default_window()
    attach_screenshot(driver.instance, 'Contract Withdrawn')


def top_up_contract():
    pass


def assert_in_solana_explore():
    click_on_view_on_explorer_button()
    go_to_token_balances_and_assert()


def request_airdrop():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, request_airdrop_button))).click()
    sleep(2)
    approve_transaction_in_solflare()
    handle_default_window()
    driver.instance.refresh()
    select_solflare_web()
    handle_new_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, allow_button))).click()
    handle_default_window()


def approve_transaction_in_solflare():
    handle_new_window()
    click(driver.instance, By.XPATH, approve_button)





