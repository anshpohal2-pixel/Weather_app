import requests

api_key = "your api key"

user_city = input("Enter city name: ")

weather_url = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}&units=metric")

weather = weather_url.json()["weather"][0]["main"]
temperature = weather_url.json()["main"]["temp"]
feels_like = weather_url.json()["main"]["feels_like"]
humidity = weather_url.json()["main"]["humidity"]
wind = weather_url.json()["wind"]["speed"]


print(f"The 🌤  weather in {user_city} is currently {weather} \n🌡 Temperature: {temperature}°C and feels like {feels_like}°C \n💧 Humidity: {humidity}% \n💨 Wind Speed: {wind} m/s")
