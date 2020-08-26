#!/usr/bin/env python3

import requests

api = "http://api.openweathermap.org/data/2.5/weather?q=Sao+Paulo&appid=cd70123bfc02f39978477a22ad0efcfa&units=metric"


req = requests.get(api)
data = req.json()
ctemp = data['main']['temp']
print("SP:",int(ctemp))
