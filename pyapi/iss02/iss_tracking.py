#!/usr/bin/env python3

import turtle
import urllib.request
import json

#trace the ISS
eoss = 'http://api.open-notify.org/iss-now.json'

#call the webserv
trackiss = urllib.request.urlopen(eoss)

#put into the file object
ztrack = trackiss.read()

#store JSON in Python data structure, result
result = json.loads(ztrack.decode('utf-8'))

#display the Pythonic data
print('\n\nConverted Python data')
print(result)
input('\nISS data retrieved and converted. Press any key to continue')

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('\nLatitude:', lat)
print('Longitude:', lon)

screen = turtle.Screen() #create a screen object
screen.setup(720, 360) #and set the resolution

screen.setworldcoordinates(-180, -90, 180, 90) #sets a particular latitude and longitude
screen.bgpic('iss_map.gif') #and add our map to the screen

screen.register_shape('spriteiss.gif') #register the tiny ISS
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

#the ISS starts off in the center of the map, but we will move it to the correct location
#typically, we report latitude and longitude, but these are actually (x,y) screen coordinates
#so they need to be reversed
lon = round(float(lon))
lat = round(float(lat))
iss.penup()
iss.goto(lon, lat)
turtle.mainloop() #this line must ALWAYS be at the bottom of the script-it keeps the graphic from closing!




