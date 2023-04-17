import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
city=input("enter the city name\n")
url=f"http://api.weatherapi.com/v1/current.json?key=06381ef020e44b4f9e4185336232803&q={city}"
r=requests.get(url)
#print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
print(w)
speak.Speak(f"The current temperature of {city} is {w} degree celcius")
