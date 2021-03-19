from datetime import datetime, timedelta


def calculate_datetime(timestamp: datetime, date_format: str, hours: int = 0):
    """Add hours to datetime and return in desired format."""
    date = timestamp + timedelta(hours=hours)
    return date.strftime(date_format)


timestamp = datetime(2019, 6, 27, 11, 30)
print(calculate_datetime(timestamp, '%Y-%m-%d %H:%M', hours=24))
