from main import apikey
import requests

def get_weather(base_url, city_name, api_key):
    param = {
        "q" : city_name,
        "appid" : api_key,
        "units" : "metric" # temperature in Celsius
    }

    response = requests.get(base_url, params=param)

    if response.status_code == 200:
        data = response.json()

        # Data Required
        c = data['name']+", "+data['sys']['country']
        t = data['main']['temp']
        h = data['main']['humidity']
        cd = data['weather'][0]['description'].title()

        # Display Data
        print(f"\nWeather in {c}")
        print(f"Temperature: {t} Celsius")
        print(f"HumidityL {h}%")
        print(f"Condition: {cd}")
    else:
        print("City not found or error fetching data.")

city = input("Enter city name: ")
api_key = apikey
base_url = "http://api.openweathermap.org/data/2.5/weather"
get_weather(base_url, city, api_key)