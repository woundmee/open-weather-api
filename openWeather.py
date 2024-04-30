"""
API:            OpenWeather
Create date:    30.04.2024
"""

import urllib.request
import json
from datetime import datetime

token = '48e29bf30d49eec1010180dfde7244c1'
url = 'https://api.openweathermap.org/data/2.5/weather?'
lat = 69.35579
lon = 88.189294

try:
    weather_data = urllib.request.urlopen(f'{url}lat={lat}&lon={lon}&units=metric&appid={token}')
    response = weather_data.read()

    jsn = json.loads(response)

    date = datetime.today().strftime('%d.%m.%y %H:%M')

    status = jsn['cod']  # код (200)
    country = jsn['sys']['country']  # страна
    city = jsn['name']  # город
    visibility = jsn['visibility']  # видимость
    temp = jsn['main']['temp']  # температура
    temp_feels_like = jsn['main']['feels_like']  # ощущается, как
    humidity = jsn['main']['humidity']  # влажность
    wind_speed = jsn['wind']['speed']  # скорость ветра в м/с
    wind_gust = jsn['wind']['gust']  # порывы ветра в м/с
    clouds = jsn['clouds']['all']  # облачность

    #print(date, status, country, city, visibility, temp, temp_feels_like, humidity, wind_speed, wind_gust, clouds)

    data = f'Status: {status}\n\nDate: {date}\nCountry: {country}\nCity: {city}\n' \
    f'Visibility: {visibility}%\nTemp: {temp}°C\nTemp feels like: {temp_feels_like}°C\n' \
    f'Humidity: {humidity}%\nWind speed: {wind_speed}m/s\nWind gust: {wind_gust}m/s\nClouds: {clouds}%'
    
    print(data)

except Exception as ex:
    print('❌ ERROR: ', ex)
