import unittest
import pytest
from flaky import flaky
from driver import driver
from helpers.driver_helpers import tear_down_and_collect
from helpers.app_helpers import sender_use_seconds, \
    sender_create_contract_and_recipient_assert_contract_streaming, sender_use_minutes, sender_use_hours, \
    sender_use_days, sender_use_weeks, sender_use_months, sender_use_years, sender_create_vesting_contract,  \
    transfer_contract,\
    recipient_withdraw_partial, sender_go_streaming_select_devnet_connect_wallet, fill_standard_details_for_streaming


@pytest.mark.all
@pytest.mark.transactions
@pytest.mark.streaming
@flaky(max_runs=2, min_passes=1)
class test_streaming(unittest.TestCase):

    @classmethod
    def setUp(cls):
        driver.initialize()

    def test_streaming_seconds(self):
        sender_go_streaming_select_devnet_connect_wallet()
        sender_use_seconds()
        fill_standard_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_minutes(self):
        sender_go_streaming_select_devnet_connect_wallet()
        sender_use_minutes()
        fill_standard_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_hours(self):
        sender_go_streaming_select_devnet_connect_wallet()
        sender_use_hours()
        fill_standard_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_days(self):
        sender_go_streaming_select_devnet_connect_wallet()
        sender_use_days()
        fill_standard_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_weeks(self):
        sender_go_streaming_select_devnet_connect_wallet()
        sender_use_weeks()
        fill_standard_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_months(self):
        sender_go_streaming_select_devnet_connect_wallet()
        sender_use_months()
        fill_standard_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_years(self):
        sender_go_streaming_select_devnet_connect_wallet()
        sender_use_years()
        fill_standard_details_for_streaming()
        sender_create_contract_and_recipient_assert_contract_streaming()

    def test_streaming_top_up_while_streaming(self):
        sender_go_streaming_select_devnet_connect_wallet()
        fill_standard_details_for_streaming()



    #
    # def test_streaming_top_up_before_stream_started(self):
    #     pass
    #
    # def test_streaming_and_sender_cancel(self):
    #     pass
    #
    # def test_streaming_and_recipient_cancel(self):
    #     pass
    #
    # def test_streaming_and_sender_transfer(self):
    #     pass
    #
    # def test_streaming_and_recipient_transfer(self):
    #     pass
    #
    # def test_streaming_and_recipient_withdraw(self):
    #     pass
    #
    # def test_streaming_and_all_can_cancel_and_transfer(self):
    #     pass
    #
    # def test_streaming_and_non_can_cancel_and_transfer(self):
    #     pass
    #
    # def test_streaming_recipient_transfer_and_sender_cancel(self):
    #     pass
    #
    # def test_streaming_start_date_in_the_past(self):
    #     pass
    #
    # def test_streaming_negative_amount(self):
    #     pass
    #
    # def test_streaming_amount_less_than_in_the_wallet(self):
    #     pass
    #
    # def test_streaming_without_any_input(self):
    #     pass
    #
    # def test_streaming_sender_transfer_to_himself(self):
    #     pass
    #
    # def test_streaming_recipient_transfer_to_himself(self):
    #     pass
    #
    # def test_streaming_recipient_withdraw_more_than_available(self):
    #     pass
    #
    # def test_streaming_more_amount_than_deposited(self):
    #     pass
    #
    # def test_streaming_big_number(self):
    #     pass
    #
    # def test_streaming_autowithdraw(self):
    #     pass
    #
    # def test_streaming_send_email(self):
    #     pass

    @classmethod
    def tearDown(cls):
        tear_down_and_collect()