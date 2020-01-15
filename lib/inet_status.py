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
        self.dns_server_start_idx = 0

    def get_start_dns(self):
        idx = self.dns_server_start_idx
        return self.dns_server_ips[idx]

    def inet_is_connected(self):

        N = self.number_of_dns_servers

        for k in range(0, N):
            idx = (self.dns_server_start_idx + k) % N
            host = self.dns_server_ips[idx]
            try:
                socket.setdefaulttimeout(self.timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                    (host, self.port))
                self.dns_server_start_idx = (self.dns_server_start_idx + 1) % N
                return True
            except socket.error as ex:
                print(ex)
                pass

        # tried all to no avail
        return False


if __name__ == "__main__":

    # create monitor instance
    monitor = StatusMonitor()

    for k in range(0, 10):
        dns_ip = monitor.get_start_dns()
        print("Next DNS server to check: {0}".format(dns_ip))
        print("")
        print("Device has internet access?")
        is_connected = monitor.inet_is_connected()
        print(is_connected)
        print("")
