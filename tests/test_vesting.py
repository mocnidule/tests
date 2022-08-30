import pytest
from flaky import flaky
from helpers.global_helpers import *


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_seconds(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    enter_standard_contract_details()
    sender_send_email()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_minutes(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    set_date()
    use_minutes()
    enter_standard_contract_details()
    sender_send_email()
    select_both_can_cancel()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_hours(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    set_date()
    use_hours()
    enter_standard_contract_details()
    sender_send_email()
    select_both_can_cancel()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_days(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    set_date()
    use_days()
    enter_standard_contract_details()
    sender_send_email()
    select_both_can_cancel()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_months(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    set_date()
    use_months()
    enter_standard_contract_details()
    sender_send_email()
    select_both_can_cancel()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_years(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    set_date()
    use_years()
    enter_standard_contract_details()
    sender_send_email()
    select_both_can_cancel()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_sender_cancel(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    enter_standard_contract_details()
    sender_send_email()
    select_both_can_cancel()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()
    cancel_contract()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_recipient_cancel(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    enter_standard_contract_details()
    sender_send_email()
    select_both_can_cancel()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    connect_recipient_wallet()
    select_devnet()
    find_contract_and_assert()
    cancel_contract()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_sender_transfer(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    enter_standard_contract_details()
    sender_send_email()
    select_both_can_transfer()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()
    transfer_contract()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_recipient_transfer(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    enter_standard_contract_details()
    sender_send_email()
    select_both_can_transfer()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    connect_recipient_wallet()
    select_devnet()
    find_contract_and_assert()
    transfer_contract()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_big_number(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    enter_big_number()
    explicit_wait(2)
    create_contract_title()
    enter_contract_title()
    enter_wallet_address()
    wait_wallet_connect_alert_to_disappear()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_auto_withdraw(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    enter_standard_contract_details()
    sender_send_email()
    sender_select_auto_withdrawal()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_add_referral(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    enter_standard_contract_details()
    sender_send_email()
    add_referral()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_bulk(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    click_add_recipient_4_times()
    fill_batch_details()
    click_create_button()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_with_cliff(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    enter_standard_contract_details()
    set_cliff()
    click_create_button()
    approve_in_wallet()
    handle_default_window()


@pytest.mark.all
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_upload_csv(setup):
    pass  # TO DO
