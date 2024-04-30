# OpenWeather API
Получить погоду по любому городу средствами openweathermap.org

## Использование

Для использования скрипта необходимо зарегистрироваться на сайте https://openweathermap.org и получить токен. Для изменения города, необходимо скорректировать следующие данные:

```python
token = 'твой_токен'
lat = # указать широту
lon = # указать долготу
```

## Выполнение
```python
python3 ./openWeather.py
```

Вывод: 

```
Status: 200

Date: 30.04.24 14:53
Country: RU
City: Noril'sk
Visibility: 447%
Temp: -11.85°C
Temp feels like: -18.85°C
Humidity: 90%
Wind speed: 6.87m/s
Wind gust: 9.96m/s
Clouds: 100%
```
