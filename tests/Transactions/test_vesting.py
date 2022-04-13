import unittest
import pytest
from flaky import flaky
from driver import driver
from helpers.driver_helpers import tear_down_and_collect
from helpers.app_helpers import \
    sender_create_contract_and_recipient_assert_contract_vesting, sender_use_seconds, sender_use_minutes, \
    sender_use_hours, sender_use_days, sender_use_random_date_and_time, sender_use_weeks, sender_use_months, \
    sender_use_years, sender_create_vesting_contract, transfer_contract, \
    go_to_vesting_and_assert_page_is_loaded, connect_senders_wallet, sender_fill_standard_contract_details, \
    sender_handle_standard_contract, cancel_contract, withdraw_contract, \
    sender_go_vesting_select_devnet_connect_wallet, select_both_can_cancel, select_both_can_transfer, \
    reconnect_sender, sender_transfer_to_self, recipient_transfer_to_self, sender_fill_big_amount_contract_details, \
    approve_button_handler
from pages.app_page import set_random_cliff, \
    sender_use_past_date, assert_stream_in_the_past_error_message, click_create_button, enter_negative_amount, \
    assert_no_negative_amount_error_message, enter_abnormal_amount, assert_not_enough_tokens_error_message, \
    set_past_cliff_date, assert_cliff_should_happen_after_start_error_message, assert_must_have_fields_populated, \
    assert_cant_transfer_stream_to_yourself, \
    withdraw_more_than_available, assert_failed_to_send_transaction_alert, sender_select_autowithdrawal, \
    select_none_can_transfer, sender_send_email


@pytest.mark.all
@pytest.mark.transactions
@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
class test_vesting(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.initialize()

    def test_vesting_seconds(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_use_seconds()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_minutes(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_use_minutes()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_hours(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_use_hours()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_days(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_use_days()
        sender_use_random_date_and_time()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_weeks(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_use_weeks()
        sender_use_random_date_and_time()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_months(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_use_months()
        sender_use_random_date_and_time()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_years(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_use_years()
        sender_use_random_date_and_time()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_and_sender_cancel(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_use_random_date_and_time()
        select_both_can_cancel()
        sender_create_contract_and_recipient_assert_contract_vesting()
        cancel_contract()

    def test_vesting_and_recipient_cancel(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_use_random_date_and_time()
        select_both_can_cancel()
        sender_create_contract_and_recipient_assert_contract_vesting()
        cancel_contract()

    def test_vesting_and_sender_transfer(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        select_both_can_transfer()
        sender_create_vesting_contract()
        transfer_contract()

    def test_vesting_and_recipient_transfer(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        select_both_can_transfer()
        sender_create_contract_and_recipient_assert_contract_vesting()
        transfer_contract()

    def test_vesting_and_recipient_withdraw(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        select_both_can_transfer()
        sender_create_contract_and_recipient_assert_contract_vesting()
        withdraw_contract()

    def test_vesting_and_non_can_cancel_and_transfer(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        select_none_can_transfer()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_and_sender_set_cliff(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_use_random_date_and_time()
        set_random_cliff()
        sender_create_vesting_contract()

    def test_vesting_recipient_transfer_and_sender_cancel(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        select_both_can_transfer()
        sender_use_random_date_and_time()
        sender_create_contract_and_recipient_assert_contract_vesting()
        transfer_contract()
        reconnect_sender()
        cancel_contract()

    def test_vesting_start_date_in_the_past(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        sender_use_past_date()
        click_create_button()
        assert_stream_in_the_past_error_message()

    def test_vesting_negative_amount(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        enter_negative_amount()
        click_create_button()
        assert_no_negative_amount_error_message()

    def test_vesting_more_amount_than_in_the_wallet(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        enter_abnormal_amount()
        click_create_button()
        assert_not_enough_tokens_error_message()

    def test_vesting_cliff_time_before_start_time(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_use_random_date_and_time()
        set_past_cliff_date()
        click_create_button()
        assert_cliff_should_happen_after_start_error_message()

    def test_vesting_without_any_input(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        click_create_button()
        assert_must_have_fields_populated()

    def test_vesting_sender_transfer_to_himself(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        select_both_can_transfer()
        sender_create_vesting_contract()
        sender_transfer_to_self()
        assert_cant_transfer_stream_to_yourself()

    def test_vesting_recipient_transfer_to_himself(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        select_both_can_transfer()
        sender_create_contract_and_recipient_assert_contract_vesting()
        recipient_transfer_to_self()
        assert_cant_transfer_stream_to_yourself()

    def test_vesting_recipient_withdraw_more_than_available(self):
        sender_handle_standard_contract()
        sender_create_contract_and_recipient_assert_contract_vesting()
        withdraw_more_than_available()
        assert_failed_to_send_transaction_alert()

    def test_vesting_sender_select_autowithdrawal(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_select_autowithdrawal()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_big_number(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_big_amount_contract_details()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_send_email(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        sender_send_email()
        click_create_button()
        approve_button_handler()
        approve_button_handler()

    @classmethod
    def tearDown(cls):
        tear_down_and_collect()
