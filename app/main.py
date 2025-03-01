import os
import requests
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        print("Error: API_KEY is not set")
        return

    CITY = "Paris"
    COUNTRY = "FR"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": f"{CITY},{COUNTRY}",
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"].capitalize()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        print(f"{CITY}/{COUNTRY} {current_time} Weather: {temp} Celsius, {weather_desc}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
