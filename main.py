import time

from lib.inet_speed import run_speed_test, run_mock_speed_test
from lib.weather import get_weather, get_mock_weather
from lib.time_util import get_unix_timestamp

# Classes
from lib.circular_logging import Logger
from lib.inet_status import StatusMonitor
from lib.iotery_conn import IoteryConnection

# Globals
import lib.globals as _GLOBALS_


_GLOBALS_.logger = Logger(stdout_on=False)
monitor = StatusMonitor()
iotery_conn = IoteryConnection()

# Get settings from the cloud
device_settings = iotery_conn.get_device_settings()
DATA_REPORT_RATE = device_settings.get("DATA_REPORT_RATE", 1800)  # seconds
INTERNET_CONNECTION_CHECK_RATE = device_settings.get(
    "INTERNET_CONNECTION_CHECK_RATE", 120)  # seconds

# Setup future timestamps
time_now = get_unix_timestamp()
time_next_report = time_now + DATA_REPORT_RATE
time_next_inet_check = time_now + INTERNET_CONNECTION_CHECK_RATE

inet_is_connected = monitor.inet_is_connected()
time_last_inet_connection = time_now  # seconds
inet_downtime = 0  # seconds

while True:

    time_now = get_unix_timestamp()

    # keep rates up to date according to cloud settings
    device_settings = iotery_conn.get_device_settings()
    DATA_REPORT_RATE = device_settings.get(
        "DATA_REPORT_RATE", 1800)  # seconds
    INTERNET_CONNECTION_CHECK_RATE = device_settings.get(
        "INTERNET_CONNECTION_CHECK_RATE", 120)  # seconds

    # Check for internet connection
    if time_now > time_next_inet_check:
        try:
            _GLOBALS_.logger.log("INFO: internet connection check begin")
            inet_is_connected = monitor.inet_is_connected()
            if inet_is_connected:
                # reset last connection timestamp
                time_last_inet_connection = time_now
                _GLOBALS_.logger.log("Connected to the internet")
            else:
                # calculate downtime
                corr_fact = INTERNET_CONNECTION_CHECK_RATE // 2
                inet_downtime = time_now - time_last_inet_connection - corr_fact
                # a correction factor helps minimize the error introduced by INTERNET_CONNECTION_CHECK_RATE
                _GLOBALS_.logger.log(
                    f"Not connected to the internet. The current downtime is {inet_downtime} seconds.")

            time_next_inet_check = time_now + INTERNET_CONNECTION_CHECK_RATE
        except:
            pass

    if time_now > time_next_report and inet_is_connected:
        try:
            _GLOBALS_.logger.log("INFO: iotery data report begin")
            #results_speed_test = run_speed_test()
            #results_weather = get_weather()
            results_speed_test = run_mock_speed_test()
            results_weather = get_mock_weather()

            # sync device info with cloud
            iotery_conn.get_device_info()

            # report data to iotery
            iotery_data = {"INTERNET_DOWNTIME": inet_downtime,
                           "SPEED_TEST_RESULTS": results_speed_test,
                           "WEATHER_DATA": results_weather}
            iotery_status = iotery_conn.post_data(data=iotery_data)

            # set timestamp threshold for next report event and reset inet_downtime
            if iotery_status["status"] == "success":
                time_next_report = time_now + DATA_REPORT_RATE
                inet_downtime = 0
                _GLOBALS_.logger.log("SUCCESS: Data report successful.")
        except:
            pass

    time.sleep(5.0)
