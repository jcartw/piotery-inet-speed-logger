import os
import pprint

from iotery_embedded_python_sdk import Iotery
from lib.time_util import get_unix_timestamp

# Globals
import lib.globals as _GLOBALS_


class IoteryConnection(object):

    def __init__(self):
        self.iotery = Iotery()
        try:
            self.me = {"uuid": "NONE", "deviceType": {"uuid": "NONE"}}
            self.key = os.environ["IOTERY_DEVICE_KEY"]
            self.serial = os.environ["IOTERY_DEVICE_SERIAL"]
            self.secret = os.environ["IOTERY_DEVICE_SECRET"]
            self.team_uuid = os.environ["IOTERY_TEAM_UUID"]
            self.login()
            self.get_device_info()
        except:
            raise Exception("Error: Iotery device credentials not found.")

    def login(self):

        _GLOBALS_.logger.log("Attempting device login...")

        login_data = {"key": self.key,
                      "serial": self.serial,
                      "secret": self.secret,
                      "teamUuid": self.team_uuid}
        try:
            login_res = self.iotery.getDeviceTokenBasic(data=login_data)
            self.iotery.set_token(login_res["token"])
            _GLOBALS_.logger.log("Device login successful.")
        except:
            _GLOBALS_.logger.log("ERROR: iotery device login failed.")

    def get_device_info(self):
        _GLOBALS_.logger.log("Requesting device info from iotery...")

        # allow 2 retries to get info
        for k in range(0, 3):
            try:
                self.me = self.iotery.getMe()
                return {"status": "success"}
            except:
                # perform another login if req failed
                self.login()

        # failure
        _GLOBALS_.logger.log("ERROR: failed to obtain device info.")
        return {"status": "failed"}

    def post_data(self, data):

        timestamp = get_unix_timestamp()
        device_uuid = self.me["uuid"]
        device_type_uuid = self.me["deviceType"]["uuid"]

        packets = [{
            "timestamp": timestamp,
            "deviceUuid": device_uuid,
            "deviceTypeUuid": device_type_uuid,
            "data": data
        }]

        opts = {"includeActiveNotificationInstances": "false",
                "includeUnexecutedCommands": "false"}

        # allow 2 retries to post data
        for k in range(0, 3):
            try:
                res = self.iotery.postData(deviceUuid=device_uuid,
                                           opts=opts, data={"packets": packets})
                return {"status": "success"}
            except:
                # perform another login if post data failed
                self.login()

        # failure
        _GLOBALS_.logger.log("ERROR: failed to post data to iotery.")
        return {"status": "failed"}


if __name__ == "__main__":

    pp = pprint.PrettyPrinter(indent=4)
    ioteryConn = IoteryConnection()
