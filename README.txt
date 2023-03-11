The a4 program builds upon a3 by providing new features for the user. It retrieves data from
2 web API's: OpenWeather and LastFM. It uses transclusion to replace the keywords "@weather"
and "@lastfm" to the specific data retrieved from the API's. For this program, "@weather" is
replaced by the temperature high for the given zipcode and country code. @lastfm is replaced
by the top album for the given artist. The user is required to input the zipcode, country
code, and artist when they choose to add a post. The new modules for the program are
WebAPI.py, LastFM.py, and OpenWeather.py. WebAPI is a parent class that contains the code
to access a given API and set the key. The LastFM and OpenWeather classes inherit the WebAPI
class and use abstract methods to load and transclude there respective data. The program 
also includes sufficient PDOCdocumentation, adheres to reasonable pycodestyle and pylint
rules, and unit tests with 88% code coverage. 