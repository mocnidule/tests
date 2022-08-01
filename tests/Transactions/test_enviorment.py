import pytest
from flaky import flaky

from helpers.app_helpers import use_minutes, \
    use_random_date_and_time, enter_standard_contract_details, cancel_contract, \
    select_both_can_cancel, \
    create_vesting_contract_and_assert, create_payment_contract, find_contract_and_assert, select_devnet, \
    use_months, transfer_contract, select_both_can_transfer, fill_standard_details_for_streaming, \
    click_on_payment_tab, use_seconds, enter_password_and_submit, enter_mainnet_vesting_contract_details, \
    fill_mainnet_details_for_streaming, click_add_recipient_4_times, fill_batch_details, click_create_button, \
    approve_transaction_in_solflare, handle_default_window, wait_transaction_confirmed_alert, \
    wait_wallet_connect_alert_to_disappear, sender_select_autowithdrawal, click_on_vesting_tab

from pages.solflare_wallet import connect_sender_wallet, connect_recipient_wallet


@pytest.mark.mainnet
@flaky(max_runs=1, min_passes=1)
def test_vesting_seconds_set_cliff_and_cancel(setup):
    enter_password_and_submit()
    connect_sender_wallet()
    click_on_vesting_tab()
    enter_mainnet_vesting_contract_details()
    select_both_can_cancel()
    sender_select_autowithdrawal()
    create_vesting_contract_and_assert()
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


@pytest.mark.mainnet
@flaky(max_runs=1, min_passes=1)
def test_bulk_vesting(setup):
    enter_password_and_submit()
    connect_sender_wallet()
    click_on_vesting_tab()
    click_add_recipient_4_times()
    fill_batch_details()
    wait_wallet_connect_alert_to_disappear()
    click_create_button()
    approve_transaction_in_solflare()
    handle_default_window()
    wait_transaction_confirmed_alert()
