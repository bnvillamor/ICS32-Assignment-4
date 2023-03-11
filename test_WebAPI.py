'''WebAPI unit testing'''
import pytest
from LastFM import LastFM
import WebAPI


def test_download_LastFM():
    '''WebAPI unit test'''
    with pytest.raises(WebAPI.Error403):
        lastfm = LastFM()
        lastfm.set_apikey('073959fac063bd9930b9ffdb6f4ff9e')
        lastfm.load_data()
    with pytest.raises(WebAPI.Error401):
        lastfm = LastFM()
        lastfm.set_apikey('ajlsdf')
        lastfm.load_data()
