import pytest
from flaky import flaky
from pages.new_payment_page import *


@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_seconds(setup):
    connect_sender_to_app()
    click_on_payment_tab()
    fill_standard_details_for_payment()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()



@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_minutes(setup):
    connect_sender_to_app()
    click_on_payment_tab()
    fill_standard_details_for_payment()
    use_minutes()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_hours(setup):
    connect_sender_to_app()
    click_on_payment_tab()
    fill_standard_details_for_payment()
    use_hours()
    sender_send_email()
    create_payment_contract()
    approve_in_wallet()
    additional_approve_in_wallet()
    handle_default_window()
    email_alert_success()
    find_contract_and_assert()


@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_days(setup):
    pass


@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_weeks(setup):
    pass


@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_months(setup):
    pass


@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_years(setup):
    pass


@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_and_sender_cancel(setup):
    pass


@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_and_recipient_cancel(setup):
    pass


@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_and_sender_transfer(setup):
    pass


@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
def test_streaming_and_recipient_transfer(setup):
    pass