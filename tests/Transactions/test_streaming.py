import unittest
import pytest
from flaky import flaky
from driver import driver
from helpers.driver_helpers import tear_down_and_collect
from helpers.app_helpers import sender_use_seconds, \
    sender_create_contract_and_recipient_assert_contract_streaming, sender_use_minutes, sender_use_hours, \
    sender_use_days, sender_use_weeks, sender_use_months, sender_use_years, sender_create_vesting_contract, \
    sender_top_up_while_streaming, sender_top_up_before_stream_started, \
    transfer_contract,\
    recipient_withdraw_partial, recipient_withdraw_full


@pytest.mark.all
@pytest.mark.transactions
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
class test_streaming(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.initialize()

    def test_streaming_seconds(self):
        pass

    def test_streaming_minutes(self):
        pass

    def test_streaming_hours(self):
        pass

    def test_streaming_days(self):
        pass

    def test_streaming_weeks(self):
        pass

    def test_streaming_months(self):
        pass

    def test_streaming_years(self):
        pass

    def test_streaming_top_up_while_streaming(self):
        pass

    def test_streaming_top_up_before_stream_started(self):
        pass

    def test_streaming_and_sender_cancel(self):
        pass

    def test_streaming_and_recipient_cancel(self):
        pass

    def test_streaming_and_sender_transfer(self):
        pass

    def test_streaming_and_recipient_transfer(self):
        pass

    def test_streaming_and_recipient_withdraw_partial(self):
        pass

    def test_streaming_and_recipient_withdraw_full(self):
        pass

    def test_streaming_and_all_can_cancel_and_transfer(self):
        pass

    def test_streaming_and_non_can_cancel_and_transfer(self):
        pass

    def test_streaming_recipient_withdraw_and_sender_cancel(self):
        pass

    def test_streaming_recipient_transfer_and_sender_cancel(self):
        pass

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

    def test_streaming_big_number(self):
        pass

    @classmethod
    def tearDown(cls):
        tear_down_and_collect()