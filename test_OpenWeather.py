'''OpenWeather unit testing'''
from OpenWeather import OpenWeather

def test_data():
    '''OpenWeather data unit test'''
    weather = OpenWeather()
    assert weather.zipcode == '92697'
    weather.set_apikey('9f6cba8a231f19a48f417e2811537884')
    weather.load_data()
    assert weather.city == 'Irvine'
    assert weather.apikey == '9f6cba8a231f19a48f417e2811537884'
