import requests
import tkinter as tk
from tkinter import messagebox

# Your API key
API_KEY = "Your api key"

# Function to get weather
def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"].title()
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = (
            f"📍 City: {city}\n"
            f"🌤 Weather: {weather}\n"
            f"🌡 Temperature: {temperature}°C (feels like {feels_like}°C)\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind Speed: {wind} m/s"
        )
        result_label.config(text=result)
    else:
        messagebox.showerror("Error", "City not found or Invalid API Key!")

# Tkinter GUI setup
root = tk.Tk()
root.title("🌦 Weather App")
root.geometry("400x400")
root.config(bg="#dbe9f4")

# Title
title_label = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"), bg="#dbe9f4")
title_label.pack(pady=10)

# Input field
city_entry = tk.Entry(root, font=("Arial", 14), width=20)
city_entry.pack(pady=10)

# Search button
search_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather, bg="#4CAF50", fg="white")
search_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#dbe9f4", justify="left")
result_label.pack(pady=20)

# Run Tkinter loop
root.mainloop()
