import requests

# Request parameters
NOMINATIM_URL = 'https://nominatim.openstreetmap.org/search'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/forecast'
WEATHER_APPID = '6170e39b3be9832d85279c4719643235'


def forecast(**kwargs):
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
    print('Weather for {}, {}:'.format(weather_info['city']['name'], weather_info['city']['country']))
    for index, weather in enumerate(weather_info['list']):
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
