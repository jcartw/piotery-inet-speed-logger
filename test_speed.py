import speedtest
import pprint

pp = pprint.PrettyPrinter(indent=4)

servers = []
threads = None

print("Initializing Speedtest...")
s = speedtest.Speedtest()
print("Getting servers...")
s.get_servers(servers)
print("Getting best server...")
s.get_best_server()
print("Test download...")
s.download(threads=threads)
print("Test upload...")
s.upload(threads=threads)
print("Share results...")
print(s.results.share())

print("Results dict")
results_dict = s.results.dict()
pp.pprint(results_dict)
print("")

# {   'bytes_received': 70357356,
#     'bytes_sent': 25001984,
#     'client': {   'country': 'BR',
#                   'ip': '179.218.139.13',
#                   'isp': 'NET Virtua',
#                   'ispdlavg': '0',
#                   'isprating': '3.7',
#                   'ispulavg': '0',
#                   'lat': '-22.9201',
#                   'loggedin': '0',
#                   'lon': '-43.3307',
#                   'rating': '0'},
#     'download': 55614422.39169828,
#     'ping': 14.577,
#     'server': {   'cc': 'BR',
#                   'country': 'Brazil',
#                   'd': 15.057214026458771,
#                   'host': 'test.afinet.com.br:8080',
#                   'id': '22448',
#                   'lat': '-22.7858',
#                   'latency': 14.577,
#                   'lon': '-43.3119',
#                   'name': 'Duque de Caxias',
#                   'sponsor': 'AFINET',
#                   'url': 'http://test.afinet.com.br:8080/speedtest/upload.php'},
#     'share': 'http://www.speedtest.net/result/8944746012.png',
#     'timestamp': '2020-01-14T15:13:59.007908Z',
#     'upload': 19763153.263908423}

