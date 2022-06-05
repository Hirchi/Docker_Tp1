import requests
import json
from datetime import datetime as dt
import os
api_key = "2ceb1995c8cc45dbdfd4e287128c7057"
lat = os.environ['LAT']
lon = os.environ['LONG']
url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
response = requests.get(url)
data = json.loads(response.text)
print(data)


