import os
import pprint

from iotery_embedded_python_sdk import Iotery


class IoteryConnection(object):

    def __init__(self):
        self.device_info = {}
        self.iotery = Iotery()
        self.token = ""
        try:
            self.key = os.environ["IOTERY_DEVICE_KEY"]
            self.serial = os.environ["IOTERY_DEVICE_SERIAL"]
            self.secret = os.environ["IOTERY_DEVICE_SECRET"]
            self.team_uuid = os.environ["IOTERY_TEAM_UUID"]
        except:
            raise Exception("Error: Iotery device credentials not found.")

    def login(self):

        login_data = {"key": self.key,
                      "serial": self.serial,
                      "secret": self.secret,
                      "teamUuid": self.team_uuid}

        self.device_info = self.iotery.getDeviceTokenBasic(data=login_data)
        self.token = self.device_info["token"]

    def get_token(self):
        return self.token


if __name__ == "__main__":

    pp = pprint.PrettyPrinter(indent=4)

    ioteryConn = IoteryConnection()
    ioteryConn.login()

    token = ioteryConn.get_token()
    pp.pprint(token)
