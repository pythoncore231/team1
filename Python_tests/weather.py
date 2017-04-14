'''
Created on Mar 23, 2017

@author: vodachuk
'''
import pyowm

city = raw_input("Which city you interesting?: ")

my_api = pyowm.OWM('6364b3b6a97c3d907f9ed245d04fd550')
observation = my_api.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print "In the ", city , "now ", str(temperature), " at celsius."
print "Also, in this city ", w.get_detailed_status()