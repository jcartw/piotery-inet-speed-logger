import urllib.request as request
import pprint
import socket


class StatusMonitor(object):

    def __init__(self):
        self.ip_dict = {"google.com": "172.217.162.174",
                        "amazon.com": "176.32.98.166", "facebook.com": "31.13.74.350"}
        self.refresh_host_ips()

    def get_ip_dict(self):
        return self.ip_dict

    def get_host_ip_by_url(self, url):
        return socket.gethostbyname(url)

    def refresh_host_ips(self):
        if self.inet_is_connected:
            for url in self.ip_dict.keys():
                self.ip_dict[url] = self.get_host_ip_by_url(url)

    def inet_is_connected(self):
        for url in self.ip_dict.keys():
            try:
                host_url = "http://" + self.ip_dict[url]
                request.urlopen(host_url, timeout=2)
                return True
            except:
                pass

        return False


if __name__ == "__main__":

    pp = pprint.PrettyPrinter(indent=4)

    # create monitor instance
    monitor = StatusMonitor()

    print("Device has internet access")
    is_connected = monitor.inet_is_connected()
    print(is_connected)
    print("")

    if is_connected:
        print("IP Dictionary")
        monitor.refresh_host_ips()
        ip_dict = monitor.get_ip_dict()
        pp.pprint(ip_dict)
        print("")
