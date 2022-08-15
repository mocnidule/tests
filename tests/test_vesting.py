import pytest
from flaky import flaky
from helpers.global_helpers import *


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_seconds(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_minutes(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_hours(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_days(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_months(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_years(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_sender_cancel(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_recipient_cancel(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_sender_transfer(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_recipient_transfer(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_big_number(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_recipient_withdraw(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_auto_withdraw(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_email_notification(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_and_add_referral(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_bulk(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_upload_csv(setup):
    pass


@pytest.mark.vesting
@flaky(max_runs=2, min_passes=1)
def test_vesting_with_cliff(setup):
    pass