import time

from datetime import datetime


def get_unix_timestamp():
    return int(time.time())


def get_utc_timestamp_str():
    utc_now = datetime.utcnow()
    out = utc_now.strftime("%Y.%m.%d [%H:%M:%S] UTC")
    return out


if __name__ == "__main__":

    unix_timestamp = get_unix_timestamp()
    print(f"Unix Timestamp")
    print(unix_timestamp)
    print("")

    out = get_utc_timestamp_str()
    print("UTC String")
    print(out)
