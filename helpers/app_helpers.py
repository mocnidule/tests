from pages.solflare_wallet import *
from pages.app_page import *
from helpers.fakers_helpers import create_contract_title
from reporting.allure import attach_screenshot
from selenium.webdriver.common.action_chains import ActionChains
from pages.solana_explore import go_to_token_balances_and_assert
from time import sleep
from selenium.common.exceptions import TimeoutException


def select_devnet():
    sleep(15)
    click_dropdown_menu()
    click_toggle()


def go_to_vesting_and_assert_page_is_loaded():
    go_to_dev_vesting()
    enter_password_and_submit()


def go_to_stream_and_assert_page_is_loaded():
    go_to_dev_stream()
    enter_password_and_submit()


def reconnect_recipient_and_assert_vesting():
    quit_driver_to_reconnect_for_vesting()
    reconnect_recipient_common()
    find_all_streams_and_assert()
    attach_screenshot(driver.instance, 'Recipient Contract')


def reconnect_recipient_and_assert_streaming():
    quit_driver_to_reconnect_for_streaming()
    reconnect_recipient_common()
    find_all_streams_and_assert()
    attach_screenshot(driver.instance, 'Recipient Contract')


def reconnect_recipient_common():
    select_solflare_web()
    mnemonic_reconnect_for_recipient()
    select_solflare_web()
    select_solflare_web()
    handle_second_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, allow_button))).click()
    handle_default_window()
    select_devnet()


def sender_fill_standard_contract_details():
    enter_amount()
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
    click_on_stream_tab()
    click_toggle()
    enter_deposited_amount()
    enter_release_amount()
    create_contract_title()
    enter_contract_title()
    enter_wallet_address()
    attach_screenshot(driver.instance, 'Filled Streaming Details')


def sender_create_vesting_contract():
    click_create_button()
    approve_button_handler()
    handle_default_window()
    find_outgoing_and_assert()
    attach_screenshot(driver.instance, 'Sender Contract')


def sender_create_streaming_contract():
    click_create_stream_button()
    approve_button_handler()
    handle_default_window()
    find_outgoing_and_assert()
    attach_screenshot(driver.instance, 'Sender Contract')


def quit_driver_to_reconnect_for_vesting():
    driver.quit_driver()
    sleep(2)
    driver.initialize()
    go_to_vesting_and_assert_page_is_loaded()


def quit_driver_to_reconnect_for_streaming():
    driver.quit_driver()
    sleep(2)
    driver.initialize()
    go_to_stream_and_assert_page_is_loaded()


def find_outgoing_and_assert():
    click_to_outgoing_page()
    transaction_title = "//p[contains(text(),'" + read_contract_title() + "')]"
    title = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, transaction_title)))
    actions = ActionChains(driver.instance)
    actions.move_to_element(title).perform()


def find_incoming_and_assert():
    click_to_incoming_page()
    transaction_title = "//p[contains(text(),'" + read_contract_title() + "')]"
    title = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, transaction_title)))
    actions = ActionChains(driver.instance)
    actions.move_to_element(title).perform()


def find_all_streams_and_assert():
    click_to_all_streams_page()
    transaction_title = "//p[contains(text(),'" + read_contract_title() + "')]"
    title = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, transaction_title)))
    actions = ActionChains(driver.instance)
    actions.move_to_element(title).perform()


def sender_create_contract_and_recipient_assert_contract_vesting():
    sender_create_vesting_contract()
    reconnect_recipient_and_assert_vesting()
    sleep(2)


def sender_create_contract_and_recipient_assert_contract_streaming():
    sender_create_streaming_contract()
    reconnect_recipient_and_assert_streaming()
    sleep(2)


def sender_use_random_date_and_time():
    set_random_time()
    set_random_date()


def transfer_contract():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, transfer_button))).click()
    transfer_to_new_recipient()
    handle_second_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, approve_button))).click()
    handle_default_window()
    transaction_title = "//p[contains(text(),'" + read_contract_title() + "')]"
    WebDriverWait(driver.instance, 20).until(ec.invisibility_of_element((By.XPATH, transaction_title)))
    attach_screenshot(driver.instance, 'Contract Transferred')


def sender_transfer_contract():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, transfer_button))).click()
    transfer_to_new_recipient()
    handle_new_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, approve_button))).click()
    handle_default_window()


def recipient_withdraw_partial():
    sleep(30)
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, withdraw_button))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, confirm_withdraw_button))).click()
    approve_button_handler()
    handle_default_window()
    # assert_in_solana_explore()
    attach_screenshot(driver.instance, 'Partial Withdraw')


def cancel_contract():
    click_to_all_streams_page()
    more_options_button = "((//p[contains(text(),'" + read_contract_title() + \
                          "')]/parent::div/parent::div)[2]//button)[2]"
    options = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, more_options_button)))
    options.click()
    cancel_button_ui = "(((//p[contains(text(),'" + read_contract_title() + "')]/parent::div/parent::div)[2]//button)[2\
    ]/parent::div/parent::div//button[contains(text(),'Cancel')])"
    cancel = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, cancel_button_ui)))
    cancel.click()
    approve_button_handler()
    handle_default_window()
    attach_screenshot(driver.instance, 'Contract Canceled')


def withdraw_contract():
    explicit_wait(45)
    withdraw_contract_button = "//p[contains(text(),'" + read_contract_title() + "')]/parent::dl//button[contains(" \
                                                                                 "text(),'Withdraw')] "
    withdraw = WebDriverWait(driver.instance, 20).until(
        ec.presence_of_element_located((By.XPATH, withdraw_contract_button)))
    withdraw.click()
    confirm_withdrawal()
    handle_default_window()
    find_outgoing_and_assert()


def recipient_withdraw_full():
    explicit_wait(370)
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, withdraw_button))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, confirm_withdraw_button))).click()
    handle_second_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, approve_button))).click()
    handle_default_window()
    # assert_in_solana_explore()
    attach_screenshot(driver.instance, 'Full Withdraw')


def decline_then_approve_withdrawal():
    explicit_wait(70)
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, withdraw_button))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, confirm_withdraw_button))).click()
    handle_second_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, reject_button))).click()
    handle_default_window()
    click_transaction_canceled_alert()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, withdraw_button))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, confirm_withdraw_button))).click()
    handle_second_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, approve_button))).click()
    handle_default_window()


def decline_then_approve_contract_creation():
    click_create_button()
    handle_new_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, reject_button))).click()
    sleep(5)
    handle_default_window()
    click_create_button()
    handle_new_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, approve_button))).click()
    handle_default_window()
    find_outgoing_and_assert()


def assert_in_solana_explore():
    click_on_view_on_explorer_button()
    go_to_token_balances_and_assert()


def sender_top_up_while_streaming():
    sleep(80)
    top_up_common()
    attach_screenshot(driver.instance, 'Topped up while streaming')


def sender_top_up_before_stream_started():
    top_up_common()
    attach_screenshot(driver.instance, 'Topped up before streaming')


def top_up_common():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, top_up_button))).click()
    WebDriverWait(driver.instance, 20).until(
        ec.presence_of_element_located((By.XPATH, top_up_amount_input_field))).clear()
    WebDriverWait(driver.instance, 20).until(
        ec.presence_of_element_located((By.XPATH, top_up_amount_input_field))).send_keys('50')
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, confirm_top_up_button))).click()
    handle_new_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, approve_button))).click()
    handle_default_window()


def request_airdrop():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, request_airdrop_button))).click()
    sleep(2)
    approve_button_handler()
    handle_default_window()
    driver.instance.refresh()
    select_solflare_web()
    handle_new_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, allow_button))).click()
    handle_default_window()


def approve_button_handler():
    try:
        handle_new_window()
        WebDriverWait(driver.instance, 5).until(ec.element_to_be_clickable((By.XPATH, approve_button))).click()
    except TimeoutException:
        handle_second_window()
        WebDriverWait(driver.instance, 5).until(ec.element_to_be_clickable((By.XPATH, approve_button))).click()


def connect_senders_wallet():
    select_solflare_web()
    handle_new_window()
    click_already_have_wallet()
    handle_solflare_for_sender()


def connect_recipients_wallet():
    select_solflare_web()
    handle_new_window()
    click_already_have_wallet()
    handle_solflare_for_recipient()


def sender_handle_standard_contract():
    go_to_vesting_and_assert_page_is_loaded()
    connect_senders_wallet()
    sender_fill_standard_contract_details()


def confirm_withdrawal():
    while True:
        try:
            element = WebDriverWait(driver.instance, 2).until(ec.element_to_be_clickable((By.XPATH, '//p[contains(text()\
            , "You can withdraw between 0")]/parent::div//button')))
            element.click()
            approve_button_handler()
        except TimeoutException:
            break
