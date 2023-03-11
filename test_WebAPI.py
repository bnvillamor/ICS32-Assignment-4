'''WebAPI unit testing'''
import pytest
from LastFM import LastFM


def test_download_LastFM():
    '''WebAPI unit test'''
    with pytest.raises(AttributeError):
        lastfm = LastFM()
        lastfm.set_apikey('073959fac063bd9930b9ffdb6f4ff9e')
        lastfm.load_data()
