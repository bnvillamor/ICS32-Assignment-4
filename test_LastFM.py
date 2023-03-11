'''LastFM unit testing'''
from LastFM import LastFM

def test_data():
    '''LastFM data unit test'''
    lastfm = LastFM()
    assert lastfm.artist == 'keshi'
    lastfm.set_apikey('073959fac063bd9930b9ffdb6f4ff9e7')
    lastfm.load_data()
    assert lastfm.top_album == 'THE REAPER'
    assert lastfm.apikey == '073959fac063bd9930b9ffdb6f4ff9e7'

def test_transclude():
    '''LastFM transclude unit test'''
    lastfm = LastFM()
    lastfm.set_apikey('073959fac063bd9930b9ffdb6f4ff9e7')
    lastfm.load_data()
    message = 'Wow I love @lastfm'
    message2 = lastfm.transclude(message)
    assert message2 == 'Wow I love THE REAPER'
