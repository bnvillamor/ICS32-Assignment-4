# Benjoseph Villamor
# villamob@uci.edu
# 62443909


from abc import ABC, abstractmethod


class WebAPI(ABC):

    def _download_url(self, url: str) -> dict:
        # TODO: Implement web api request code in a way that supports
        # all types of web APIs
        pass

    def set_apikey(self, apikey: str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
            
        '''
        #TODO: assign apikey value to a class data attribute that can be accessed by class members
        self._apikey = apikey
        return self._apikey

    @abstractmethod
    def load_data(self):
        '''
        Calls the web api using the required values and stores the response in class data attributes.
            
        '''
        #TODO: use the apikey data attribute and the urllib module to request data from the web api. 
        # See sample code at the begining of Part 1 for a hint.
        
        #TODO: assign the necessary response data to the required class data attributes
        pass

    @abstractmethod
    def transclude(self, message: str) -> str:
        pass
