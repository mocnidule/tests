import unittest
import pytest
from flaky import flaky
from driver import driver
from helpers.driver_helpers import tear_down_and_collect
from helpers.app_helpers import sender_use_seconds, create_recipient_and_sender_fill_details_for_streaming, \
    sender_create_contract_and_recipient_assert_contract_streaming, sender_use_minutes, sender_use_hours, \
    sender_use_days, sender_use_weeks, sender_use_months, sender_use_years, sender_create_contract, \
    sender_top_up_while_streaming, sender_top_up_before_stream_started, sender_cancel_contract, \
    recipient_can_cancel_and_transfer, sender_transfer_contract, recipient_cancel_contract, recipient_transfer_contract,\
    recipient_withdraw_partial, recipient_withdraw_full, non_can_cancel_and_transfer, reconnect_sender, \
    create_recipient_and_sender_fill_details_for_vesting, sender_use_random_date_and_time, \
    sender_create_contract_and_recipient_assert_contract_vesting, set_random_cliff, click_toggle


@pytest.mark.devs
@flaky(max_runs=2, min_passes=1)
class test_devsuite(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.initialize()

    def test_vesting_minutes(self):
        create_recipient_and_sender_fill_details_for_vesting()
        sender_use_random_date_and_time()
        sender_use_minutes()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_and_recipient_cancel(self):
        create_recipient_and_sender_fill_details_for_vesting()
        sender_use_random_date_and_time()
        recipient_can_cancel_and_transfer()
        sender_create_contract_and_recipient_assert_contract_vesting()
        recipient_cancel_contract()

    def test_vesting_and_sender_set_cliff(self):
        create_recipient_and_sender_fill_details_for_vesting()
        sender_use_random_date_and_time()
        set_random_cliff()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_streaming_and_recipient_withdraw_partial(self):
        create_recipient_and_sender_fill_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()
        recipient_withdraw_partial()

    def test_streaming_and_all_can_cancel_and_transfer(self):
        create_recipient_and_sender_fill_details_for_streaming()
        recipient_can_cancel_and_transfer()
        sender_create_contract_and_recipient_assert_contract_streaming()

    @classmethod
    def tearDown(cls):
        tear_down_and_collect()

