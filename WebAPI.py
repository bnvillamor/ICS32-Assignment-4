# Benjoseph Villamor
# villamob@uci.edu
# 62443909

import json
import urllib
from urllib import request, error
from abc import ABC, abstractmethod


class WebAPI(ABC):

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
            print('Invalid data formatting')
            print(f'Error code: {err3}')
        finally:
            if response is not None:
                response.close()

        return r_obj

    def set_apikey(self, apikey: str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
            
        '''
        #TODO: assign apikey value to a class data attribute that can be accessed by class members
        self.apikey = apikey

    @abstractmethod
    def load_data(self):
        '''
        Calls the web api using the required values and stores the response in class data attributes.
            
        '''
        pass

    @abstractmethod
    def transclude(self, message: str) -> str:
        pass
