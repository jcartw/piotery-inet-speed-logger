import os
import requests
import time

## Load credentials
try:
    DARKSKY_API_KEY = os.environ['DARKSKY_API_KEY']
except:
    print("ERROR: credentials not found.")
