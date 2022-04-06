import unittest
import pytest
from flaky import flaky
from driver import driver
from helpers.driver_helpers import tear_down_and_collect
from helpers.app_helpers import \
    sender_create_contract_and_recipient_assert_contract_vesting, sender_use_seconds, sender_use_minutes, \
    sender_use_hours, sender_use_days, sender_use_random_date_and_time, sender_use_weeks, sender_use_months, \
    sender_use_years, sender_create_vesting_contract, transfer_contract, \
    recipient_withdraw_partial, recipient_withdraw_full, decline_then_approve_withdrawal, \
    decline_then_approve_contract_creation, \
    go_to_vesting_and_assert_page_is_loaded, connect_senders_wallet, sender_fill_standard_contract_details, \
    sender_handle_standard_contract, cancel_contract, withdraw_contract, \
    sender_go_vesting_select_devnet_connect_wallet, select_both_can_cancel, select_both_can_transfer

from pages.app_page import set_random_cliff, \
    sender_use_past_date, assert_stream_in_the_past_error_message, click_create_button, enter_negative_amount, \
    assert_no_negative_amount_error_message, enter_abnormal_amount, assert_not_enough_tokens_error_message, \
    set_past_cliff_date, assert_cliff_should_happen_after_start_error_message, assert_must_have_fields_populated, \
    sender_transfer_to_self, assert_cant_transfer_stream_to_yourself, recipient_transfer_to_self, \
    withdraw_more_than_available, assert_failed_to_send_transaction_alert, sender_select_autowithdrawal, \
    recipient_wait_for_autowithdrawal


@pytest.mark.all
@pytest.mark.transactions
@pytest.mark.vesting
# @flaky(max_runs=2, min_passes=1)
class test_vesting(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.initialize()

    # def test_vesting_seconds(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_seconds()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_minutes(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_minutes()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_hours(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_hours()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_days(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_days()
    #     sender_use_random_date_and_time()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_weeks(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_weeks()
    #     sender_use_random_date_and_time()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_months(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_months()
    #     sender_use_random_date_and_time()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_years(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_years()
    #     sender_use_random_date_and_time()
    #     sender_create_contract_and_recipient_assert_contract_vesting()

    # def test_vesting_and_sender_cancel(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_random_date_and_time()
    #     select_both_can_cancel()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #     cancel_contract()
    #
    # def test_vesting_and_recipient_cancel(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_random_date_and_time()
    #     select_both_can_cancel()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #     cancel_contract()
    #
    # def test_vesting_and_sender_transfer(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     select_both_can_transfer()
    #     sender_create_vesting_contract()
    #     transfer_contract()
    #
    # def test_vesting_and_recipient_transfer(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     select_both_can_transfer()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #     transfer_contract()
    #
    def test_vesting_and_recipient_withdraw_partial(self):
        sender_go_vesting_select_devnet_connect_wallet()
        sender_fill_standard_contract_details()
        select_both_can_transfer()
        sender_create_contract_and_recipient_assert_contract_vesting()
        withdraw_contract()
    #
    # def test_vesting_and_recipient_withdraw_full(self):
    #     sender_handle_standard_contract()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #     withdraw_contract()
    #
    # def test_vesting_and_all_can_cancel_and_transfer(self):
    #     sender_handle_standard_contract()
    #     all_can_transfer_and_cancel()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_and_non_can_cancel_and_transfer(self):
    #     sender_handle_standard_contract()
    #     non_can_cancel_and_transfer()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_and_sender_set_cliff(self):
    #     sender_handle_standard_contract()
    #     sender_use_random_date_and_time()
    #     set_random_cliff()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_recipient_withdraw_and_sender_cancel(self):
    #     sender_handle_standard_contract()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #     withdraw_contract()
    #     reconnect_sender()
    #     cancel_contract()
    #
    # def test_vesting_recipient_transfer_and_sender_cancel(self):
    #     sender_handle_standard_contract()
    #     all_can_transfer_and_cancel()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #     transfer_contract()
    #     reconnect_sender()
    #     cancel_contract()
    #
    # def test_vesting_start_date_in_the_past(self):
    #     go_to_vesting_and_assert_page_is_loaded()
    #     connect_senders_wallet()
    #     sender_use_past_date()
    #     click_create_button()
    #     assert_stream_in_the_past_error_message()
    #
    # def test_vesting_negative_amount(self):
    #     go_to_vesting_and_assert_page_is_loaded()
    #     connect_senders_wallet()
    #     enter_negative_amount()
    #     click_create_button()
    #     assert_no_negative_amount_error_message()
    #
    # def test_vesting_more_amount_than_in_the_wallet(self):
    #     go_to_vesting_and_assert_page_is_loaded()
    #     connect_senders_wallet()
    #     enter_abnormal_amount()
    #     click_create_button()
    #     assert_not_enough_tokens_error_message()
    #
    # def test_vesting_recipient_cancel_or_transfer_if_sender_not_select(self):
    #     sender_handle_standard_contract()
    #     non_can_cancel_and_transfer()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_cliff_time_before_start_time(self):
    #     create_recipient_and_sender_fill_details_for_vesting()
    #     sender_use_random_date_and_time()
    #     set_past_cliff_date()
    #     click_create_button()
    #     assert_cliff_should_happen_after_start_error_message()
    #
    # def test_vesting_without_any_input(self):
    #     go_to_vesting_and_assert_page_is_loaded()
    #     connect_senders_wallet()
    #     click_create_button()
    #     assert_must_have_fields_populated()
    #
    # def test_vesting_sender_transfer_to_himself(self):
    #     sender_handle_standard_contract()
    #     sender_create_vesting_contract()
    #     sender_transfer_to_self()
    #     assert_cant_transfer_stream_to_yourself()
    #
    # def test_vesting_recipient_transfer_to_himself(self):
    #     sender_handle_standard_contract()
    #     all_can_transfer_and_cancel()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #     recipient_transfer_to_self()
    #     assert_cant_transfer_stream_to_yourself()
    #
    # def test_vesting_recipient_withdraw_more_than_available(self):
    #     sender_handle_standard_contract()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #     withdraw_more_than_available()
    #     assert_failed_to_send_transaction_alert()
    #
    # def test_vesting_recipient_decline_then_approve_transaction_while_withdrawal(self):
    #     sender_handle_standard_contract()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #     decline_then_approve_withdrawal()
    #
    # def test_vesting_sender_decline_then_approve_transaction_while_create(self):
    #     sender_handle_standard_contract()
    #     decline_then_approve_contract_creation()
    #
    # def test_vesting_sender_select_autowithdrawal(self):
    #     sender_handle_standard_contract()
    #     sender_select_autowithdrawal()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #     recipient_wait_for_autowithdrawal()

    # def test_vesting_big_number(self):
    #     pass

    @classmethod
    def tearDown(cls):
        tear_down_and_collect()
