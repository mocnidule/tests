from helpers.global_helpers import *


def go_to_multi_sig_page():
    click(driver.instance, By.XPATH, wallet_not_connected_alert)
    click(driver.instance, By.XPATH, wallet_connected_alert)
    click(driver.instance, By.XPATH, multi_sig_page)


def return_to_multi_sig_page():
    scroll_to_top()
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


def go_to_new_vesting_from_multi_sig():
    click(driver.instance, By.XPATH, new_proposal_button)
    click(driver.instance, By.XPATH, vesting_proposal)


def go_to_new_payment_from_multi_sig():
    click(driver.instance, By.XPATH, new_proposal_button)
    click(driver.instance, By.XPATH, stream_proposal)


def go_to_proposals_tab():
    click(driver.instance, By.XPATH, proposals_tab)


def go_to_streams_tab():
    click(driver.instance, By.XPATH, streams_tab_in_multi_sig)


def click_approve_button_in_multi_sig():
    click(driver.instance, By.XPATH, approve_button_multi_sig)


def view_pending_proposals_only():
    click(driver.instance, By.XPATH, pending_proposals_switch)


def select_multi_sig():
    click(driver.instance, By.XPATH, multi_sig_wallet)


def find_proposal_and_approve():
    view_pending_proposals_only()
    actionChains = ActionChains(driver.instance)
    element = WebDriverWait(driver.instance, 20).until(
        ec.visibility_of_element_located((By.XPATH, "((//div[contains(text(),'" + read_contract_title() + "')]/parent::div/parent::div" \
                                                                                    "//button[1]))")))
    actionChains.move_to_element(element).click().perform()
    approve_in_wallet()
    handle_default_window()
    attach_screenshot(driver.instance, 'Contract Proposal Approved')


def click_propose_streaming_contract():
    click(driver.instance, By.XPATH, create_multisig_payment_proposal_button)


def click_propose_vesting_contract():
    element = WebDriverWait(driver.instance, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, '//button[contains(text(),"Create Vesting Proposal")]')))
    actionChains = ActionChains(driver.instance)
    actionChains.move_to_element(element).click().perform()
    click(driver.instance, By.XPATH, '//button[contains(text(),"Create Vesting Proposal")]')


def assert_contract_in_streams():
    wait_invisibility(driver.instance, By.XPATH, spinner)
    scroll_to_top()
    go_to_streams_tab()
    wait_visibility(driver.instance, By.XPATH, "//p[contains(text(),'" + read_contract_title() + "')]")