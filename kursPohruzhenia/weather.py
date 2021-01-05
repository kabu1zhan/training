import pprint
import requests

API_KEY_YAN_WEATHER = '25ab82db-86d6-42fb-8559-c7bef98cdc2f'
API_KEY_YAN_GEO = '44410a58-82ad-44a7-969a-b8ebfd2eb1c9'


class YanWeatherNow:

    @staticmethod
    def weather_get(geo):
        url = f"https://api.weather.yandex.ru/v1/forecast?lat={geo[0]}&lon" \
            f"={geo[1]}&extra=true"
        headers = {'X-Yandex-API-Key': API_KEY_YAN_WEATHER}
        data = requests.get(url, headers=headers).json()
        forecast = {
            "Температура": data["fact"]["temp"],
            "Давление": data["fact"]["pressure_mm"]
        }
        return forecast
class GeoYandexNow:
    @staticmethod
    def get_point(city):
        url = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY_YAN_GEO}" \
            f"&format=json&geocode={city}"
        data = requests.get(url).json()["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]["Point"]["pos"]
        return data.split()

class CityInfo:

    def __init__(self, city):
        self.city = city
        self._YanWetherNow = YanWeatherNow()
        self._GeoYandexNow = GeoYandexNow()

    def weather_forecast(self):
        geo = self._GeoYandexNow.get_point(self.city)
        print("Гео кординаты")
        print(geo)
        return self._YanWetherNow.weather_get(geo)


def _main():
    city = 'Тараз'
    city_info = CityInfo(city)
    forecast = city_info.weather_forecast()
    print("Погода сейчас")
    print(forecast)

if __name__ == "__main__":
    _main()