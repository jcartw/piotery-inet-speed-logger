import time

from lib.inet_speed import run_mock_speed_test
from lib.weather import get_mock_weather
from lib.logging import Logger
from lib.time_util import get_unix_timestamp

REPORT_RATE = 10  # seconds
logger = Logger(stdout_on=False)

time_now = get_unix_timestamp()
time_next_report = time_now + REPORT_RATE

while True:

    time_now = get_unix_timestamp()

    logger.log("main loop...")

    if time_now > time_next_report:
        logger.log("Collecting measurements...")

        logger.log("Report to cloud...")
        time_next_report = time_now + REPORT_RATE

    time.sleep(1.0)
