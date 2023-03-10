import urllib
import json
from urllib import request, error


# key: 9f6cba8a231f19a48f417e2811537884
def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))

    finally:
        if response != None:
            response.close()

    return r_obj


def main() -> None:
    zipc = "92697"
    ccode = "US"
    apikey = "9f6cba8a231f19a48f417e2811537884"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipc},{ccode}&appid={apikey}"

    weather_obj = _download_url(url)
    if weather_obj is not None:
        print(weather_obj['main']['temp_max'])
        #['weather'][0]['description']


if __name__ == '__main__':
    main()
