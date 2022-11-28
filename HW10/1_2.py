# Применил шаблон с импользованием фасадов

from abc import ABC, abstractmethod

class WeatherAPI(ABC):
    @abstractmethod
    def get_temp(self) -> float:
        pass 

class GoogleAPI(WeatherAPI):
    def get_temp(self) -> float:
        return 20


class SomeMeteoApi:
    def get_temp_in_fahrenheit(self) -> float:
        return 451

class MyConverter:
    def __init__(self, source):
        self._source = source

    def get_temp(self):
        temp = self._source.get_temp_in_fahrenheit()
        return (temp - 32) * 5/9


def client_code(api: WeatherAPI) -> None:
    print(f"Temperature in Celsius: {api.get_temp()}")


if __name__ == "__main__":
    google_api = GoogleAPI()
    client_code(google_api)

    some_meteo_api = SomeMeteoApi()
    converted_api = MyConverter(some_meteo_api)
    client_code(converted_api)
