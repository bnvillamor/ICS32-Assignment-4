# Benjoseph Villamor
# villamob@uci.edu
# 62443909
from WebAPI import WebAPI
# 9f6cba8a231f19a48f417e2811537884


class OpenWeather(WebAPI):

    def __init__(self, zipcode='92697', ccode='US'):
        self.zipcode = zipcode
        self.ccode = ccode

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in
        class data attributes.

        '''
        # TODO: use the apikey data attribute and the urllib module to request data from the web api.
        # See sample code at the begining of Part 1 for a hint.
        # TODO: assign the necessary response data to the required class data attributes
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}"
        weather_obj = super()._download_url(url)
        if weather_obj is not None:
            self.temperature = weather_obj['main']['temp']
            self.high_temperature = weather_obj['main']['temp_max']
            self.low_temperature = weather_obj['main']['temp_min']
            self.latitude = weather_obj['coord']['lat']
            self.longitude = weather_obj['coord']['lon']
            self.description = weather_obj['weather'][0]['description']
            self.humidity = weather_obj['main']['humidity']
            self.city = weather_obj['name']
            self.sunset = weather_obj['sys']['sunset']

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude

        :returns: The transcluded message
        '''
        # TODO: write code necessary to transclude keywords in the message parameter with appropriate data from API
        message = message.replace('@weather', str(self.high_temperature))
        return message
