from weather.api.current import CurrentWeather
from weather.api.weekly import WeeklyWeather
from utils.config import Config


class ApiMaster:
    # 单例模式
    __instance = None
    __first_init = False

    def __new__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, city: str = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if not self.__first_init:
            self.__first_init = True
            self.__config = Config().get()['weather-api']
            self.__current_weather = None
            self.__weekly_weather = None
        if city is not None:
            self.city = city

    def fresh_weather(self):
        self.__current_weather = CurrentWeather(self.__config, self.city).get()
        self.__weekly_weather = WeeklyWeather(self.__config, self.city).get()

    def get_current_weather(self) -> dict:
        return self.__current_weather

    def get_weekly_weather(self) -> dict:
        return self.__weekly_weather
