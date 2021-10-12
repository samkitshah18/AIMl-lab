
import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "8e5b5c251amshc212add6414d43cp14c4c0jsn5ddd339d73e6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
    