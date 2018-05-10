"""
This file contain logic for weather_forecast script.
Defined functions:
    forecast(**kwargs) -> None:
        kwargs -- command line arguments passed by user
        Make get requests to OpenWeather and Nominatim API using 'requests' module.
        First: make get request to Nominatim and receive longitude and latitude of requested location.
        Second: pass geo coordinates to OpenWeather API and receive weather five day forecast for every
                three hours
        Third: call print_work to make a fancy output

    print_work(print_work(weather_info, days)) -> None:
        Gets weather info and number of days to show forecast for and prints it.
"""
import requests

# Request parameters
NOMINATIM_URL = 'https://nominatim.openstreetmap.org/search'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/forecast'
WEATHER_APPID = '6170e39b3be9832d85279c4719643235'


def forecast(**kwargs):
    """
    This function handles work with OpenWeather and Nominatim API's.
    Firstly it send get request with desired location to Nominatim and gets a response in json format.
    If response is empty then prints that such location not found. Valid response contains longitude
    and latitude of requested location.
    These coordinates transferred to OpenWeather as location to get weather for. OpenWeather returns a
    hourly 5 day forecast.

    :param kwargs: Options got from command line
    :return: None
    """
    # Get city and country from from kwargs
    nominatim_parameters = dict(q=kwargs['location'], format='json', limit=1, dedupe=0)
    try:
        location_req = requests.get(url=NOMINATIM_URL, params=nominatim_parameters)
    except requests.ConnectionError:
        print('No internet! Check your internet connection and try again.')
        return
    # Check if request was satisfied
    if not location_req.ok:
        print('Nominatim is currently unavailable. Try again later or contact <fedoseevalex@inbox.ru>.')
        return
    # Check response length
    if not len(location_req.json()):
        print('Sorry, I could find requested location. Try to ask the other way.')
        return
    # Get place coordinates
    try:
        location_for_weather = dict(lat=location_req.json()[0]['lat'], lon=location_req.json()[0]['lon'])
    except requests.ConnectionError:
        print('No internet! Check your internet connection and try again.')
        return

    # Make weather parameters
    weather_parameters = dict(APPID=WEATHER_APPID, units='metric', **location_for_weather)
    weather_req = requests.get(url=WEATHER_URL, params=weather_parameters)
    # Check weather request
    if not weather_req.ok:
        print('OpenWeatherMap is currently unavailable. Try again later or contact <fedoseevalex@inbox.ru>.')
        print('Error: {}'.format(weather_req.json()['message']))
        return

    print_work(weather_req.json(), kwargs['days'])


def print_work(weather_info, days):
    """
    This function handle printing in fancy manner.

    :param weather_info: OpenWeather response. Contains forecast for each 3 hours for five days.
    :param days: Number of days to show forecast for.
    :return: None
    """
    print('Weather for {}, {}:'.format(weather_info['city']['name'], weather_info['city']['country']))
    for index, weather in enumerate(weather_info['list']):
        # As OpenWeather response contains forecast for each 3 hours of five further days
        # it would be convenient to split forecast by day.
        # So for 40 given forecasts each 8 of them belong to one day.
        # And 8 here is to split forecast for each day.
        module, remainder = divmod(index, 8)
        if module >= days:
            break
        if remainder == 0:
            print('\nDate: {}'.format(weather['dt_txt'].split(' ')[0]))
            print('\tPressure: {} hPa'.format(weather['main']['pressure']))
            print('\tHumidity: {}%'.format(weather['main']['humidity']))
            print('\tWind speed: {} m/s'.format(weather['wind']['speed']))
            print('\t{:<12} {:<12} {:12}'.format('Time', 'Temperature,°C', 'Description'))
        print('\t{:<12} {:^12} {:>12}'.format(weather['dt_txt'].split(' ')[1], weather['main']['temp'],
                                              weather['weather'][0]['description'].capitalize()))
    print('\nWrong location? Give me more information next time -> weather_forecast "Detailed place description..."')

# Add documentation and maybe tests
