import pytest
from flaky import flaky
from pages.multisig_page import *
from pages.new_payment_page import fill_standard_details_for_payment


@pytest.mark.all
@pytest.mark.multisig
@flaky(max_runs=2, min_passes=1)
def test_create_multi_sig(setup):
    enter_password_and_submit()
    connect_sender_wallet()
    select_devnet()
    go_to_multi_sig_page()
    create_new_multi_sig_wallet()


@pytest.mark.all
@pytest.mark.multisig
@flaky(max_runs=2, min_passes=1)
def test_create_vesting_multi_sig_accept_execute(setup):
    enter_password_and_submit()
    connect_sender_wallet()
    select_devnet()
    go_to_multi_sig_page()
    select_multi_sig()
    go_to_new_vesting_from_multi_sig()
    enter_standard_contract_details()
    click_propose_vesting_contract()
    approve_in_wallet()
    handle_default_window()
    connect_recipient_wallet()
    connect_button_handler()
    handle_default_window()
    select_devnet()
    go_to_multi_sig_page()
    select_multi_sig()
    go_to_proposals_tab()
    find_proposal_and_approve()
    assert_contract_in_streams()


@pytest.mark.all
@pytest.mark.multisig
@flaky(max_runs=2, min_passes=1)
def test_payment_multi_sig_accept_execute(setup):
    enter_password_and_submit()
    connect_sender_wallet()
    select_devnet()
    go_to_multi_sig_page()
    select_multi_sig()
    go_to_new_payment_from_multi_sig()
    fill_standard_details_for_payment()
    click_propose_streaming_contract()
    approve_in_wallet()
    handle_default_window()
    connect_recipient_wallet()
    connect_button_handler()
    handle_default_window()
    select_devnet()
    go_to_multi_sig_page()
    select_multi_sig()
    go_to_proposals_tab()
    find_proposal_and_approve()
    assert_contract_in_streams()


@pytest.mark.all
@pytest.mark.multisig
@flaky(max_runs=2, min_passes=1)
def test_payment_multi_sig_cancel(setup):
    pass


@pytest.mark.all
@pytest.mark.multisig
@flaky(max_runs=2, min_passes=1)
def test_payment_multi_sig_add_remove_member(setup):
    pass