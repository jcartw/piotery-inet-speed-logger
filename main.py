import time

from lib.inet_speed import run_mock_speed_test
from lib.inet_status import StatusMonitor
from lib.weather import get_mock_weather
from lib.circular_logging import Logger
from lib.time_util import get_unix_timestamp


REPORT_RATE = 10  # seconds
INET_CONNECTION_CHECK_RATE = 60  # seconds

logger = Logger(stdout_on=False)
monitor = StatusMonitor()

time_now = get_unix_timestamp()
time_next_report = time_now + REPORT_RATE
time_next_inet_check = time_now + INET_CONNECTION_CHECK_RATE

inet_is_connected = monitor.inet_is_connected()
time_last_inet_connection = time_now  # seconds
inet_downtime = 0  # seconds

while True:

    time_now = get_unix_timestamp()

    logger.log("main loop...")

    # Check for internet connection
    if time_now > time_next_inet_check:
        logger.log("Checking for internet connection...")
        inet_is_connected = monitor.inet_is_connected()
        if inet_is_connected:
            # reset last connection timestamp
            time_last_inet_connection = time_now
        else:
            # calculate downtime
            inet_downtime = time_now - time_last_inet_connection
            logger.log(f"Current downtime: {inet_downtime}")

        logger.log("Report to cloud...")
        time_next_report = time_now + REPORT_RATE

    if time_now > time_next_report and inet_is_connected:
        logger.log("Collecting measurements...")

        # report inet_downtime and reset

        logger.log("Report to cloud...")
        time_next_report = time_now + REPORT_RATE

    time.sleep(1.0)
