from driver import driver
from selenium.webdriver.support.ui import WebDriverWait
from helpers.window_helpers import handle_default_window, handle_second_window
from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from helpers.fakers_helpers import *
from selenium.webdriver.common.keys import Keys

vesting_screen = 'vesting'
streams_screen = 'streams'
app_navigation = '(//ul)[2]'
connect_button = '(//button[contains(text(),"Connect")])[1]'
phantom = '//p[contains(text(),"Phantom")]'
solflare = '//p[contains(text(),"Solflare (Web)")]'
request_airdrop_button = '//button[contains(text(),"Airdrop")]'
address_locator = '(//span[contains(@class, "font-light") and contains(@class,"text-base")])[1]'
amount_input = '//input[@id="amount"]'
release_amount_input = 'releaseAmount'
title_input = '//input[@id="subject"]'
recipient_input = '//input[@id="recipient"]'
create_button = '//button[contains(text(),"Create Vesting Contract")]'
release_frequency = 'releaseFrequencyCounter'
release_frequency_picker = 'releaseFrequencyPeriod'
second = '//option[@value="1"]'
minute = '//option[@value="60"]'
hour = '//option[@value="3600"]'
day = '//option[@value="86400"]'
week = '//option[@value="604800"]'
month = '//option[@value="2628002"]'
year = '//option[@value="31536000"]'
start_date_input = 'startDate'
end_date_input = 'endDate'
start_time_input = 'startTime'
end_time_input = 'endTime'
alert_close_button = '//*[@fill-rule="evenodd"]'
approve_button = '//*[contains(text(),"APPROVE")]'
reject_button = '//*[contains(text(),"REJECT")]'
allow_button = '//*[contains(text(),"ALLOW")]'
cancel_button = '(//button[contains(text(),"Cancel")])[3]'
transfer_button = '(//button[contains(text(),"Transfer")])[1]'
canceled_card = '//span[contains(text(),"canceled")]'
recipient_can_transfer_checkbox = 'recipientCanTransfer'
recipient_can_cancel_checkbox = 'recipientCanCancel'
sender_can_cancel_checkbox = 'senderCanCancel'
sender_can_transfer_checkbox = 'senderCanTransfer'
advanced_toggle = '(//button[@role="switch"])[4]'
transfer_recipient_address_field = '(//input[@placeholder="Recipient address"])[1]'
confirm_transfer_button = '(//button[contains(text(),"Transfer")])[2]'
withdraw_button = '(//button[contains(text(),"Withdraw")])[1]'
top_up_button = '(//button[contains(text(),"Top Up")])[1]'
confirm_withdraw_button = '(//button[contains(text(),"Withdraw")])[2]'
confirm_top_up_button = '(//button[contains(text(),"Top Up")])[2]'
cliff_date_input = 'cliffDate'
cliff_time_input = 'cliffTime'
cliff_percentage_input = 'cliffAmount'
no_streams_in_the_past_alert = '//p[contains(text(),"Cannot start stream in the past.")]'
no_negative_amount_alert = '//p[contains(text(),"Please provide amount greater than 0.")]'
not_enough_tokens_alert = '//p[contains(text(),"have enough tokens.")]'
cliff_should_happen_after_start_alert = '//p[contains(text(),"Cliff should happen after start.")]'
view_on_explorer_button = '//a[contains(text(),"View on explorer")]'
wallet_connected_alert = '//*[contains(text(),"Wallet connected!")]'
transaction_canceled_alert = '//*[contains(text(),"Transaction cancelled")]'
transaction_confirmed_alert = '//*[contains(text(),"Transaction confirmed!")]'
cant_transfer_stream_to_yourself_alert = '//*[contains(text(),"transfer stream to yourself.")]'
amount_is_required_alert = '//p[contains(text(),"Amount is required.")]'
please_provide_title_alert = '//p[contains(text(),"Please provide a subject (title).")]'
chose_recipient_alert = '//p[contains(text(),"You must choose a recipient.")]'
failed_to_send_transaction_alert = '//*[contains(text(),"failed to send transaction")]'
withdraw_amount_input_field = '(//input[@type="number" and contains(@class,"py-1.5")])[1]'
top_up_amount_input_field = '(//input[@type="number" and contains(@class,"py-1.5")])[2]'
deposited_amount_input_field = 'depositedAmount'
release_amount_input_field = 'releaseAmount'
stream_tab = '//a[contains(text(),"New Stream")]'
dev_toggle = '//button[@role="switch"]'
password = '//input[@type="password"]'
submit_password = '//*[contains(text(),"Submit")]'
auto_withdrawal = '//button[@role="switch"]'
dropdown_button = '//button[@id="headlessui-menu-button-1"]'
outgoing_page = '//button[contains(text(),"Outgoing")]'
incoming_page = '//button[contains(text(),"Incoming")]'
all_streams_page = '//button[contains(text(),"All Streams")]'
who_can_transfer_vesting = '//select[@data-testid="vesting-who-can-transfer"]'
who_can_cancel_vesting = '//select[@data-testid="vesting-who-can-cancel"]'
both_can_cancel = '(//option[@value="both"])[2]'
more_options_contract = '(((//p[contains(text(), "TestIo")]/parent::div/parent::div)[2]//button)[2])'
stream_payment_button = '//button[contains(text(),"Create Streaming Contract")]'


def select_both_can_cancel():
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, who_can_cancel_vesting))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, both_can_cancel))).click()


def click_to_outgoing_page():
    WebDriverWait(driver.instance, 10).until(ec.presence_of_element_located((By.TAG_NAME, 'body'))).send_keys(Keys.CONTROL + Keys.HOME)
    sleep(5)
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, outgoing_page))).click()


def click_to_incoming_page():
    WebDriverWait(driver.instance, 10).until(ec.presence_of_element_located((By.TAG_NAME, 'body'))).send_keys(Keys.CONTROL + Keys.HOME)
    sleep(5)
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, incoming_page))).click()


def click_to_all_streams_page():
    WebDriverWait(driver.instance, 10).until(ec.presence_of_element_located((By.TAG_NAME, 'body'))).send_keys(Keys.CONTROL + Keys.HOME)
    sleep(5)
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, all_streams_page))).click()


def click_dropdown_menu():
    sleep(10)
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, dropdown_button))).click()


def click_toggle():
    sleep(3)
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, dev_toggle))).click()


def go_to_dev_vesting():
    driver.instance.get('https://staging.streamflow.finance/' + vesting_screen)
    driver.instance.maximize_window()


def go_to_dev_stream():
    driver.instance.get('https://staging.streamflow.finance/' + streams_screen)
    driver.instance.maximize_window()


def click_on_stream_tab():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, stream_tab))).click()


def assert_page_is_loaded():
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, app_navigation)))


def enter_password_and_submit():
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, password))).send_keys('streamooor')
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, submit_password))).click()


def click_connect_button():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, connect_button))).click()


def select_phantom_wallet():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, phantom))).click()


def copy_wallet_address():
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, address_locator)))
    address = driver.instance.find_element(By.XPATH, address_locator).text
    with open('./reporting/wallets/wallet_address.txt', 'w') as file:
        file.write(str(address))


def read_wallet_address():
    with open('./reporting/wallets/wallet_address.txt', 'r') as file:
        address = file.read()
    return address


def enter_deposited_amount():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, deposited_amount_input_field))). \
        send_keys(get_deposited_amount())


def enter_amount():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, amount_input))).\
        send_keys(get_amount())


def enter_release_amount():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_amount_input_field))).\
        send_keys(get_amount())


def enter_negative_amount():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, amount_input))).\
        send_keys('-1000')


def enter_abnormal_amount():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, amount_input))). \
        send_keys('1000000000')


def enter_contract_title():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, title_input))). \
        send_keys(read_contract_title())


def enter_wallet_address():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, recipient_input))). \
        send_keys('Cetz5BzrUQzRWtHYwVqUacvvp78CUScUU5LuTAH5WR34')


def click_create_button():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, create_button))).click()


def click_create_stream_button():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, stream_payment_button))).click()


def select_frequency_picker():
    sleep(5)
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency_picker))).click()


def sender_use_seconds():
    select_frequency_picker()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, second))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))).clear()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))). \
        send_keys(get_seconds())


def sender_use_minutes():
    select_frequency_picker()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, minute))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))).clear()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))). \
        send_keys(get_minutes())


def sender_use_hours():
    select_frequency_picker()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, hour))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))).clear()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))). \
        send_keys(get_hours())


def sender_use_days():
    select_frequency_picker()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, day))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))).clear()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))). \
        send_keys(get_days())


def sender_use_weeks():
    select_frequency_picker()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, week))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))).clear()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))). \
        send_keys(get_weeks())


def sender_use_months():
    select_frequency_picker()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, month))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))).clear()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))). \
        send_keys(get_months())


def sender_use_years():
    select_frequency_picker()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, year))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))).clear()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, release_frequency))). \
        send_keys(get_years())


def set_random_date():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, start_date_input))). \
        send_keys(random_start_date())
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, end_date_input))). \
        send_keys(random_end_date())


def sender_use_past_date():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, start_date_input))). \
        send_keys(random_start_past_date())
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, end_date_input))). \
        send_keys(random_end_past_date())


def set_random_time():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, start_time_input))). \
        send_keys(random_start_time())
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, end_time_input))). \
        send_keys(random_end_time())


def close_popup_alert():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, alert_close_button))).click()


def select_solflare_web():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, solflare))).click()


def all_can_transfer_and_cancel():
    click_advanced_toggle()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, sender_can_transfer_checkbox))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, recipient_can_cancel_checkbox))).click()


def non_can_cancel_and_transfer():
    click_advanced_toggle()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, recipient_can_transfer_checkbox))).click()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.ID, sender_can_cancel_checkbox))).click()


def click_advanced_toggle():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, advanced_toggle))).click()


def transfer_to_new_recipient():
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, transfer_recipient_address_field))).send_keys('F7zQFckoPdSoCo4CZkEgrYk9r4JJ5BcizVNvj735cm19')
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, confirm_transfer_button))).click()


def sender_transfer_to_self():
    click_on_transaction_confirmed_alert()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, transfer_button))).click()
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, transfer_recipient_address_field))).send_keys(read_sender_wallet_address())
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, confirm_transfer_button))).click()


def recipient_transfer_to_self():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, transfer_button))).click()
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, transfer_recipient_address_field))).send_keys(read_wallet_address())
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, confirm_transfer_button))).click()


def read_sender_wallet_address():
    with open('./reporting/wallets/sender_address.txt', 'r') as file:
        address = file.read()
    return address


def set_random_cliff():
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.ID, cliff_date_input))).send_keys('12122026')
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.ID, cliff_time_input))).send_keys(random_start_time())
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.ID, cliff_percentage_input))).clear()
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.ID, cliff_percentage_input))).send_keys(get_cliff_percentage())


def set_past_cliff_date():
    click_advanced_toggle()
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.ID, cliff_date_input))).send_keys('12122022')
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.ID, cliff_time_input))).send_keys(random_start_time())
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.ID, cliff_percentage_input))).send_keys(get_cliff_percentage())


def assert_stream_in_the_past_error_message():
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, no_streams_in_the_past_alert)))


def assert_no_negative_amount_error_message():
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, no_negative_amount_alert)))


def assert_not_enough_tokens_error_message():
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, not_enough_tokens_alert)))


def assert_cliff_should_happen_after_start_error_message():
    WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, cliff_should_happen_after_start_alert)))


def click_on_view_on_explorer_button():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, view_on_explorer_button))).click()


def click_wallet_connected_alert():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, wallet_connected_alert))).click()


def click_on_transaction_confirmed_alert():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, transaction_confirmed_alert))).click()


def assert_must_have_fields_populated():
    WebDriverWait(driver.instance, 20).until(
        ec.presence_of_element_located((By.XPATH, please_provide_title_alert)))
    WebDriverWait(driver.instance, 20).until(
        ec.presence_of_element_located((By.XPATH, chose_recipient_alert)))
    WebDriverWait(driver.instance, 20).until(
        ec.presence_of_element_located((By.XPATH, amount_is_required_alert)))


def assert_cant_transfer_stream_to_yourself():
    WebDriverWait(driver.instance, 20).until(
        ec.presence_of_element_located((By.XPATH, cant_transfer_stream_to_yourself_alert)))


def assert_overview_section():
    pass


def withdraw_more_than_available():
    sleep(70)
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, withdraw_button))).click()
    sleep(3)
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, withdraw_amount_input_field))).clear()
    WebDriverWait(driver.instance, 20).until(
        ec.presence_of_element_located((By.XPATH, withdraw_amount_input_field))).send_keys('50000')
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, confirm_withdraw_button))).click()
    handle_second_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, approve_button))).click()
    handle_default_window()


def assert_failed_to_send_transaction_alert():
    WebDriverWait(driver.instance, 20).until(
        ec.presence_of_element_located((By.XPATH, failed_to_send_transaction_alert)))


def click_transaction_canceled_alert():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, transaction_canceled_alert))).click()


def sender_select_autowithdrawal():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, auto_withdrawal))).click()


def recipient_wait_for_autowithdrawal():
    sleep(60)





















