from lib.time_util import get_utc_timestamp_str

from collections import deque

CACHE_SIZE = 50


class Logger(object):
    def __init__(self, stdout_on=False):
        self.log_cache = deque(maxlen=CACHE_SIZE)
        self.stdout_on = stdout_on

    def set_stdout_on(flag):
        self.stdout_on = flag

    def log(self, text):

        if not isinstance(text, str):
            raise Exception("The argument 'text' must be a string")

        # Add timestamp to log
        line = get_utc_timestamp_str() + ": " + text
        self.log_cache.append(line)

        # write log cache to file
        f = open("piotery_inet_speed_logger.log", "w")
        for line in self.log_cache:
            f.write(line + "\n")
        f.close()

        if(self.stdout_on):
            print(line)

    def show_all_logs(self):
        for line in self.log_cache:
            print(line)
