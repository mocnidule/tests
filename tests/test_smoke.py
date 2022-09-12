import pytest
from flaky import flaky
from helpers.global_helpers import *
from pages.new_payment_page import fill_standard_details_for_payment, create_payment_contract


@pytest.mark.all
@pytest.mark.smokex
@flaky(max_runs=2, min_passes=1)
def test_vesting(setup):
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
@pytest.mark.smoke
@flaky(max_runs=1, min_passes=1)
def test_payment(setup):
    connect_sender_to_app()
    click_on_payment_tab()
    fill_standard_details_for_payment()
    create_payment_contract()
    approve_in_wallet()
    handle_default_window()
    wait_transaction_confirmed_alert()
    connect_recipient_wallet()
    click_on_payment_tab()
    select_devnet()
    click_dropdown_menu()
    click_toggle()
    find_contract_and_assert()
    transfer_contract()
