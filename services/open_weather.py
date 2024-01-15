import os
import requests
from dotenv import load_dotenv

load_dotenv()

class OpenWeatherService:
    """
        This class is responsible for getting the weather forecast from OpenWeather API
    """
    def __init__(self):
        self.api_key = os.environ['OPEN_WEATHER_API_KEY']

    def get_weather(self, city: str) -> dict:
        location = self._get_lat_and_lon(city)

        url = f"http://api.openweathermap.org/data/2.5/forecast?lat={location.get('lat')}&lon={location.get('lon')}&appid={self.api_key}"

        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def _get_lat_and_lon(self, city: str) -> dict:
        if city:
            BaseException("City is required")

        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()

        lat = response.json()[0]['lat']
        lon = response.json()[0]['lon']
        
        return {
            "lat": lat,
            "lon": lon
        }
    