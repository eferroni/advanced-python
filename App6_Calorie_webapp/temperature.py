import requests
from selectorlib import Extractor


class Temperature:

    base_url = "https://www.timeanddate.com/worldclock"
    yaml_path = 'temperature.yaml'
    headers = {
        'user-agent': 'Mozilla/5.0 (platform; rv:geckoversion)/'
                      'Gecko/geckotrail Firefox/firefoxversion'
    }

    def __init__(self, country: str, city: str):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        return f"{self.base_url}/{self.country}/{self.city}"

    def _scrape(self):
        extractor = Extractor.from_yaml_file(self.yaml_path)
        response = requests.get(self._build_url(), headers=self.headers)
        return extractor.extract(response.text)

    def get(self):
        scrapped_content = self._scrape()
        return float(scrapped_content['temp'].replace("°C", "").strip())


if __name__ == '__main__':
    temperature = Temperature(country='brazil',
                              city='porto-alegre').get()
    print(temperature)
