from datetime import datetime


def get_current_date_utc_timestamp() -> int:
    now = datetime.utcnow()
    timestamp = datetime(year=now.year, month=now.month, day=now.day).timestamp()
    timestamp = int(timestamp)
    return timestamp
