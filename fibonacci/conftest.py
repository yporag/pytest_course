import pytest
from datetime import datetime, timedelta
from typing import Callable


@pytest.fixture
def time_tracker():
    start_time = datetime.now()
    yield

    end_time = datetime.now()
    total_run_time = end_time - start_time

    print(f"\ntotal_run_time = {total_run_time}")


class PerformanceException(Exception):
    def __init__(self, runtime: timedelta, limit: timedelta):
        self.runtime = runtime
        self.limit = limit

    def __str__(self) -> str:
        return f"Performance test exceeded time limit. runtime ={self.runtime.total_seconds()}, limit = {self.limit.total_seconds()}"


def track_performance(method: Callable, runtime_limit=timedelta(seconds=2)):
    def run_function_and_validate_runtime(*args, **kw):
        start_time = datetime.now()
        result = method(*args, **kw)

        end_time = datetime.now()
        total_run_time = end_time - start_time

        print(f"\ntotal_run_time = {total_run_time.total_seconds}")

        if total_run_time > runtime_limit:
            raise PerformanceException(runtime=total_run_time, limit=runtime_limit)

        return result

    return run_function_and_validate_runtime
