import requests

api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return "City not found."

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"The temperature in {city.title()} is {temperature}°C with {description}."