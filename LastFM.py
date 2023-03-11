'''LastFM child class from WebAPI'''
# Benjoseph Villamor
# villamob@uci.edu
# 62443909

# key: 073959fac063bd9930b9ffdb6f4ff9e7
from WebAPI import WebAPI


class LastFM(WebAPI):
    '''LastFM child class from WebAPI'''
    def __init__(self, artist='keshi'):
        self.artist = artist

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in
        class data attributes.

        '''
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist={self.artist}&api_key={self.apikey}&format=json"
        fm_obj = super()._download_url(url)
        self.top_album = fm_obj['topalbums']['album'][0]['name']

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
            
        :returns: The transcluded message
        '''
        message = message.replace('@lastfm', str(self.top_album))
        return message
