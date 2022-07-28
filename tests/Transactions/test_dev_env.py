import pytest
from flaky import flaky
from driver import driver
from helpers.app_helpers import use_minutes, \
    use_random_date_and_time, enter_standard_contract_details, cancel_contract, \
    select_both_can_cancel, \
    create_vesting_contract_and_assert, create_payment_contract, find_contract_and_assert, select_devnet, \
    use_months, transfer_contract, select_both_can_transfer, fill_standard_details_for_streaming, \
    click_on_payment_tab, use_seconds, enter_password_and_submit
from pages.solflare_wallet import connect_sender_wallet, connect_recipient_wallet
from driver import driver

@pytest.mark.devnnet
@flaky(max_runs=1, min_passes=1)
def test_vesting_seconds_cliff_and_cancel(setup):
    enter_password_and_submit()
    connect_sender_wallet()
    select_devnet()
    enter_standard_contract_details()
    select_both_can_cancel()
    create_vesting_contract_and_assert()
    driver.instance.refresh()
    connect_recipient_wallet()
    select_devnet()
    find_contract_and_assert()
    cancel_contract()


@pytest.mark.devnnet
@flaky(max_runs=1, min_passes=1)
def test_streaming_minutes_top_up_and_transfer(setup):
    enter_password_and_submit()
    connect_sender_wallet()
    select_devnet()
    click_on_payment_tab()
    use_minutes()
    select_both_can_transfer()
    fill_standard_details_for_streaming()
    create_payment_contract()
    driver.instance.refresh()
    connect_recipient_wallet()
    select_devnet()
    click_on_payment_tab()
    find_contract_and_assert()
    transfer_contract()


@pytest.mark.devnnet
@flaky(max_runs=1, min_passes=1)
def test_bulk_vesting(setup):
    pass