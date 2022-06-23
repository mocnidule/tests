import unittest
import pytest
from flaky import flaky
from driver import driver
from helpers.driver_helpers import tear_down_and_collect
from helpers.app_helpers import sender_create_contract_and_recipient_assert_contract_streaming, sender_use_minutes, \
    sender_use_hours, sender_use_random_date_and_time, sender_fill_big_amount_contract_details, \
    sender_create_contract_and_recipient_assert_contract_vesting, set_random_cliff, \
    sender_select_autowithdrawal, sender_fill_standard_contract_details, cancel_contract, \
    fill_standard_details_for_streaming, select_both_can_cancel, sender_go_vesting_select_devnet_connect_wallet, \
    sender_go_streaming_select_devnet_connect_wallet, click_add_recipient_100_times, fill_batch_details, \
    sender_create_vesting_contract, sender_create_streaming_contract, click_to_all_streams_page
from time import sleep


@pytest.mark.devs
@flaky(max_runs=1, min_passes=1)
class test_dev(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.initialize()

    # def test_vesting_batch(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     click_add_recipient_100_times()
    #     fill_batch_details()
    #     sender_use_random_date_and_time()
    #     sender_create_vesting_contract()
    #
    # def test_vesting_minutes(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_random_date_and_time()
    #     sender_use_minutes()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_and_recipient_cancel(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_random_date_and_time()
    #     select_both_can_cancel()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #     cancel_contract()
    #
    # def test_vesting_and_sender_set_cliff(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_use_random_date_and_time()
    #     set_random_cliff()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_sender_select_auto_withdraw(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_standard_contract_details()
    #     sender_select_autowithdrawal()
    #     sender_create_contract_and_recipient_assert_contract_vesting()
    #
    # def test_vesting_sender_big_number(self):
    #     sender_go_vesting_select_devnet_connect_wallet()
    #     sender_fill_big_amount_contract_details()
    #     sender_create_contract_and_recipient_assert_contract_vesting()

    # def test_streaming_top_up(self):
    #     sender_go_streaming_select_devnet_connect_wallet()
    #     fill_standard_details_for_streaming()
    #     sender_create_streaming_contract()

    # def test_streaming_sender_transfer(self):
    #     pass
    #
    # def test_streaming_recipient_manual_withdrawal(self):
    #     pass
    #
    def test_streaming_search_and_filter_contract(self):
        sender_go_streaming_select_devnet_connect_wallet()
        fill_standard_details_for_streaming()
        sender_create_streaming_contract()
        click_to_all_streams_page()
        sleep(200)

    # def test_streaming_minutes(self):
    #     sender_go_streaming_select_devnet_connect_wallet()
    #     fill_standard_details_for_streaming()
    #     sender_create_contract_and_recipient_assert_contract_streaming()

    @classmethod
    def tearDown(cls):
        tear_down_and_collect()

