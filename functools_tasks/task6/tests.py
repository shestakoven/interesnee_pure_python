from datetime import datetime

from functools_tasks.task6.task6 import calculate_datetime

import pytest


@pytest.mark.parametrize('test_date, add_hours, result', [
    (datetime(2019, 6, 27, 11, 30), 26, '2019-06-28 13:30'),
    (datetime(2019, 6, 27, 11, 30), -5, '2019-06-27 06:30'),
    (datetime(2019, 6, 27, 11, 30), 24, '2019-06-28 11:30'),
    (datetime(2019, 6, 27, 11, 30), 0, '2019-06-27 11:30'),
])
def test_calculate_datetime_returns_sum_right(test_date, add_hours, result):
    test_format = '%Y-%m-%d %H:%M'
    assert result == calculate_datetime(test_date, test_format,
                                        hours=add_hours)
