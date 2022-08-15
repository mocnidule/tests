from helpers.global_helpers import *


def go_to_multi_sig_page():
    click(driver.instance, By.XPATH, wallet_not_connected_alert)
    click(driver.instance, By.XPATH, wallet_connected_alert)
    click(driver.instance, By.XPATH, multi_sig_page)


def create_new_multi_sig_wallet():
    click(driver.instance, By.XPATH, new_multi_sig_wallet)
    driver.instance.find_element(By.ID, wallet_name).send_keys('Test Multi-sig')
    button = driver.instance.find_element(By.XPATH, add_member)
    for i in range(4):
        button.click()
    driver.instance.find_element(By.ID, member_one).send_keys('HQusf1yxnzwcWBCYZcRRhJnRscng3RQofAVZ5KSBoDPf')
    driver.instance.find_element(By.ID, member_two).send_keys('3dUkYworYstcd1p91PTUPUYLqV7VgJyQri6xybRuKwkA')
    driver.instance.find_element(By.ID, member_three).send_keys('y9ptUGPjYXesub59gLwy2baXBWAbJDHiXLyUzsTA3pY')
    driver.instance.find_element(By.ID, member_four).send_keys('58VuwmGK9UwFuSFsWUoWM4bCyDTKyEKLmACSpxbJV4Np')  # ledger
    click(driver.instance, By.XPATH, create_multi_sig_wallet_button)
    approve_in_wallet()
