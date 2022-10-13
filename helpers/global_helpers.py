from pages.new_vesting_page import *
from pages.solflare_wallet_page import *
from reporting.allure import attach_screenshot
from selenium. webdriver. common. keys import Keys


def enter_standard_contract_details():
    enter_amount()
    explicit_wait(2)
    create_contract_title()
    enter_contract_title()
    enter_wallet_address()
    attach_screenshot(driver.instance, 'Filled Vesting Details')


def request_airdrop():
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, request_airdrop_button))).click()
    explicit_wait(2)
    approve_in_wallet()
    handle_default_window()
    driver.instance.refresh()
    select_solflare_web()
    handle_new_window()
    WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, allow_button))).click()
    handle_default_window()


def email_alert_success():
    wait_visibility(driver.instance, By.XPATH, email_sent_alert)


def sender_send_email():
    driver.instance.find_element(By.ID, recipient_email_input).send_keys('dusankovacevic01@gmail.com')


def select_both_can_cancel():
    click(driver.instance, By.XPATH, who_can_cancel_vesting)
    click(driver.instance, By.XPATH, both_can_cancel)


def select_both_can_transfer():
    click(driver.instance, By.XPATH, who_can_transfer_vesting)
    click(driver.instance, By.XPATH, both_can_transfer)


def go_to_outgoing_page():
    scroll_to_top()
    click(driver.instance, By.XPATH, outgoing_page)


def go_to_incoming_page():
    scroll_to_top()
    click(driver.instance, By.XPATH, incoming_page)


def go_to_all_streams_page():
    scroll_to_top()
    click(driver.instance, By.XPATH, all_streams_page)


def click_dropdown_menu():
    click(driver.instance, By.XPATH, dropdown_button)


def click_toggle():
    click(driver.instance, By.XPATH, dev_toggle)


def click_on_payment_tab():
    click(driver.instance, By.XPATH, new_payment_button)
    click(driver.instance, By.XPATH, stream_payment)


def click_on_vesting_tab():
    click(driver.instance, By.XPATH, new_payment_button)
    click(driver.instance, By.XPATH, vesting_payment)


def enter_password_and_submit():
    try:
        WebDriverWait(driver.instance, 3).until(ec.url_to_be('https://app.streamflow.finance/'))
        pass
    except TimeoutException:
        wait_visibility(driver.instance, By.XPATH, password)
        driver.instance.find_element(By.XPATH, password).send_keys('streamooor')
        click(driver.instance, By.XPATH, submit_password)


def find_contract_in_all_streams_and_assert():
    go_to_all_streams_page()
    driver.instance.find_element(By.XPATH, search_contracts_input_field).send_keys(read_contract_title())
    wait_visibility(driver.instance, By.XPATH, "//p[contains(text(),'" + read_contract_title() + "')]")
    attach_screenshot(driver.instance, 'Contract')


def select_devnet():
    try:
        WebDriverWait(driver.instance, 3).until(ec.url_to_be('https://app.streamflow.finance/dashboard'))
        pass
    except TimeoutException:
        click_dropdown_menu()
        click_toggle()


def click_home_button():
    click(driver.instance, By.XPATH, dashboard_tab)


def use_seconds():
    select_frequency_picker()
    click(driver.instance, By.XPATH, second)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_seconds())


def use_minutes():
    select_frequency_picker()
    click(driver.instance, By.XPATH, minute)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_minutes())


def use_hours():
    select_frequency_picker()
    click(driver.instance, By.XPATH, hour)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_hours())


def use_days():
    select_frequency_picker()
    click(driver.instance, By.XPATH, day)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_days())


def use_weeks():
    select_frequency_picker()
    click(driver.instance, By.XPATH, week)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_weeks())


def use_months():
    select_frequency_picker()
    click(driver.instance, By.XPATH, month)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_months())


def use_years():
    select_frequency_picker()
    click(driver.instance, By.XPATH, year)
    driver.instance.find_element(By.ID, release_frequency).clear()
    driver.instance.find_element(By.ID, release_frequency).send_keys(get_years())


def click_wallet_connected_alert():
    click(driver.instance, By.XPATH, wallet_connected_alert)


def wait_wallet_connect_alert_to_disappear():
    wait_invisibility(driver.instance, By.XPATH, wallet_connected_alert)


def click_on_transaction_confirmed_alert():
    click(driver.instance, By.XPATH, transaction_confirmed_alert)


def wait_transaction_confirmed_alert():
    wait_visibility(driver.instance, By.XPATH, transaction_confirmed_alert)


def find_outgoing_and_assert():
    go_to_outgoing_page()
    transaction_title = "//p[contains(text(),'" + read_contract_title() + "')]"
    title = WebDriverWait(driver.instance, 120).until(ec.presence_of_element_located((By.XPATH, transaction_title)))
    actions = ActionChains(driver.instance)
    actions.move_to_element(title).perform()


def find_incoming_and_assert():
    go_to_incoming_page()
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


def enter_contract_title():
    wait_visibility(driver.instance, By.XPATH, title_input)
    driver.instance.find_element(By.XPATH, title_input).send_keys(read_contract_title())


def enter_wallet_address():
    wait_visibility(driver.instance, By.XPATH, recipient_input)
    driver.instance.find_element(By.XPATH, recipient_input).send_keys('BarpKdmxv3K8FaJ1KsH6mvGo9GrWNKsRbWu7CLEahAzv')


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
    approve_in_wallet()
    handle_default_window()
    attach_screenshot(driver.instance, 'Contract Transferred')


def withdraw_contract():
    explicit_wait(240)
    go_to_all_streams_page()
    more_options_button = "((//p[contains(text(),'" + read_contract_title() + \
                          "')]/parent::div/parent::div)[2]//button)[2]"
    options = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, more_options_button)))
    options.click()
    withdraw_contract_button = "(((//p[contains(text(),'" + read_contract_title() + "')]/parent::div/parent::div)[2]//button)[2\
    ]/parent::div/parent::div//button[contains(text(),'Withdraw')])"
    withdraw = WebDriverWait(driver.instance, 20).until(
        ec.presence_of_element_located((By.XPATH, withdraw_contract_button)))
    withdraw.click()
    withdraw_button_confirm = "//*[contains(text(),'You can withdraw between 0')]/parent::div//button[2]"
    button = WebDriverWait(driver.instance, 20).until(ec.element_to_be_clickable((By.XPATH, withdraw_button_confirm)))
    button.click()
    approve_in_wallet()
    handle_default_window()
    explicit_wait(10)
    attach_screenshot(driver.instance, 'Contract Withdrawn')


def cancel_contract():
    more_options_button = "((//p[contains(text(),'" + read_contract_title() + \
                          "')]/parent::div/parent::div)[2]//button)[2]"
    options = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, more_options_button)))
    options.click()
    cancel_button_ui = "(((//p[contains(text(),'" + read_contract_title() + "')]/parent::div/parent::div)[2]//button)[2\
    ]/parent::div/parent::div//button[contains(text(),'Cancel')])"
    cancel = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, cancel_button_ui)))
    cancel.click()
    approve_in_wallet()
    handle_default_window()
    attach_screenshot(driver.instance, 'Contract Canceled')


def top_up_contract():
    more_options_button = "((//p[contains(text(),'" + read_contract_title() + \
                          "')]/parent::div/parent::div)[2]//button)[2]"
    options = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, more_options_button)))
    options.click()
    top_up_button_ui = "(((//p[contains(text(),'" + read_contract_title() + "')]/parent::div/parent::div)[2]//button)[2\
        ]/parent::div/parent::div//button[contains(text(),'Cancel')])"
    top_up = WebDriverWait(driver.instance, 20).until(ec.presence_of_element_located((By.XPATH, top_up_button_ui)))
    top_up.click()
    approve_in_wallet()
    handle_default_window()
    attach_screenshot(driver.instance, 'Contract Top-ed UP')


def sender_select_auto_withdrawal():
    explicit_wait(3)
    click(driver.instance, By.XPATH, auto_withdrawal)


def scroll_to_top():
    driver.instance.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
    explicit_wait(2)


def scroll_to_bottom():
    driver.instance.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    explicit_wait(2)


def find_contract_and_assert():
    go_to_all_streams_page()
    driver.instance.find_element(By.XPATH, search_contracts_input_field).send_keys(read_contract_title())
    wait_visibility(driver.instance, By.XPATH, "//p[contains(text(),'" + read_contract_title() + "')]")
    attach_screenshot(driver.instance, 'Contract')


def select_frequency_picker():
    click(driver.instance, By.ID, release_frequency_picker)


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


def connect_sender_to_app():
    enter_password_and_submit()
    connect_sender_wallet()
    select_devnet()


def add_referral():
    driver.instance.find_element(By.XPATH, referral_input_field).send_keys('HG4sYqvkTfgBvGgZZhYfws4f8BoytTr1NmcDEwkKC2z8')