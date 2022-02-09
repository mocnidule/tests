from helpers.window_helpers import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import allure

create_new_wallet_button = '//button[contains(text(),"Create New Wallet")]'
phantom_mnemonic = '//textarea[@rows="3"]'
confirmed_saved_mnemonic_button = '//button[contains(text(),"OK, I saved it somewhere")]'
password_first_input = '//input[@name="password.first"]'
password_confirm_input = '//input[@name="password.confirm"]'
checkbox = '//input[@type="checkbox"]'
save_button = '//button[contains(text(),"Save")]'
continue_button = '//button[contains(text(),"Continue")]'
finish_button = '//button[contains(text(),"Finish")]'
connect_button = '//button[contains(text(),"Connect")]'
import_secret_button = '//button[contains(text(),"Import secret recovery phrase")]'
approve_transaction_button = '//button[contains(text(),"Approve")]'
secret_recovery_phase_button = '//button[contains(text(),"Use Secret Recovery Phrase")]'
mnemonic_text_area = '//textarea[@placeholder="Secret phrase"]'


def create_phantom_wallet_for_sender():
    handle_new_window()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, create_new_wallet_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, phantom_mnemonic))).click()
    mnemonic_phase = driver.instance.find_element(By.XPATH, phantom_mnemonic).text
    with open('./reporting/wallets/sender_mnemonic.txt', 'w') as file:
        file.write(str(mnemonic_phase))
    allure.attach.file('./reporting/wallets/sender_mnemonic.txt',
                       attachment_type=allure.attachment_type.TEXT, name='Sender Mnemonic')
    handle_passwords_and_create()


def create_phantom_wallet_for_recipient():
    handle_new_window()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, create_new_wallet_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, phantom_mnemonic))).click()
    mnemonic_phase = driver.instance.find_element(By.XPATH, phantom_mnemonic).text
    with open('./reporting/wallets/recipient_mnemonic.txt', 'w') as file:
        file.write(str(mnemonic_phase))
    allure.attach.file('./reporting/wallets/recipient_mnemonic.txt',
                       attachment_type=allure.attachment_type.TEXT, name='Recipient Mnemonic')
    handle_passwords_and_create()


def phantom_connect_to_app():
    sleep(2)
    handle_new_window()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, connect_button))).click()
    handle_default_window()


def phantom_approve_transaction():
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, approve_transaction_button))).click()


def phantom_reconnect_recipient():
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, secret_recovery_phase_button))). \
        click()


def handle_passwords_and_create():
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, confirmed_saved_mnemonic_button))). \
        click()
    handle_phantom_standard_fields()


def click_secret_recovery_phase_button_and_reconnect():
    handle_new_window()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, secret_recovery_phase_button))). \
        click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, mnemonic_text_area))). \
        send_keys(read_recipient_mnemonic())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, import_secret_button))). \
        click()
    handle_phantom_standard_fields()


def read_recipient_mnemonic():
    with open('./recipient_mnemonic.txt', 'r') as file:
        name = file.read()
    return name


def handle_phantom_standard_fields():
    driver.instance.find_element(By.XPATH, password_first_input).send_keys('mocMOC123')
    driver.instance.find_element(By.XPATH, password_confirm_input).send_keys('mocMOC123')
    driver.instance.find_element(By.XPATH, checkbox).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, save_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, continue_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, finish_button))).click()
    handle_default_window()
