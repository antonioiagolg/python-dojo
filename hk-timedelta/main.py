import math
import re

from datetime import timedelta, timezone, datetime

def get_timedelta(zone):
    hours = int(zone[0:3])
    minutes = int(zone[0]+zone[3:5])

    return timedelta(hours=hours, minutes=minutes)

def get_timezone(given_timedelta):
    return timezone(given_timedelta)

def get_month(month):
    return datetime.strptime(month, "%b").month

def get_datetime(timezone, raw_datetime):
    return datetime(int(raw_datetime["year"]), get_month(raw_datetime["month"]), int(raw_datetime["day"]), int(raw_datetime["hour"]), int(raw_datetime["minute"]), int(raw_datetime["second"]), tzinfo=timezone)

def time_delta(t1, t2):
    pattern = r"(\w{3}) (\w{2}) (\w{3}) (\d{4}) (\w{2}):(\w{2}):(\w{2}) ([\+\-]\w{4})"
    time1 = {
        "week": "",
        "day": "",
        "month": "",
        "year": "",
        "hour": "",
        "minute": "",
        "second": "",
        "zone": ""
    }
    
    time2 = {
        "week": "",
        "day": "",
        "month": "",
        "year": "",
        "hour": "",
        "minute": "",
        "second": "",
        "zone": ""
    }

    match = re.search(pattern, t1)
    if match:
        time1["week"], time1["day"], time1["month"], time1["year"], time1["hour"], time1["minute"], time1["second"], time1["zone"] = match.groups()

    match = re.search(pattern, t2)
    if match:
        time2["week"], time2["day"], time2["month"], time2["year"], time2["hour"], time2["minute"], time2["second"], time2["zone"] = match.groups()
    
    timedelta1 = get_timedelta(time1["zone"])
    timedelta2 = get_timedelta(time2["zone"])

    timezone1 = get_timezone(timedelta1)
    timezone2 = get_timezone(timedelta2)

    date1 = get_datetime(timezone1, time1)
    date2 = get_datetime(timezone2, time2)


    result = date1 - date2
    return abs(int(result.total_seconds()))

if __name__ == "__main__":
    result = open("result.txt", "w")

    test_cases = int(input())

    for i in range(test_cases):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)
        result.write(str(delta) + '\n')

    result.close()
