# Benjoseph Villamor
# villamob@uci.edu
# 62443909
import urllib
import json
from urllib import request, error


class OpenWeather:

    def __init__(self, zipcode, ccode):
        self.zipcode = zipcode
        self.ccode = ccode

    def set_apikey(self, apikey:str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service

        '''
        #TODO: assign apikey value to a class data attribute that can be accessed by class members
        self.apikey = apikey

    def _download_url(self, url_to_download: str) -> dict:
        response = None
        r_obj = None

        try:
            response = urllib.request.urlopen(url_to_download)
            json_results = response.read()
            r_obj = json.loads(json_results)

        except urllib.error.HTTPError as err:
            print('Failed to download contents of URL')
            print(f'Status code: {err.code}')

        finally:
            if response is not None:
                response.close()

        return r_obj

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in
        class data attributes.

        '''
        #TODO: use the apikey data attribute and the urllib module to request data from the web api. 
        # See sample code at the begining of Part 1 for a hint.
        #TODO: assign the necessary response data to the required class data attributes
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}"
        weather_obj = self._download_url(url)
        self.temperature = weather_obj['main']['temp']
        self.high_temperature = weather_obj['main']['temp_max']
        self.low_temperature = weather_obj['main']['temp_min']
        self.latitude = weather_obj['coord']['lat']
        self.longitude = weather_obj['coord']['lon']
        self.description = weather_obj['weather'][0]['description']
        self.humidity = weather_obj['main']['humidity']
        self.city = weather_obj['name']
        self.sunset = weather_obj['sys']['sunset']
        self.sunrise = weather_obj['sys']['sunset']
        self.pressure = weather_obj['main']['pressure']

