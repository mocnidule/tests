import unittest
import pytest
from flaky import flaky
from driver import driver
from helpers.driver_helpers import tear_down_and_collect
from helpers.app_helpers import sender_use_seconds, \
    sender_create_contract_and_recipient_assert_contract_streaming, sender_use_minutes, sender_use_hours, \
    sender_use_days, sender_use_weeks, sender_use_months, sender_use_years, sender_create_vesting_contract, \
    sender_top_up_while_streaming, sender_top_up_before_stream_started, \
    sender_use_random_date_and_time, sender_fill_big_amount_contract_details, \
    sender_create_contract_and_recipient_assert_contract_vesting, set_random_cliff, click_toggle, \
    sender_select_autowithdrawal, recipient_wait_for_autowithdrawal, go_to_vesting_and_assert_page_is_loaded, \
    connect_senders_wallet, connect_recipients_wallet, sender_fill_standard_contract_details, cancel_contract, \
    click_on_stream_tab, go_to_stream_and_assert_page_is_loaded, fill_standard_details_for_streaming, withdraw_contract, \
    select_devnet, select_both_can_cancel


@pytest.mark.devs
@flaky(max_runs=2, min_passes=1)
class test_devsuite(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.initialize()

    def test_vesting_minutes(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        select_devnet()
        sender_fill_standard_contract_details()
        sender_use_random_date_and_time()
        sender_use_minutes()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_and_recipient_cancel(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        select_devnet()
        sender_fill_standard_contract_details()
        select_both_can_cancel()
        sender_create_contract_and_recipient_assert_contract_vesting()
        cancel_contract()

    def test_vesting_and_sender_set_cliff(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        select_devnet()
        sender_fill_standard_contract_details()
        sender_use_random_date_and_time()
        set_random_cliff()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_streaming_hours(self):
        go_to_stream_and_assert_page_is_loaded()
        connect_senders_wallet()
        select_devnet()
        sender_use_hours()
        fill_standard_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_vesting_sender_select_autowithdrawal(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        select_devnet()
        sender_fill_standard_contract_details()
        sender_select_autowithdrawal()
        sender_create_contract_and_recipient_assert_contract_vesting()

    def test_vesting_sender_big_number(self):
        go_to_vesting_and_assert_page_is_loaded()
        connect_senders_wallet()
        select_devnet()
        sender_fill_big_amount_contract_details()
        sender_create_contract_and_recipient_assert_contract_vesting()

    @classmethod
    def tearDown(cls):
        tear_down_and_collect()

