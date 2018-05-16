import traces
from datetime import datetime

def test_quickstart():
    time_series = traces.TimeSeries()
    time_series[datetime(2042, 2, 1,  6,  0,  0)] = 0  # 6:00:00am
    time_series[datetime(2042, 2, 1,  7, 45, 56)] = 1  # 7:45:56am
    time_series[datetime(2042, 2, 1,  8, 51, 42)] = 0  # 8:51:42am
    time_series[datetime(2042, 2, 1, 12,  3, 56)] = 1  # 12:03:56am
    time_series[datetime(2042, 2, 1, 12,  7, 13)] = 0  # 12:07:13am

    assert time_series[datetime(2042, 2, 1, 11,  0, 0)] == 0

    distribution = time_series.distribution(
        start=datetime(2042, 2, 1,  6,  0,  0),  # 6:00am
        end=datetime(2042, 2, 1,  13,  0,  0)   # 1:00pm
    )

    assert distribution[1] == 0.16440476190476191
