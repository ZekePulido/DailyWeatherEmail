import requests

api_key = 'api key'

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

CITY = 'Starkville, US'  # The city parameter should be in the format 'city,country'

url = BASE_URL + "q=" + CITY + "&appid=" + api_key

def kelvin_to_celsius_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def statement(max):
    if max > 75:
        return "It is going to be a hotter day!"
    elif max < 65:
        return "It is going to be a cooler day!"
    else:
        return "It will feel great today!"

def email():
    response = requests.get(url)
    data = response.json()

    curr_temp_kelvin = data['main']['temp']
    curr_temp_fahrenheit = round(kelvin_to_celsius_to_fahrenheit(curr_temp_kelvin))

    max_temp_kelvin = data['main']['temp_max']
    max_temp_fahrenheit = round(kelvin_to_celsius_to_fahrenheit(max_temp_kelvin))

    min_temp_kelvin = data['main']['temp_min']
    min_temp_fahrenheit = round(kelvin_to_celsius_to_fahrenheit(min_temp_kelvin))

    clouds = data['weather'][0]['description']

    final = statement(max_temp_fahrenheit)

    return f'''
    Good morning,\n
    The current temperature is: {curr_temp_fahrenheit} degrees outside.
    The high of today is: {max_temp_fahrenheit} degrees outside.
    The low of today is: {min_temp_fahrenheit} degrees outside.
    The clouds are currently {clouds}\n
    {final}
    '''
