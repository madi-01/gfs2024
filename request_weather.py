import requests
import json

url = f'https://api.openweathermap.org/data/2.5/weather?q=Achern,de&lang=de&units=metric&appid=6adb2c33960716c89b149d1523a0e3cd'
response = requests.get(url).json()

temperatur = response['main']['temp']
luftfeuchtigkeit = response['main']['humidity']
beschreibung = response['weather'][0]
wind = response['wind']['speed']

print ("----------------------")
print ("Achern:")
print ("Temperatur: " + str(temperatur) + "°C")
print ("Luftfeuchtigkeit: " + str(luftfeuchtigkeit) + "%")
print ("Beschreibung: " + str(beschreibung['description']))
print ("Windgeschwindigkeit: " + str(wind) + "km/h")