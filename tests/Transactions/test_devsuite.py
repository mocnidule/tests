import unittest
import pytest
from flaky import flaky
from driver import driver
from helpers.driver_helpers import tear_down_and_collect
from helpers.app_helpers import sender_use_seconds, create_recipient_and_sender_fill_details_for_streaming, \
    sender_create_contract_and_recipient_assert_contract_streaming, sender_use_minutes, sender_use_hours, \
    sender_use_days, sender_use_weeks, sender_use_months, sender_use_years, sender_create_contract, \
    sender_top_up_while_streaming, sender_top_up_before_stream_started, sender_cancel_contract, \
    all_can_transfer_and_cancel, sender_transfer_contract, recipient_cancel_contract, transfer_contract,\
    recipient_withdraw_partial, recipient_withdraw_full, non_can_cancel_and_transfer, reconnect_sender, \
    create_recipient_and_sender_fill_details_for_vesting, sender_use_random_date_and_time, \
    sender_create_contract_and_recipient_assert_contract_vesting, set_random_cliff, click_toggle, \
    sender_select_autowithdrawal, recipient_wait_for_autowithdrawal, go_to_vesting_and_assert_page_is_loaded, \
    connect_senders_wallet, connect_recipients_wallet, sender_fill_standard_contract_details, cancel_contract, \
    click_on_stream_tab, go_to_stream_and_assert_page_is_loaded, fill_standard_details_for_streaming, withdraw_contract


@pytest.mark.devs
@flaky(max_runs=2, min_passes=1)
class test_devsuite(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.initialize()

    def test_vesting_minutes(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        sender_fill_standard_contract_details()
        sender_use_random_date_and_time()
        sender_use_minutes()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_and_recipient_cancel(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        sender_fill_standard_contract_details()
        all_can_transfer_and_cancel()
        sender_create_contract_and_recipient_assert_contract_vesting()
        cancel_contract()

    def test_vesting_and_sender_set_cliff(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        sender_fill_standard_contract_details()
        sender_use_random_date_and_time()
        set_random_cliff()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_streaming_years(self):
        go_to_stream_and_assert_page_is_loaded()
        connect_senders_wallet()
        fill_standard_details_for_streaming()
        sender_use_years()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_vesting_sender_select_autowithdrawal(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        sender_fill_standard_contract_details()
        sender_select_autowithdrawal()
        sender_create_contract_and_recipient_assert_contract_vesting()
        recipient_wait_for_autowithdrawal()

    @classmethod
    def tearDown(cls):
        tear_down_and_collect()

