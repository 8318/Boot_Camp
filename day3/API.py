from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

import urllib.request
with urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=dc008cc4b840428ceb20b2e304c2f191') as response:
    map = response.read()
    print ("TODAYS WEATHER in the world")
    print (map)
