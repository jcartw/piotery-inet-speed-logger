import speedtest
import pprint


def run_mock_speed_test():
    results = {
        "bytes_received": 70357356,
        "bytes_sent": 25001984,
        "client": {"country": "BR",
                   "ip": "179.218.139.13",
                   "isp": "NET Virtua",
                   "ispdlavg": "0",
                   "isprating": "3.7",
                   "ispulavg": "0",
                   "lat": "-22.9201",
                   "loggedin": "0",
                   "lon": "-43.3307",
                   "rating": "0"},
        "download": 55614422.39169828,
        "ping": 14.577,
        "server": {"cc": "BR",
                   "country": "Brazil",
                   "d": 15.057214026458771,
                   "host": "test.afinet.com.br:8080",
                   "id": "22448",
                   "lat": "-22.7858",
                   "latency": 14.577,
                   "lon": "-43.3119",
                   "name": "Duque de Caxias",
                   "sponsor": "AFINET",
                   "url": "http://test.afinet.com.br:8080/speedtest/upload.php"},
        "share": "http://www.speedtest.net/result/8944746012.png",
        "timestamp": "2020-01-14T15:13:59.007908Z",
        "upload": 19763153.263908423}

    return results


def run_speed_test():
    servers = []
    threads = None

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    results = s.results.dict()

    return results


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)

    print("Mock speed results")
    print("----------------------------")
    speed_results = run_mock_speed_test()
    pp.pprint(speed_results)
    print("")

    print("Actual speed results")
    print("----------------------------")
    # speed_results = run_speed_test()
    # pp.pprint(speed_results)
    print("")
