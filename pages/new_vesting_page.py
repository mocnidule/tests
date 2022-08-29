from helpers.global_helpers import *
from helpers.fakers_helpers import *
from helpers.batch_helpers import *
from pages.solflare_wallet_page import *
from selenium.webdriver.common.action_chains import ActionChains
from reporting.allure import attach_screenshot


def create_vesting_contract_and_assert():
    click_create_button()
    approve_in_wallet()
    handle_default_window()
    find_contract_and_assert()


def read_amount():
    with open('./reporting/wallets/amount.txt', 'r') as file:
        address = file.read()
    return address


def set_date():
    set_random_date()


def enter_amount():
    wait_visibility(driver.instance, By.XPATH, amount_input)
    try:
        WebDriverWait(driver.instance, 3).until(ec.url_to_be('https://app.streamflow.finance/new-vesting'))
        driver.instance.find_element(By.XPATH, amount_input).send_keys('0.1')
    except TimeoutException:
        driver.instance.find_element(By.XPATH, amount_input).send_keys(get_amount())


def enter_big_number():
    wait_visibility(driver.instance, By.XPATH, amount_input)
    driver.instance.find_element(By.XPATH, amount_input).send_keys(get_big_amount())


def click_create_button():
    button = driver.instance.find_element('xpath', '//button[contains(text(),"Create Vesting Contract")]')
    actions = ActionChains(driver.instance)
    actions.move_to_element(button).perform()
    click(driver.instance, By.XPATH, '//button[contains(text(),"Create Vesting Contract")]')


def set_random_date():
    wait_visibility(driver.instance, By.ID, end_date_input)
    click(driver.instance, By.ID, end_date_input)
    driver.instance.find_element(By.ID, end_date_input).send_keys('20271226')


def set_cliff():
    wait_visibility(driver.instance, By.ID, cliff_percentage_input)
    driver.instance.find_element(By.ID, cliff_percentage_input).clear()
    driver.instance.find_element(By.ID, cliff_percentage_input).send_keys(get_cliff_percentage())


def assert_overview_section():
    pass


def click_add_recipient_4_times():
    explicit_wait(5)
    button = driver.instance.find_element(By.XPATH, add_recipient)
    for i in range(4):
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
    driver.instance.find_element(By.XPATH, recipient_amount_zero).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_one).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_two).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_three).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, recipient_amount_four).send_keys(get_amount())
    driver.instance.find_element(By.XPATH, wallet_zero).send_keys('5vt84qYFy5rE4pskRVVDsttTLYprdKPP9qtgAzy44bye')
    driver.instance.find_element(By.XPATH, wallet_one).send_keys('CauXy1r5eAFKpKfNg2jxFtqWazNKmEVM5noYjEDxQkY4')
    driver.instance.find_element(By.XPATH, wallet_two).send_keys('DADgs3ofcnxBX5H2N4JMb5j8DSBwP4mtUch6ACn8ePZD')
    driver.instance.find_element(By.XPATH, wallet_three).send_keys('9764L34rFUL7CMCd6VsAhsAA4qoHSZiKJ7dXGekKuESC')
    driver.instance.find_element(By.XPATH, wallet_four).send_keys('y9ptUGPjYXesub59gLwy2baXBWAbJDHiXLyUzsTA3pY')
    driver.instance.find_element(By.XPATH, email_one).send_keys('dusankovacevic01@gmail.com')
    driver.instance.find_element(By.XPATH, email_two).send_keys('dusandev87@gmail.com')
    driver.instance.find_element(By.XPATH, email_three).send_keys('mocnibratdule@gmail.com')
    driver.instance.find_element(By.XPATH, email_four).send_keys('dushan@streamflow.com')


def upload_csv():
    pass