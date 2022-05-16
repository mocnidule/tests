from driver import driver
from helpers.window_helpers import handle_default_window, handle_second_window
from selenium.webdriver.common.by import By
from helpers.fakers_helpers import *
from selenium.webdriver.common.keys import Keys
from helpers.element_helpers import *
from helpers.batch_locators import *


vesting_screen = 'vesting'
streams_screen = 'streams'
app_navigation = '(//ul)[2]'
connect_button = '(//button[contains(text(),"Connect")])[1]'
solflare = '//p[contains(text(),"Solflare (Web)")]'
request_airdrop_button = '//button[contains(text(),"Airdrop")]'
address_locator = '(//span[contains(@class, "font-light") and contains(@class,"text-base")])[1]'
amount_input = '//input[@id="recipients.0.depositedAmount"]'
release_amount_input = 'releaseAmount'
title_input = '//input[@id="recipients.0.name"]'
recipient_input = '//input[@id="recipients.0.recipient"]'
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
withdraw_button = '(//button[contains(text(),"Withdraw")])[1]'
top_up_button = '(//button[contains(text(),"Top Up")])[1]'
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
both_can_transfer = '(//option[@value="both"])[1]'
none_can_transfer = '(//option[@value="neither"])[1]'
none_can_cancel = '(//option[@value="neither"])[2]'
more_options_contract = '(((//p[contains(text(), "TestIo")]/parent::div/parent::div)[2]//button)[2])'
stream_payment_button = '//button[contains(text(),"Create Streaming Contract")]'
transfer_address_input = '//input[@placeholder="Recipient address"]'
confirm_transfer_button = '//input[@value="HG4sYqvkTfgBvGgZZhYfws4f8BoytTr1NmcDEwkKC2z8"]/following-sibling::div//button[2]'
confirm_transfer_sender = '//input[@value="57TCgyLw4pT48A1z5fWwQ9eUWuwfpo2izzYcWVRiqEnP"]/following-sibling::div//button[2]'
confirm_transfer_recipient = '//input[@value="954fBxNr25X31DbvMkw2ta5KBjkxmMUSFHeUHuXA1VqD"]/following-sibling::div//button[2]'
confirm_withdraw_button = '//p[contains(text(), "You can withdraw between 0")]/parent::div//button[2]'
recipient_email_input = '//input[@data-testid="vesting-email"]'
add_recipient = '//button[contains(text(), "+ Add Recipient")]'


def sender_send_email():
    driver.instance.find_element(By.XPATH, recipient_email_input).send_keys('dusankovacevic01@gmail.com')


def select_both_can_cancel():
    click(driver.instance, By.XPATH, who_can_cancel_vesting)
    click(driver.instance, By.XPATH, both_can_cancel)


def select_both_can_transfer():
    click(driver.instance, By.XPATH, who_can_transfer_vesting)
    click(driver.instance, By.XPATH, both_can_transfer)


def select_none_can_transfer():
    click(driver.instance, By.XPATH, who_can_transfer_vesting)
    click(driver.instance, By.XPATH, both_can_transfer)


def click_to_outgoing_page():
    scroll_to_top()
    click(driver.instance, By.XPATH, outgoing_page)


def click_to_incoming_page():
    scroll_to_top()
    click(driver.instance, By.XPATH, incoming_page)


def click_to_all_streams_page():
    scroll_to_top()
    click(driver.instance, By.XPATH, all_streams_page)


def click_dropdown_menu():
    explicit_wait(10)
    click(driver.instance, By.XPATH, dropdown_button)


def click_toggle():
    explicit_wait(3)
    click(driver.instance, By.XPATH, dev_toggle)


def go_to_dev_vesting():
    driver.instance.get('https://staging.streamflow.finance/' + vesting_screen)
    driver.instance.maximize_window()


def go_to_dev_stream():
    driver.instance.get('https://staging.streamflow.finance/' + streams_screen)
    driver.instance.maximize_window()


def click_on_stream_tab():
    click(driver.instance, By.XPATH, stream_tab)


def assert_page_is_loaded():
    wait_visibility(driver.instance, By.XPATH, app_navigation)


def enter_password_and_submit():
    wait_visibility(driver.instance, By.XPATH, password)
    driver.instance.find_element(By.XPATH, password).send_keys('streamooor')
    click(driver.instance, By.XPATH, submit_password)


def click_connect_button():
    click(driver.instance, By.XPATH, connect_button)


def copy_wallet_address():
    wait_visibility(driver.instance, By.XPATH, address_locator)
    address = driver.instance.find_element(By.XPATH, address_locator).text
    with open('./reporting/wallets/wallet_address.txt', 'w') as file:
        file.write(str(address))


def read_wallet_address():
    with open('./reporting/wallets/wallet_address.txt', 'r') as file:
        address = file.read()
    return address


def read_amount():
    with open('./reporting/wallets/amount.txt', 'r') as file:
        address = file.read()
    return address


def enter_deposited_amount():
    wait_visibility(driver.instance, By.ID, deposited_amount_input_field)
    driver.instance.find_element(By.ID, deposited_amount_input_field).send_keys(get_deposited_amount())


def enter_amount():
    wait_visibility(driver.instance, By.XPATH, amount_input)
    driver.instance.find_element(By.XPATH, amount_input).send_keys(get_amount())


def enter_release_amount():
    wait_visibility(driver.instance, By.ID, release_amount_input_field)
    driver.instance.find_element(By.ID, release_amount_input_field).send_keys(get_amount())


def enter_negative_amount():
    wait_visibility(driver.instance, By.XPATH, amount_input)
    driver.instance.find_element(By.XPATH, amount_input).send_keys('-1000')


def enter_big_number():
    wait_visibility(driver.instance, By.XPATH, amount_input)
    driver.instance.find_element(By.XPATH, amount_input).send_keys(get_big_amount())


def enter_abnormal_amount():
    wait_visibility(driver.instance, By.XPATH, amount_input)
    driver.instance.find_element(By.XPATH, amount_input).send_keys('10000000000000')


def enter_contract_title():
    wait_visibility(driver.instance, By.XPATH, title_input)
    driver.instance.find_element(By.XPATH, title_input).send_keys(read_contract_title())


def enter_wallet_address():
    wait_visibility(driver.instance, By.XPATH, recipient_input)
    driver.instance.find_element(By.XPATH, recipient_input).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')


def click_create_button():
    click(driver.instance, By.XPATH, create_button)


def click_create_stream_button():
    click(driver.instance, By.XPATH, stream_payment_button)


def select_frequency_picker():
    explicit_wait(5)
    click(driver.instance, By.ID, release_frequency_picker)


def sender_use_seconds():
    select_frequency_picker()
    click(driver.instance, By.XPATH, second)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_seconds())


def sender_use_minutes():
    select_frequency_picker()
    click(driver.instance, By.XPATH, second)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_minutes())


def sender_use_hours():
    select_frequency_picker()
    click(driver.instance, By.XPATH, second)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_hours())


def sender_use_days():
    select_frequency_picker()
    click(driver.instance, By.XPATH, second)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_days())


def sender_use_weeks():
    select_frequency_picker()
    click(driver.instance, By.XPATH, second)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_weeks())


def sender_use_months():
    select_frequency_picker()
    click(driver.instance, By.XPATH, second)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_months())


def sender_use_years():
    select_frequency_picker()
    click(driver.instance, By.XPATH, second)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_years())


def set_random_date():
    wait_visibility(driver.instance, By.ID, start_date_input)
    driver.instance.find_element(By.ID, start_date_input).send_keys(random_start_date())
    wait_visibility(driver.instance, By.ID, end_date_input)
    driver.instance.find_element(By.ID, end_date_input).send_keys(random_end_date())


def sender_use_past_date():
    wait_visibility(driver.instance, By.ID, start_date_input)
    driver.instance.find_element(By.ID, start_date_input).send_keys(random_start_past_date())
    wait_visibility(driver.instance, By.ID, end_date_input)
    driver.instance.find_element(By.ID, end_date_input).send_keys(random_end_past_date())


def set_random_time():
    wait_visibility(driver.instance, By.ID, start_time_input)
    driver.instance.find_element(By.ID, start_time_input).send_keys(random_start_time())
    wait_visibility(driver.instance, By.ID, end_time_input)
    driver.instance.find_element(By.ID, end_date_input).send_keys(random_end_time())


def close_popup_alert():
    click(driver.instance, By.XPATH, alert_close_button)


def select_solflare_web():
    click(driver.instance, By.XPATH, solflare)


def transfer_to_new_recipient():
    try_transfer()


def try_transfer():
    try:
        elements = driver.instance.find_elements(By.XPATH, '//input[@placeholder="Recipient address"]')
        for element in elements:
            if element.is_displayed() and element.is_enabled():
                element.send_keys('HG4sYqvkTfgBvGgZZhYfws4f8BoytTr1NmcDEwkKC2z8')
            else:
                print('Could not find the element')
    except TimeoutException:
        pass
    click(driver.instance, By.XPATH, confirm_transfer_button)


def read_sender_wallet_address():
    with open('./reporting/wallets/sender_address.txt', 'r') as file:
        address = file.read()
    return address


def set_random_cliff():
    wait_visibility(driver.instance, By.ID, cliff_date_input)
    driver.instance.find_element(By.ID, cliff_date_input).send_keys('12122026')
    driver.instance.find_element(By.ID, cliff_time_input).send_keys(random_start_time())
    explicit_wait(2)
    wait_visibility(driver.instance, By.ID, cliff_percentage_input)
    driver.instance.find_element(By.ID, cliff_percentage_input).clear()
    driver.instance.find_element(By.ID, cliff_percentage_input).send_keys(get_cliff_percentage())


def set_past_cliff_date():
    wait_visibility(driver.instance, By.ID, cliff_date_input)
    driver.instance.find_element(By.ID, cliff_date_input).send_keys('12122022')
    driver.instance.find_element(By.ID, cliff_time_input).send_keys(random_start_time())
    driver.instance.find_element(By.ID, cliff_percentage_input).clear()
    driver.instance.find_element(By.ID, cliff_time_input).send_keys(get_cliff_percentage())


def assert_stream_in_the_past_error_message():
    wait_visibility(driver.instance, By.XPATH, no_streams_in_the_past_alert)


def assert_no_negative_amount_error_message():
    wait_visibility(driver.instance, By.XPATH, no_negative_amount_alert)


def assert_not_enough_tokens_error_message():
    wait_visibility(driver.instance, By.XPATH, not_enough_tokens_alert)


def assert_cliff_should_happen_after_start_error_message():
    wait_visibility(driver.instance, By.XPATH, cliff_should_happen_after_start_alert)


def click_on_view_on_explorer_button():
    click(driver.instance, By.XPATH, view_on_explorer_button)


def click_wallet_connected_alert():
    click(driver.instance, By.XPATH, wallet_connected_alert)


def click_on_transaction_confirmed_alert():
    click(driver.instance, By.XPATH, transaction_confirmed_alert)


def assert_must_have_fields_populated():
    wait_visibility(driver.instance, By.XPATH, please_provide_title_alert)
    wait_visibility(driver.instance, By.XPATH, chose_recipient_alert)
    wait_visibility(driver.instance, By.XPATH, amount_is_required_alert)


def assert_cant_transfer_stream_to_yourself():
    wait_visibility(driver.instance, By.XPATH, cant_transfer_stream_to_yourself_alert)


def assert_overview_section():
    pass


def withdraw_more_than_available():
    explicit_wait(70)
    click(driver.instance, By.XPATH, withdraw_button)
    explicit_wait(3)
    driver.instance.find_element(By.XPATH, withdraw_amount_input_field).clear()
    driver.instance.find_element(By.XPATH, withdraw_amount_input_field).send_keys('50000')
    click(driver.instance, By.XPATH, confirm_withdraw_button)
    handle_second_window()
    click(driver.instance, By.XPATH, approve_button)
    handle_default_window()


def assert_failed_to_send_transaction_alert():
    wait_visibility(driver.instance, By.XPATH, failed_to_send_transaction_alert)


def click_transaction_canceled_alert():
    click(driver.instance, By.XPATH, transaction_canceled_alert)


def sender_select_autowithdrawal():
    click(driver.instance, By.XPATH, auto_withdrawal)


def recipient_wait_for_autowithdrawal():
    explicit_wait(30)


def scroll_to_top():
    wait_visibility(driver.instance, By.TAG_NAME, 'body')
    driver.instance.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
    explicit_wait(5)


def click_add_recipient_50_times():
    button = driver.instance.find_element(By.XPATH, add_recipient)
    for i in range(50):
        button.click()


def fill_batch_details():
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_zero).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_one).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_two).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_three).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_four).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_five).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_six).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_seven).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_eight).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_nine).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_ten).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_eleven).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_twelve).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_thirteen).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_fourteen).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_fifteen).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_sixteen).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_seventeen).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_eighteen).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_nineteen).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_twenty).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_twenty_one).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_twenty_two).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_twenty_three).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_twenty_four).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_twenty_five).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_twenty_six).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_twenty_seven).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_twenty_eight).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_twenty_nine).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_thirty).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_thirty_one).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_thirty_two).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_thirty_three).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_thirty_four).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_thirty_five).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_thirty_six).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_thirty_seven).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_thirty_eight).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_thirty_nine).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_forty).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_forty_one).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_forty_two).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_forty_three).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_forty_four).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_forty_five).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_forty_six).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_forty_seven).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_forty_eight).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_forty_nine).send_keys(read_contract_title())
    create_contract_title()
    driver.instance.find_element(By.XPATH, contract_title_fifty).send_keys(read_contract_title())

    driver.instance.find_element(By.XPATH, recipient_amount_zero).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_one).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_two).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_three).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_four).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_five).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_six).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_seven).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_eight).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_nine).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_ten).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_eleven).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_twelve).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_thirteen).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_fourteen).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_fifteen).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_sixteen).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_seventeen).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_eighteen).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_nineteen).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_twenty).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_twenty_one).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_twenty_two).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_twenty_three).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_twenty_four).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_twenty_five).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_twenty_six).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_twenty_seven).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_twenty_eight).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_twenty_nine).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_thirty).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_thirty_one).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_thirty_two).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_thirty_three).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_thirty_four).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_thirty_five).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_thirty_six).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_thirty_seven).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_thirty_eight).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_thirty_nine).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_forty).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_forty_one).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_forty_two).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_forty_three).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_forty_four).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_forty_five).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_forty_six).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_forty_seven).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_forty_eight).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_forty_nine).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_fifty).send_keys(get_amount())


    driver.instance.find_element(By.XPATH, wallet_zero).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_one).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_two).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_three).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_four).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_five).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_six).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_seven).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_eight).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_nine).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_ten).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_eleven).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_twelve).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_thirteen).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_fourteen).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_fifteen).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_sixteen).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_seventeen).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_eighteen).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_nineteen).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_twenty).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_twenty_one).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_twenty_two).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_twenty_three).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_twenty_four).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_twenty_five).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_twenty_six).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_twenty_seven).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_twenty_eight).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_twenty_nine).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_thirty).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_thirty_one).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_thirty_two).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_thirty_three).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_thirty_four).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_thirty_five).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_thirty_six).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_thirty_seven).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_thirty_eight).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_thirty_nine).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_forty).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_forty_one).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_forty_two).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_forty_three).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_forty_four).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_forty_five).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_forty_six).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_forty_seven).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_forty_eight).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_forty_nine).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
    driver.instance.find_element(By.XPATH, wallet_fifty).send_keys('8CXHjjsMBde6LZADNfzHbKjqtNnNU1vmbZoviopVaei5')
