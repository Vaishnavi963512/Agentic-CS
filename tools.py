import os
import requests

# Get API key from environment variable
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


# -------------------------------
# Weather Tool
# -------------------------------
def get_weather(city: str):
    try:
        if not city:
            return "City not provided."

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        )

        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return "City not found."

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        return f"The temperature in {city.title()} is {temperature}°C with {description}."

    except Exception as e:
        return f"Error: {str(e)}"


# -------------------------------
# (Optional) News Tool (future use)
# -------------------------------
def get_news(topic: str):
    return f"News feature coming soon for topic: {topic}"
