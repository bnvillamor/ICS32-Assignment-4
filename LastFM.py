# Benjoseph Villamor
# villamob@uci.edu
# 62443909

# key: 073959fac063bd9930b9ffdb6f4ff9e7

import urllib
import json
from urllib import request, error


class LastFM:

    def __init__(self, artist='keshi'):
        self.artist = artist

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
        except urllib.error.URLError as err2:
            print('Loss of local connection to Internet')
            print(f'Error code: {err2}')
        except (IndexError, KeyError) as err3:
            print('Invalid data formatting from the remote API')
            print(f'Error code: {err3}')
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
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist={self.artist}&api_key={self.apikey}&format=json"
        fm_obj = self._download_url(url)
        self.top_album = fm_obj['topalbums']['album'][0]['name']

    def transclude(self, message: str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
            
        :returns: The transcluded message
        '''
        #TODO: write code necessary to transclude keywords in the message parameter with appropriate data from API
        lst1 = message.split()
        temp = ''
        temp2 = ''
        for i in lst1:
            if '@lastfm' in i:
                temp = i
                i = i.replace('@lastfm', str(self.top_album))
                temp2 = i
        if temp != '':
            message = message.replace(temp, temp2)
        return message
