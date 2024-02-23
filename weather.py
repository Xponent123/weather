import pyttsx3
import requests
import json
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",130)
engine.say("enter city")
engine.runAndWait()
city=input("enter city: ")
url = f"http://api.weatherstack.com/current?access_key=yourkeyquery={city}" # add your api key instead of yourkey
r=requests.get(url)
dic = json.loads(r.text)
engine.say(f"weather report of {city} is")
engine.runAndWait()
print(f"weather report of {city}: ")
engine.say(f"temperature of {city} is: {dic['current']['temperature']}")
engine.runAndWait()
print(f"temperature: {dic['current']['temperature']}")
engine.say(f"it feels like {dic['current']['feelslike']}")
engine.runAndWait()
print(f"feels like: {dic['current']['feelslike']}")
engine.say(f"humidiy is {dic['current']['humidity']}")
engine.runAndWait()
print(f"humidity: {dic['current']['humidity']}")
engine.say(f"wind speed is {dic['current']['wind_speed']} and wind direction is {dic['current']['wind_dir']}")
engine.runAndWait()
print(f"wind speed: {dic['current']['wind_speed']}")
print(f"wind direction: {dic['current']['wind_dir']}")

print(f"latitude: {dic['location']['lat']}")
print(f"longitude: {dic['location']['lon']}")
print(f"timezone: {dic['location']['timezone_id']}")
print(f"current time: {dic['location']['localtime']}")


print(f"weather description: {dic['current']['weather_descriptions']}")


print(f"precipitation: {dic['current']['precip']}")
print(f"visibility: {dic['current']['visibility']}")
engine.say("thank you")
engine.runAndWait()
print("Thank you")
