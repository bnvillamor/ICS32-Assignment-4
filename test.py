from LastFM import LastFM

artist = 'Cher'
apikey = "073959fac063bd9930b9ffdb6f4ff9e7"
last_fm = LastFM(artist)
last_fm.set_apikey(apikey)
last_fm.load_data()
print(last_fm.top_album)
