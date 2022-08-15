import pytest
from flaky import flaky
from helpers.global_helpers import *
from pages.solflare_wallet_page import connect_sender_wallet, connect_recipient_wallet


@pytest.mark.mainnet
@flaky(max_runs=1, min_passes=1)
def test_vesting_seconds_set_cliff_and_cancel(setup):
    enter_password_and_submit()
    connect_sender_wallet()
    click_on_vesting_tab()
    enter_mainnet_vesting_contract_details()
    sender_send_email()
    select_both_can_cancel()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    driver.instance.refresh()
    connect_recipient_wallet()
    find_contract_and_assert()
    cancel_contract()


@pytest.mark.mainnet
@flaky(max_runs=1, min_passes=1)
def test_streaming_minutes_top_up_and_transfer(setup):
    enter_password_and_submit()
    connect_sender_wallet()
    click_on_payment_tab()
    use_minutes()
    select_both_can_transfer()
    fill_mainnet_details_for_streaming()
    create_payment_contract()
    connect_recipient_wallet()
    click_on_payment_tab()
    find_contract_and_assert()
    transfer_contract()


# @pytest.mark.mainnet
# @flaky(max_runs=1, min_passes=1)
# def test_bulk_vesting(setup):
#     enter_password_and_submit()
#     connect_sender_wallet()
#     click_on_vesting_tab()
#     click_add_recipient_4_times()
#     fill_batch_details()
#     wait_wallet_connect_alert_to_disappear()
#     click_create_button()
#     approve_transaction_in_solflare()
#     handle_default_window()
#     wait_transaction_confirmed_alert()
