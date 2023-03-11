'''WebAPI parent class and error handling'''
# Benjoseph Villamor
# villamob@uci.edu
# 62443909

import json
import urllib
from urllib import request, error
from abc import ABC, abstractmethod


class Error404(Exception):
    '''404 Error Exception'''


class Error503(Exception):
    '''503 Error Exception'''


class Error401(Exception):
    '''401 Error Exception'''


class Error400(Exception):
    '''400 Error Exception'''


class Error403(Exception):
    '''403 Error Exception'''


class WebAPI(ABC):
    '''WebAPI parent class for OpenWeather and LastFM'''

    def _download_url(self, url_to_download: str) -> dict:
        response = None
        r_obj = None

        try:
            response = urllib.request.urlopen(url_to_download)
            json_results = response.read()
            r_obj = json.loads(json_results)
        except urllib.error.HTTPError as err:
            if err.code == 404:
                raise Error404(f'{err.code} Error, please try again') from err
            elif err.code == 503:
                raise Error503(f'{err.code} Error, please try again') from err
            elif err.code == 401:
                raise Error401(f'{err.code} Error, please try again') from err
            elif err.code == 403:
                raise Error403(f'{err.code} Error, please try again') from err
            elif err.code == 400:
                raise Error400(f'{err.code} Error, please try again') from err
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
        self.apikey = apikey

    @abstractmethod
    def load_data(self):
        '''
        Calls the web api using the required values and stores the response in class data attributes.

        '''

    @abstractmethod
    def transclude(self, message: str) -> str:
        '''Abstract Transclude method'''
