import unittest
import pytest
from flaky import flaky
from driver import driver
from helpers.driver_helpers import tear_down_and_collect
from helpers.app_helpers import sender_use_seconds, create_recipient_and_sender_fill_details_for_streaming, \
    sender_create_contract_and_recipient_assert_contract_streaming, sender_use_minutes, sender_use_hours, \
    sender_use_days, sender_use_weeks, sender_use_months, sender_use_years, sender_create_vesting_contract, \
    sender_top_up_while_streaming, sender_top_up_before_stream_started, sender_cancel_contract, \
    all_can_transfer_and_cancel, sender_transfer_contract, recipient_cancel_contract, transfer_contract,\
    recipient_withdraw_partial, recipient_withdraw_full, non_can_cancel_and_transfer, reconnect_sender


@pytest.mark.all
@pytest.mark.transactions
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
class test_streaming(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.initialize()

    def test_streaming_seconds(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_use_seconds()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_minutes(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_use_minutes()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_hours(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_use_hours()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_days(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_use_days()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_weeks(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_use_weeks()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_months(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_use_months()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_years(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_use_years()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_top_up_while_streaming(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_use_minutes()
        sender_create_vesting_contract()
        sender_top_up_while_streaming()

    def test_streaming_top_up_before_stream_started(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_create_vesting_contract()
        sender_top_up_before_stream_started()

    def test_streaming_and_sender_cancel(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_create_vesting_contract()
        sender_cancel_contract()

    def test_streaming_and_recipient_cancel(self):
        create_recipient_and_sender_fill_details_for_streaming()
        all_can_transfer_and_cancel()
        sender_create_contract_and_recipient_assert_contract_streaming()
        recipient_cancel_contract()

    def test_streaming_and_sender_transfer(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_create_vesting_contract()
        sender_transfer_contract()

    def test_streaming_and_recipient_transfer(self):
        create_recipient_and_sender_fill_details_for_streaming()
        all_can_transfer_and_cancel()
        sender_create_contract_and_recipient_assert_contract_streaming()
        transfer_contract()

    def test_streaming_and_recipient_withdraw_partial(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()
        recipient_withdraw_partial()

    def test_streaming_and_recipient_withdraw_full(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()
        recipient_withdraw_full()

    def test_streaming_and_all_can_cancel_and_transfer(self):
        create_recipient_and_sender_fill_details_for_streaming()
        all_can_transfer_and_cancel()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_and_non_can_cancel_and_transfer(self):
        create_recipient_and_sender_fill_details_for_streaming()
        non_can_cancel_and_transfer()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_recipient_withdraw_and_sender_cancel(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()
        recipient_withdraw_partial()
        reconnect_sender()
        sender_cancel_contract()

    def test_streaming_recipient_transfer_and_sender_cancel(self):
        create_recipient_and_sender_fill_details_for_streaming()
        all_can_transfer_and_cancel()
        sender_create_contract_and_recipient_assert_contract_streaming()
        transfer_contract()
        reconnect_sender()
        sender_cancel_contract()

    def test_streaming_start_date_in_the_past(self):
        pass

    def test_streaming_negative_amount(self):
        pass

    def test_streaming_amount_less_than_in_the_wallet(self):
        pass

    def test_streaming_recipient_cancel_if_sender_not_selected(self):
        pass

    def test_streaming_recipient_transfer_if_sender_not_selected(self):
        pass

    def test_streaming_without_any_input(self):
        pass

    def test_streaming_sender_transfer_to_himself(self):
        pass

    def test_streaming_recipient_transfer_to_himself(self):
        pass

    def test_streaming_recipient_withdraw_more_than_available(self):
        pass

    def test_streaming_more_amount_than_deposited(self):
        pass

    @classmethod
    def tearDown(cls):
        tear_down_and_collect()