import logging

import requests

logger = logging.getLogger(__name__)


def get_weather_data():
    try:
        response = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')
        weather_from_hko = response.json()

        # using data from "Hong Kong Observatory"
        weather_data = {
            'humidity': weather_from_hko['humidity']['data'][0]['value'],
            'temperature': [
                _data['value']
                for _data in weather_from_hko['temperature']['data']
                if _data['place'] == 'Hong Kong Observatory'
            ][0],
            'uvindex': weather_from_hko['uvindex']
        }
    except BaseException:
        logger.warning('Error found.', exc_info=True)
        weather_data = dict()

    return weather_data


if __name__ == '__main__':
    weather = get_weather_data()
    print(weather)
