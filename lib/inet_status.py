import socket


class StatusMonitor(object):

    def __init__(self, timeout=3, port=53):
        self.dns_server_ips = ["8.8.8.8",
                               "8.8.4.4",
                               "9.9.9.9",
                               "149.112.112.112",
                               "1.1.1.1",
                               "1.0.0.1"]
        self.number_of_dns_servers = len(self.dns_server_ips)
        self.timeout = timeout
        self.port = port
        self.dns_server_start_idx = -1

    def inet_is_connected(self):

        N = self.number_of_dns_servers
        self.dns_server_start_idx = (self.dns_server_start_idx + 1) % N

        for k in range(0, N):
            idx = (self.dns_server_start_idx + k) % N
            host = self.dns_server_ips[idx]
            try:
                print("trying to connect to: {0}".format(host))
                socket.setdefaulttimeout(self.timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                    (host, self.port))
                return True
            except socket.error as ex:
                print(ex)
                pass

        # tried all to no avail
        return False


if __name__ == "__main__":

    # create monitor instance
    monitor = StatusMonitor()

    print("Device has internet access?")
    is_connected = monitor.inet_is_connected()
    print(is_connected)
    print("")

    print("Device has internet access?")
    is_connected = monitor.inet_is_connected()
    print(is_connected)
    print("")

    print("Device has internet access?")
    is_connected = monitor.inet_is_connected()
    print(is_connected)
    print("")
