# Benjoseph Villamor
# villamob@uci.edu
# 62443909

# key: 073959fac063bd9930b9ffdb6f4ff9e7
from WebAPI import WebAPI


class LastFM(WebAPI):

    def __init__(self, artist='keshi'):
        self.artist = artist

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in
        class data attributes.

        '''
        #TODO: use the apikey data attribute and the urllib module to request data from the web api. 
        # See sample code at the begining of Part 1 for a hint.
        #TODO: assign the necessary response data to the required class data attributes
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist={self.artist}&api_key={self.apikey}&format=json"
        fm_obj = super()._download_url(url)
        self.top_album = fm_obj['topalbums']['album'][0]['name']

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
            
        :returns: The transcluded message
        '''
        #TODO: write code necessary to transclude keywords in the message parameter with appropriate data from API
        message = message.replace('@lastfm', str(self.top_album))
        return message
