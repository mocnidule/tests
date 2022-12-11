import pytest
from flaky import flaky
from helpers.global_helpers import *
from pages.new_payment_page import fill_standard_details_for_payment, create_payment_contract


@pytest.mark.all
@pytest.mark.smoke
@flaky(max_runs=1, min_passes=1)
def test_vesting(setup):
    connect_sender_to_app()
    select_new_stream()
    enter_standard_contract_details()
    sender_send_email()
    explicit_wait(5)
    click_continue_button()
    click_create_stream()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    explicit_wait(15)
