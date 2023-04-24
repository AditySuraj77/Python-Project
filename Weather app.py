import requests
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
city = input('Enter the city name : \n')

url = f'https://api.weatherapi.com/v1/current.json?key=30b033aa93b54e56b8b54344232803&q={city}'

r = requests.get(url)
print(r.text)
#print(type(r.text))

wdic = json.loads(r.text)
temp= (wdic['current']['temp_c'])
print(f'{city} Temperature {temp}')
speak.Speak(f"The {city} Tempreture is {temp} degree celcius")