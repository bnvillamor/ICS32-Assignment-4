'''OpenWeather child class from WebAPI'''
# Benjoseph Villamor
# villamob@uci.edu
# 62443909
from WebAPI import WebAPI


class OpenWeather(WebAPI):
    '''OpenWeather child class from WebAPI'''
    def __init__(self, zipcode='92697', ccode='US'):
        self.zipcode = zipcode
        self.ccode = ccode

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in
        class data attributes.

        '''
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}"
        self.weather_obj = super()._download_url(url)
        if self.weather_obj is not None:
            self.temperature = self.weather_obj['main']['temp']
            self.high_temperature =  self.weather_obj['main']['temp_max']
            self.low_temperature =  self.weather_obj['main']['temp_min']
            self.latitude =  self.weather_obj['coord']['lat']
            self.longitude =  self.weather_obj['coord']['lon']
            self.description =  self.weather_obj['weather'][0]['description']
            self.humidity =  self.weather_obj['main']['humidity']
            self.city =  self.weather_obj['name']
            self.sunset =  self.weather_obj['sys']['sunset']

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude

        :returns: The transcluded message
        '''
        if self.weather_obj is not None:
            message = message.replace('@weather', str(self.high_temperature))
        return message
