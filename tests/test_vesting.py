import pytest
from flaky import flaky
from helpers.global_helpers import *


@pytest.mark.vestingx
@flaky(max_runs=2, min_passes=1)
def test_vesting_seconds(setup):
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


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_minutes(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    use_random_date_and_time()
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


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_hours(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    use_random_date_and_time()
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


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_days(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    use_random_date_and_time()
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


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_months(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    use_random_date_and_time()
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


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_years(setup):
    connect_sender_to_app()
    click_on_vesting_tab()
    use_random_date_and_time()
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

#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_and_sender_cancel(setup):
#     pass
#
#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_and_recipient_cancel(setup):
#     pass
#
#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_and_sender_transfer(setup):
#     pass
#
#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_and_recipient_transfer(setup):
#     pass
#
#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_big_number(setup):
#     pass
#
#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_and_recipient_withdraw(setup):
#     pass
#
#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_and_auto_withdraw(setup):
#     pass
#
#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_and_email_notification(setup):
#     pass
#
#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_and_add_referral(setup):
#     pass
#
#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_bulk(setup):
#     pass
#
#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_upload_csv(setup):
#     pass
#
#
# @pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
# def test_vesting_with_cliff(setup):
#     pass