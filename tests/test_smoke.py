import pytest
from flaky import flaky
from helpers.global_helpers import *


@pytest.mark.all
@pytest.mark.smoke
@flaky(max_runs=1, min_passes=1)
def test_vesting_solana(setup):
    handle_new_window()
    driver.instance.close()
    handle_default_window()
    connect_sender_to_solana()
    select_new_stream()
    enter_standard_contract_details()
    explicit_wait(5)
    click_continue_button()
    click_create_stream()
    approve_in_wallet()
    handle_default_window()
    wait_stream_created_modal()


# @pytest.mark.all
# @pytest.mark.smoke
# @flaky(max_runs=1, min_passes=1)
# def test_vesting_aptos(setup):
#     handle_default_window()
#     enter_password_and_submit()
#     select_aptos()
#     connect_sender_on_aptos()
#     select_new_stream()
#     select_aptos_token_and_fill_details()
#     disable_aw()
#     click_continue_button()
#     click_create_stream()
#     handle_second_window()
#     click(driver.instance, By.XPATH, '//button[contains(text(),"Approve")]')
#     explicit_wait(3)
#     handle_default_window()
#     handle_second_window()
#     click(driver.instance, By.XPATH, '//button[contains(text(),"Sign")]')
#     handle_default_window()
#     wait_stream_created_modal()

