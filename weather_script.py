import requests

api_key = 'xxxxxxxxxxxxxxxxxxxxx' # <- needed to obtain from page openweather.map
city = input('Enter the city name:\n')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature {temp} K, which is {round(int(temp) - 273.15)} C.')
    print(f" Description: {desc}")
else:
    print("Error fetching weather data")
