import requests
api_key = "c230f0d60a8013246cbde6a8ef39359a"
city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}
try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    print(f"\n📍 City       : {data['name']}")
    print(f"🌡️  Temp       : {data['main']['temp']}°C")
    print(f"🤔 Feels Like : {data['main']['feels_like']}°C")
    print(f"💧 Humidity   : {data['main']['humidity']}%")
    print(f"🌤️  Weather    : {data['weather'][0]['description']}")
    print(f"💨 Wind Speed : {data['wind']['speed']} m/s")
except requests.Exceptions.HTTPError:
    print("Please check the city name and try again.")
except requests.Exceptions.ConnectionError:
    print("Network error. Please check your connection and try again.")