import requests

api_anhtar = '9ec33f7de30acef4fbb71a4fe26a0096'

şehir= input('Şehir ismini giriniz: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={şehir}&appid={api_anhtar}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')