import os
import pprint

from iotery_embedded_python_sdk import Iotery
from lib.time_util import get_unix_timestamp


class IoteryConnection(object):

    def __init__(self):
        self.iotery = Iotery()
        try:
            self.key = os.environ["IOTERY_DEVICE_KEY"]
            self.serial = os.environ["IOTERY_DEVICE_SERIAL"]
            self.secret = os.environ["IOTERY_DEVICE_SECRET"]
            self.team_uuid = os.environ["IOTERY_TEAM_UUID"]
            self.login()
            self.me = self.iotery.getMe()
        except:
            raise Exception("Error: Iotery device credentials not found.")

    def login(self):

        login_data = {"key": self.key,
                      "serial": self.serial,
                      "secret": self.secret,
                      "teamUuid": self.team_uuid}
        try:
            login_res = self.iotery.getDeviceTokenBasic(data=login_data)
            self.iotery.set_token(login_res["token"])
        except:
            raise Exception("Error: iotery device login failed")

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
                self.iotery.postData(deviceUuid=device_uuid,
                                     opts=opts, data={"packets": packets})
                return {"status": "success"}
            except:
                # perform another login if post data failed
                self.login()

        return {"status": "failed"}


if __name__ == "__main__":

    pp = pprint.PrettyPrinter(indent=4)
    ioteryConn = IoteryConnection()
