from datetime import datetime
from zoneinfo import ZoneInfo


def compare_timezone_str_to_datetime(timezone_str: str, dt: datetime):
    now = datetime.now(tz=ZoneInfo(timezone_str))
    return now.utcoffset() == dt.utcoffset()
