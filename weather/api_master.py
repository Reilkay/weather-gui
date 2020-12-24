from weather.api.current import CurrentWeather
from weather.api.weekly import WeeklyWeather
from utils.config import Config


class ApiMaster:
    def __init__(self) -> None:
        self.__config = Config().get()['weather-api']
        self.__current_weather = None
        self.__weekly_weather = None
        self.city = '沈阳'

    def fresh_weather(self):
        self.__current_weather = CurrentWeather(self.__config, self.city).get()
        self.__weekly_weather = WeeklyWeather(self.__config, self.city).get()

    def get_current_weather(self) -> dict:
        return self.__current_weather

    def get_weekly_weather(self) -> dict:
        return self.__weekly_weather
