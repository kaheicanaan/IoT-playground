import sys
import unittest

sys.path.append('src')


class MyTestCase(unittest.TestCase):
    @unittest.skip("This code work on OSX only")
    def test_temperature_readings(self):
        self.fail()

    def test_weather_data(self):
        import weather
        weather_data = weather.get_weather_data()
        for attr in ['humidity', 'temperature', 'uvindex']:
            self.assertIn(attr, weather_data)


if __name__ == '__main__':
    unittest.main()
