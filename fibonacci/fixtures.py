import pytest
from datetime import datetime


@pytest.fixture
def time_tracker():
    start_time = datetime.now()
    yield

    end_time = datetime.now()
    total_run_time = end_time - start_time

    print(f"\ntotal_run_time = {total_run_time}")
