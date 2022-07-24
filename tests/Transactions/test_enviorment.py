import pytest
from flaky import flaky

from helpers.app_helpers import use_minutes, \
    use_random_date_and_time, enter_standard_contract_details, cancel_contract, \
    select_both_can_cancel, \
    create_vesting_contract_and_assert, sender_create_payment_contract, find_contract_and_assert, select_devnet, \
    use_months, transfer_contract, select_both_can_transfer, fill_standard_details_for_streaming, \
    click_on_payment_tab, enter_password_and_submit
from helpers.driver_helpers import tear_down
from pages.solflare_wallet import connect_sender_wallet, connect_recipient_wallet


@pytest.mark.smoke
@flaky(max_runs=1, min_passes=1)
def test_vesting_months_cliff_and_cancel(setup):
    enter_password_and_submit()
    connect_sender_wallet()
    select_devnet()
    use_months()
    select_both_can_cancel()
    enter_standard_contract_details()
    use_random_date_and_time()
    create_vesting_contract_and_assert()
    connect_recipient_wallet()
    select_devnet()
    find_contract_and_assert()
    cancel_contract()
    tear_down()


@pytest.mark.smoke
@flaky(max_runs=1, min_passes=1)
def test_streaming_minutes_top_up_and_transfer(setup):
    enter_password_and_submit()
    connect_sender_wallet()
    click_on_payment_tab()
    select_devnet()
    use_minutes()
    select_both_can_transfer()
    fill_standard_details_for_streaming()
    sender_create_payment_contract()
    connect_recipient_wallet()
    click_on_payment_tab()
    select_devnet()
    find_contract_and_assert()
    transfer_contract()
    tear_down()