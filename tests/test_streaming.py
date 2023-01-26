import pytest
from flaky import flaky
from helpers.global_helpers import *
from pages.new_payment_page import fill_standard_details_for_payment, create_payment_contract


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_seconds(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    fill_standard_details_for_payment()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_minutes(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    use_minutes()
    fill_standard_details_for_payment()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_hours(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    use_hours()
    fill_standard_details_for_payment()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_days(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    use_days()
    fill_standard_details_for_payment()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_weeks(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    use_weeks()
    fill_standard_details_for_payment()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_months(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    use_months()
    fill_standard_details_for_payment()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_years(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    use_years()
    fill_standard_details_for_payment()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_and_sender_cancel(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    fill_standard_details_for_payment()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()
    cancel_contract()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_and_recipient_cancel(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    fill_standard_details_for_payment()
    sender_send_email()
    select_both_can_cancel()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    connect_recipient_wallet_on_solana()
    click_on_payment_tab()
    select_devnet()
    find_contract_and_assert()
    cancel_contract()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_and_sender_transfer(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    fill_standard_details_for_payment()
    select_both_can_transfer()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()
    transfer_contract()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_and_recipient_transfer(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    fill_standard_details_for_payment()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    connect_recipient_wallet_on_solana()
    click_on_payment_tab()
    select_devnet()
    find_contract_and_assert()
    transfer_contract()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_and_recipient_withdraw(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    select_frequency_picker()
    click(driver.instance, By.XPATH, minute)
    fill_standard_details_for_payment()
    create_payment_contract()
    approve_in_wallet()
    handle_default_window()
    connect_recipient_wallet_on_solana()
    click_on_payment_tab()
    select_devnet()
    find_contract_and_assert()
    withdraw_contract()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_auto_withdraw(setup):
    connect_sender_to_solana()
    click_on_payment_tab()
    fill_standard_details_for_payment()
    sender_send_email()
    sender_select_auto_withdrawal()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.all
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_and_recipient_top_up(setup):
    pass