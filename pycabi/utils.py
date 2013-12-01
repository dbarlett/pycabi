"""Utility methods used within pyCaBi that are also useful externally.

"""

import datetime
import re


def parse_timestamp(cabi_timestamp):
    """Parse a timestamp from the CaBi status XML file.

    Format: Unix timestamp concatenated with 3-digit millisecond value

    :param cabi_timestamp: timestamp from XML file
    :type cabi_timestamp: str, int
    :returns: datetime object
    :rtype: datetime.datetime

    """

    unix_timestamp = int(str(cabi_timestamp)[0:10])
    milliseconds = int(str(cabi_timestamp)[10:13])
    timestamp = datetime.datetime.fromtimestamp(unix_timestamp)
    return timestamp.replace(microsecond=(milliseconds * 1000))


def parse_trip_duration(duration):
    """Parse a CaBi trip duration from a Trip History Data file

    Format: "14h 26min. 2sec." or "0h 16m 18s"

    :param duration: duration string from file
    :type duration: str
    :returns: trip duration, in seconds
    :rtype: int

    """

    hours = int(re.search(r"\d{1,2}(?=h)", duration).group(0))
    minutes = int(re.search(r"\d{1,2}(?=m)", duration).group(0))
    seconds = int(re.search(r"\d{1,2}(?=s)", duration).group(0))
    return (hours * 3600) + (minutes * 60) + seconds
