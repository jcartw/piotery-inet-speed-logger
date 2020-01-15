import os
import requests
import time
import pprint


def get_mock_weather():
    results = {"currently":
               {"apparentTemperature": 85.32,
                "cloudCover": 0.92,
                "dewPoint": 68.1,
                "humidity": 0.62,
                   "icon": "cloudy",
                   "ozone": 261.9,
                   "precipIntensity": 0,
                   "precipProbability": 0,
                   "pressure": 1015.2,
                   "summary": "Overcast",
                   "temperature": 82.31,
                   "time": 1579022112,
                   "uvIndex": 5,
                   "visibility": 10,
                   "windBearing": 120,
                   "windGust": 11.31,
                   "windSpeed": 9.03},
               "flags": {"nearest-station": 6.412,
                         "sources": ["cmc", "gfs", "icon", "isd", "madis"],
                         "units": "us"},
               "latitude": -22.98548,
               "longitude": -43.22283,
               "offset": -3,
               "timezone": "America/Sao_Paulo"}

    return results


def get_weather():

    # Load credentials
    try:
        DARKSKY_API_KEY = os.environ["DARKSKY_API_KEY"]
        LATITUDE = os.environ["LATITUDE"]
        LONGITUDE = os.environ["LONGITUDE"]
    except:
        print("ERROR: credentials not found.")
        return None

    # Get weather data from darksky
    url = f"https://api.darksky.net/forecast/{DARKSKY_API_KEY}/{LATITUDE},{LONGITUDE}?exclude=hourly,daily"
    res = requests.get(url)
    weather_data = res.json()
    return weather_data


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)

    print("Mock weather results")
    print("----------------------------")
    weather_results = get_mock_weather()
    pp.pprint(weather_results)
    print("")

    print("Actual weather results")
    print("----------------------------")
    #weather_results = get_weather()
    # pp.pprint(weather_results)
    print("")
