import pytest
from flaky import flaky
from pages.multisig_page import *
from time import sleep


@pytest.mark.multisig
@flaky(max_runs=1, min_passes=1)
def test_create_multi_sig():
    enter_password_and_submit()
    connect_sender_wallet()
    select_devnet()
    go_to_multi_sig_page()
    create_new_multi_sig_wallet()
    sleep(1000)
