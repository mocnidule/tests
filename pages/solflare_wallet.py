from helpers.window_helpers import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.app_page import select_solflare_web


create_new_wallet_button = '//*[contains(text(),"I NEED A NEW WALLET")]'
already_have_wallet_button = '//*[contains(text(),"I ALREADY HAVE A WALLET")]'
advanced_button = '//*[contains(text(),"Advanced")]'
skip_button = '//span[contains(text(),"Skip")]'
wrote_down_mnemonic_button = '//*[contains(text(),"I SAVED MY RECOVERY PHRASE")]'
verify_button = '//span[contains(text(),"Verify")]'
allow_button = '//span[contains(text(),"ALLOW")]'
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


def create_wallet_for_sender():
    select_solflare_web()
    handle_new_window()
    driver.instance.maximize_window()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, create_new_wallet_button))).click()
    get_sender_mnemonic()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, wrote_down_mnemonic_button))).click()
    collect_sender_mnemonics()
    solflare_common_outro()


def create_wallet_for_recipient():
    select_solflare_web()
    handle_new_window()
    driver.instance.maximize_window()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, create_new_wallet_button))).click()
    get_recipient_mnemonic()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, wrote_down_mnemonic_button))).click()
    collect_recipient_mnemonics()
    solflare_common_outro()


def solflare_common_intro():
    select_solflare_web()
    handle_new_window()
    driver.instance.maximize_window()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, create_new_wallet_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, copy_mnemonic_button))).click()


def solflare_common_outro():
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, continue_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, continue_button))).click()
    handle_default_window()
    select_solflare_web()
    handle_second_window()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, allow_button))).click()
    handle_default_window()


def mnemonic_reconnect_for_recipient():
    handle_new_window()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, already_have_wallet_button))).click()
    reconnect_recipient_mnemonic()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, continue_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, continue_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, advanced_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, select_right_wallet))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, continue_button))).click()
    handle_default_window()


def mnemonic_reconnect_for_sender():
    handle_new_window()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, already_have_wallet_button))).click()
    reconnect_sender_mnemonic()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, continue_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, continue_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, advanced_button))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, select_right_wallet))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, continue_button))).click()
    handle_default_window()

def get_recipient_mnemonic():
    one = '//*[@data-index="1"]'
    one_mnemonic = driver.instance.find_element(By.XPATH, one).text
    with open('./reporting/wallets/recipient/one.txt', 'w') as file:
        file.write(one_mnemonic)
    two = '//*[@data-index="2"]'
    two_mnemonic = driver.instance.find_element(By.XPATH, two).text
    with open('./reporting/wallets/recipient/two.txt', 'w') as file:
        file.write(two_mnemonic)
    three = '//*[@data-index="3"]'
    three_mnemonic = driver.instance.find_element(By.XPATH, three).text
    with open('./reporting/wallets/recipient/three.txt', 'w') as file:
        file.write(three_mnemonic)
    four = '//*[@data-index="4"]'
    four_mnemonic = driver.instance.find_element(By.XPATH, four).text
    with open('./reporting/wallets/recipient/four.txt', 'w') as file:
        file.write(four_mnemonic)
    five = '//*[@data-index="5"]'
    five_mnemonic = driver.instance.find_element(By.XPATH, five).text
    with open('./reporting/wallets/recipient/five.txt', 'w') as file:
        file.write(five_mnemonic)
    six = '//*[@data-index="6"]'
    six_mnemonic = driver.instance.find_element(By.XPATH, six).text
    with open('./reporting/wallets/recipient/six.txt', 'w') as file:
        file.write(six_mnemonic)
    seven = '//*[@data-index="7"]'
    seven_mnemonic = driver.instance.find_element(By.XPATH, seven).text
    with open('./reporting/wallets/recipient/seven.txt', 'w') as file:
        file.write(seven_mnemonic)
    eight = '//*[@data-index="8"]'
    eight_mnemonic = driver.instance.find_element(By.XPATH, eight).text
    with open('./reporting/wallets/recipient/eight.txt', 'w') as file:
        file.write(eight_mnemonic)
    nine = '//*[@data-index="9"]'
    nine_mnemonic = driver.instance.find_element(By.XPATH, nine).text
    with open('./reporting/wallets/recipient/nine.txt', 'w') as file:
        file.write(nine_mnemonic)
    ten = '//*[@data-index="10"]'
    ten_mnemonic = driver.instance.find_element(By.XPATH, ten).text
    with open('./reporting/wallets/recipient/ten.txt', 'w') as file:
        file.write(ten_mnemonic)
    eleven = '//*[@data-index="11"]'
    eleven_mnemonic = driver.instance.find_element(By.XPATH, eleven).text
    with open('./reporting/wallets/recipient/eleven.txt', 'w') as file:
        file.write(eleven_mnemonic)
    twelve = '//*[@data-index="12"]'
    twelve_mnemonic = driver.instance.find_element(By.XPATH, twelve).text
    with open('./reporting/wallets/recipient/twelve.txt', 'w') as file:
        file.write(twelve_mnemonic)


def read_recipient_mnemonic_one():
    with open('./reporting/wallets/recipient/one.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_recipient_mnemonic_two():
    with open('./reporting/wallets/recipient/two.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_recipient_mnemonic_three():
    with open('./reporting/wallets/recipient/three.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_recipient_mnemonic_four():
    with open('./reporting/wallets/recipient/four.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_recipient_mnemonic_five():
    with open('./reporting/wallets/recipient/five.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_recipient_mnemonic_six():
    with open('./reporting/wallets/recipient/six.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_recipient_mnemonic_seven():
    with open('./reporting/wallets/recipient/seven.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_recipient_mnemonic_eight():
    with open('./reporting/wallets/recipient/eight.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_recipient_mnemonic_nine():
    with open('./reporting/wallets/recipient/nine.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_recipient_mnemonic_ten():
    with open('./reporting/wallets/recipient/ten.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_recipient_mnemonic_eleven():
    with open('./reporting/wallets/recipient/eleven.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_recipient_mnemonic_twelve():
    with open('./reporting/wallets/recipient/twelve.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def collect_recipient_mnemonics():
    one = 'mnemonic-input-0'
    two = 'mnemonic-input-1'
    three = 'mnemonic-input-2'
    four = 'mnemonic-input-3'
    five = 'mnemonic-input-4'
    six = 'mnemonic-input-5'
    seven = 'mnemonic-input-6'
    eight = 'mnemonic-input-7'
    nine = 'mnemonic-input-8'
    ten = 'mnemonic-input-9'
    eleven = 'mnemonic-input-10'
    twelve = 'mnemonic-input-11'
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, one))). \
        send_keys(read_recipient_mnemonic_one())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, two))). \
        send_keys(read_recipient_mnemonic_two())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, three))). \
        send_keys(read_recipient_mnemonic_three())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, four))). \
        send_keys(read_recipient_mnemonic_four())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, five))). \
        send_keys(read_recipient_mnemonic_five())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, six))). \
        send_keys(read_recipient_mnemonic_six())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, seven))). \
        send_keys(read_recipient_mnemonic_seven())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, eight))). \
        send_keys(read_recipient_mnemonic_eight())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, nine))). \
        send_keys(read_recipient_mnemonic_nine())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, ten))). \
        send_keys(read_recipient_mnemonic_ten())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, eleven))). \
        send_keys(read_recipient_mnemonic_eleven())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, twelve))). \
        send_keys(read_recipient_mnemonic_twelve())


def get_sender_mnemonic():
    one = '//*[@data-index="1"]'
    one_mnemonic = driver.instance.find_element(By.XPATH, one).text
    with open('./reporting/wallets/sender/one.txt', 'w') as file:
        file.write(one_mnemonic)
    two = '//*[@data-index="2"]'
    two_mnemonic = driver.instance.find_element(By.XPATH, two).text
    with open('./reporting/wallets/sender/two.txt', 'w') as file:
        file.write(two_mnemonic)
    three = '//*[@data-index="3"]'
    three_mnemonic = driver.instance.find_element(By.XPATH, three).text
    with open('./reporting/wallets/sender/three.txt', 'w') as file:
        file.write(three_mnemonic)
    four = '//*[@data-index="4"]'
    four_mnemonic = driver.instance.find_element(By.XPATH, four).text
    with open('./reporting/wallets/sender/four.txt', 'w') as file:
        file.write(four_mnemonic)
    five = '//*[@data-index="5"]'
    five_mnemonic = driver.instance.find_element(By.XPATH, five).text
    with open('./reporting/wallets/sender/five.txt', 'w') as file:
        file.write(five_mnemonic)
    six = '//*[@data-index="6"]'
    six_mnemonic = driver.instance.find_element(By.XPATH, six).text
    with open('./reporting/wallets/sender/six.txt', 'w') as file:
        file.write(six_mnemonic)
    seven = '//*[@data-index="7"]'
    seven_mnemonic = driver.instance.find_element(By.XPATH, seven).text
    with open('./reporting/wallets/sender/seven.txt', 'w') as file:
        file.write(seven_mnemonic)
    eight = '//*[@data-index="8"]'
    eight_mnemonic = driver.instance.find_element(By.XPATH, eight).text
    with open('./reporting/wallets/sender/eight.txt', 'w') as file:
        file.write(eight_mnemonic)
    nine = '//*[@data-index="9"]'
    nine_mnemonic = driver.instance.find_element(By.XPATH, nine).text
    with open('./reporting/wallets/sender/nine.txt', 'w') as file:
        file.write(nine_mnemonic)
    ten = '//*[@data-index="10"]'
    ten_mnemonic = driver.instance.find_element(By.XPATH, ten).text
    with open('./reporting/wallets/sender/ten.txt', 'w') as file:
        file.write(ten_mnemonic)
    eleven = '//*[@data-index="11"]'
    eleven_mnemonic = driver.instance.find_element(By.XPATH, eleven).text
    with open('./reporting/wallets/sender/eleven.txt', 'w') as file:
        file.write(eleven_mnemonic)
    twelve = '//*[@data-index="12"]'
    twelve_mnemonic = driver.instance.find_element(By.XPATH, twelve).text
    with open('./reporting/wallets/sender/twelve.txt', 'w') as file:
        file.write(twelve_mnemonic)


def read_sender_mnemonic_one():
    with open('./reporting/wallets/sender/one.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_sender_mnemonic_two():
    with open('./reporting/wallets/sender/two.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_sender_mnemonic_three():
    with open('./reporting/wallets/sender/three.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_sender_mnemonic_four():
    with open('./reporting/wallets/sender/four.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_sender_mnemonic_five():
    with open('./reporting/wallets/sender/five.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_sender_mnemonic_six():
    with open('./reporting/wallets/sender/six.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_sender_mnemonic_seven():
    with open('./reporting/wallets/sender/seven.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_sender_mnemonic_eight():
    with open('./reporting/wallets/sender/eight.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_sender_mnemonic_nine():
    with open('./reporting/wallets/sender/nine.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_sender_mnemonic_ten():
    with open('./reporting/wallets/sender/ten.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_sender_mnemonic_eleven():
    with open('./reporting/wallets/sender/eleven.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def read_sender_mnemonic_twelve():
    with open('./reporting/wallets/sender/twelve.txt', 'r') as file:
        mnemonic = file.read()
    return mnemonic


def collect_sender_mnemonics():
    one = 'mnemonic-input-0'
    two = 'mnemonic-input-1'
    three = 'mnemonic-input-2'
    four = 'mnemonic-input-3'
    five = 'mnemonic-input-4'
    six = 'mnemonic-input-5'
    seven = 'mnemonic-input-6'
    eight = 'mnemonic-input-7'
    nine = 'mnemonic-input-8'
    ten = 'mnemonic-input-9'
    eleven = 'mnemonic-input-10'
    twelve = 'mnemonic-input-11'
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, one))). \
        send_keys(read_sender_mnemonic_one())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, two))). \
        send_keys(read_sender_mnemonic_two())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, three))). \
        send_keys(read_sender_mnemonic_three())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, four))). \
        send_keys(read_sender_mnemonic_four())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, five))). \
        send_keys(read_sender_mnemonic_five())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, six))). \
        send_keys(read_sender_mnemonic_six())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, seven))). \
        send_keys(read_sender_mnemonic_seven())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, eight))). \
        send_keys(read_sender_mnemonic_eight())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, nine))). \
        send_keys(read_sender_mnemonic_nine())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, ten))). \
        send_keys(read_sender_mnemonic_ten())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, eleven))). \
        send_keys(read_sender_mnemonic_eleven())
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.ID, twelve))). \
        send_keys(read_sender_mnemonic_twelve())


def reconnect_recipient_mnemonic():
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, textarea))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, textarea))). \
        send_keys(" ".join([read_recipient_mnemonic_one(), read_recipient_mnemonic_two(), read_recipient_mnemonic_three(), read_recipient_mnemonic_four(), read_recipient_mnemonic_five(), read_recipient_mnemonic_six(), read_recipient_mnemonic_seven(), read_recipient_mnemonic_eight(), read_recipient_mnemonic_nine(), read_recipient_mnemonic_ten(), read_recipient_mnemonic_eleven(), read_recipient_mnemonic_twelve()]))


def reconnect_sender_mnemonic():
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, textarea))).click()
    WebDriverWait(driver.instance, 10).until(ec.element_to_be_clickable((By.XPATH, textarea))). \
        send_keys(" ".join(
        [read_sender_mnemonic_one(), read_sender_mnemonic_two(), read_sender_mnemonic_three(),
         read_sender_mnemonic_four(), read_sender_mnemonic_five(),read_sender_mnemonic_six(), read_sender_mnemonic_seven(), read_sender_mnemonic_eight(), read_sender_mnemonic_nine(), read_sender_mnemonic_ten(), read_sender_mnemonic_eleven(), read_recipient_mnemonic_twelve() ]))






